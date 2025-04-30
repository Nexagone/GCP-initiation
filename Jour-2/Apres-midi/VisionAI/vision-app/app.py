import os
import uuid
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from google.cloud import vision
from google.cloud import storage
import tempfile
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

# Configuration des credentials GCP
CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), 'credentials.json')
if not os.path.exists(CREDENTIALS_PATH):
    raise FileNotFoundError(f"Le fichier credentials.json n'a pas été trouvé à l'emplacement : {CREDENTIALS_PATH}")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = CREDENTIALS_PATH

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

# Configuration
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
BUCKET_NAME = 'visionai-img-demo'  # À remplacer par le nom de votre bucket

# Fonction pour générer une URL signée
def generate_signed_url(bucket_name, blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    
    # URL valide pendant 1 heure
    expiration = datetime.now() + timedelta(hours=1)
    
    url = blob.generate_signed_url(
        version="v4",
        expiration=expiration,
        method="GET"
    )
    return url

# Vérification des extensions de fichiers autorisées
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route principale
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Route pour l'analyse d'image
@app.route('/analyze', methods=['POST'])
def analyze_image():
    # Vérifier qu'un fichier a été envoyé
    if 'file' not in request.files:
        flash('Aucun fichier sélectionné')
        return redirect(request.url)
    
    file = request.files['file']
    
    # Si l'utilisateur ne sélectionne pas de fichier
    if file.filename == '':
        flash('Aucun fichier sélectionné')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        # Créer un nom de fichier sécurisé et unique
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        
        # Sauvegarder temporairement le fichier
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            file.save(temp.name)
            temp_file_path = temp.name
        
        try:
            # Envoyer le fichier à GCS (Google Cloud Storage)
            storage_client = storage.Client()
            bucket = storage_client.bucket(BUCKET_NAME)
            blob = bucket.blob(f"uploads/{unique_filename}")
            blob.upload_from_filename(temp_file_path)
            
            # Générer l'URL signée pour l'image
            image_url = generate_signed_url(BUCKET_NAME, f"uploads/{unique_filename}")
            
            # Analyser l'image avec Vision API
            vision_client = vision.ImageAnnotatorClient()
            image = vision.Image()
            image.source.image_uri = f"gs://{BUCKET_NAME}/uploads/{unique_filename}"
            
            # Définir les types d'analyse à effectuer
            features = [
                vision.Feature(type_=vision.Feature.Type.LABEL_DETECTION),
                vision.Feature(type_=vision.Feature.Type.FACE_DETECTION),
                vision.Feature(type_=vision.Feature.Type.LANDMARK_DETECTION),
                vision.Feature(type_=vision.Feature.Type.TEXT_DETECTION),
                vision.Feature(type_=vision.Feature.Type.SAFE_SEARCH_DETECTION)
            ]
            
            # Effectuer l'analyse
            response = vision_client.annotate_image({"image": image, "features": features})
            
            # Nettoyer le fichier temporaire
            os.unlink(temp_file_path)
            
            # Préparer les résultats pour l'affichage
            results = {
                'labels': [(label.description, round(label.score * 100, 2)) for label in response.label_annotations],
                'faces': len(response.face_annotations),
                'landmarks': [(landmark.description, round(landmark.score * 100, 2)) for landmark in response.landmark_annotations],
                'texts': response.text_annotations[0].description if response.text_annotations else "",
                'safe_search': {
                    'adult': response.safe_search_annotation.adult.name,
                    'spoof': response.safe_search_annotation.spoof.name,
                    'medical': response.safe_search_annotation.medical.name,
                    'violence': response.safe_search_annotation.violence.name,
                    'racy': response.safe_search_annotation.racy.name
                },
                'image_url': image_url
            }
            
            return render_template('result.html', results=results)
            
        except Exception as e:
            flash(f"Une erreur s'est produite: {str(e)}")
            return redirect(url_for('index'))
    
    flash('Type de fichier non autorisé')
    return redirect(url_for('index'))

# Route API pour des analyses simples (démonstration)
@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
        
    if file and allowed_file(file.filename):
        # Logique similaire à la route d'analyse principale
        # Simplifiée pour l'API
        try:
            # Sauvegarder temporairement le fichier
            with tempfile.NamedTemporaryFile(delete=False) as temp:
                file.save(temp.name)
                temp_file_path = temp.name
            
            # Analyser l'image directement (sans GCS)
            vision_client = vision.ImageAnnotatorClient()
            
            with open(temp_file_path, 'rb') as image_file:
                content = image_file.read()
            
            image = vision.Image(content=content)
            response = vision_client.label_detection(image=image)
            
            # Nettoyer le fichier temporaire
            os.unlink(temp_file_path)
            
            # Retourner les résultats en JSON
            return jsonify({
                'labels': [(label.description, round(label.score * 100, 2)) 
                          for label in response.label_annotations]
            })
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    # Utiliser le port défini par l'environnement pour Cloud Run
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)