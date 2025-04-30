from flask import Flask, render_template, request, jsonify
from google.cloud import dialogflow
import os
from dotenv import load_dotenv
import json

# Chargement des variables d'environnement
load_dotenv()

app = Flask(__name__)

# Configuration de Dialogflow
PROJECT_ID = os.getenv('DIALOGFLOW_PROJECT_ID')
CREDENTIALS_PATH = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
LANGUAGE_CODE = 'fr'

def check_configuration():
    """Vérifie la configuration de l'application."""
    errors = []
    
    if not PROJECT_ID:
        errors.append("DIALOGFLOW_PROJECT_ID n'est pas défini dans le fichier .env")
    
    if not CREDENTIALS_PATH:
        errors.append("GOOGLE_APPLICATION_CREDENTIALS n'est pas défini dans le fichier .env")
    elif not os.path.exists(CREDENTIALS_PATH):
        errors.append(f"Le fichier de credentials n'existe pas à l'emplacement : {CREDENTIALS_PATH}")
    else:
        try:
            with open(CREDENTIALS_PATH, 'r') as f:
                json.load(f)
        except json.JSONDecodeError:
            errors.append("Le fichier de credentials n'est pas un JSON valide")
        except Exception as e:
            errors.append(f"Erreur lors de la lecture du fichier de credentials : {str(e)}")
    
    return errors

def detect_intent_texts(text):
    """Envoie un texte à Dialogflow et récupère la réponse."""
    try:
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(PROJECT_ID, "unique-session-id")
        
        text_input = dialogflow.TextInput(text=text, language_code=LANGUAGE_CODE)
        query_input = dialogflow.QueryInput(text=text_input)
        
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
        
        return response.query_result.fulfillment_text
    except Exception as e:
        raise Exception(f"Erreur Dialogflow : {str(e)}")

@app.route('/')
def home():
    errors = check_configuration()
    if errors:
        return render_template('index.html', errors=errors)
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'response': 'Veuillez entrer un message.'})
    
    try:
        response = detect_intent_texts(user_message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'response': f'Une erreur est survenue: {str(e)}'})

if __name__ == '__main__':
    errors = check_configuration()
    if errors:
        print("\nErreurs de configuration :")
        for error in errors:
            print(f"- {error}")
    app.run(debug=True) 