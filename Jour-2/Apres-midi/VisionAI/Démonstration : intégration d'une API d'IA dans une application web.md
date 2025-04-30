# Guide d'Installation et Configuration Locale

Ce guide vous aidera à configurer l'application Vision AI pour qu'elle fonctionne localement avec vos credentials GCP.

## Prérequis

- Python 3.7 ou supérieur
- Compte Google Cloud Platform (GCP)
- Accès à la console GCP

## 1. Configuration du Projet GCP

### 1.1 Création du Projet
1. Accédez à la [console GCP](https://console.cloud.google.com/)
2. Cliquez sur "Créer un projet" ou sélectionnez un projet existant
3. Notez l'ID du projet

### 1.2 Activation des APIs
1. Dans la console GCP, allez dans "APIs et services" > "Bibliothèque"
2. Activez les APIs suivantes :
   - Cloud Vision API
   - Cloud Storage API

### 1.3 Création d'un Compte de Service
1. Dans la console GCP, allez dans "IAM et administration" > "Comptes de service"
2. Cliquez sur "Créer un compte de service"
3. Remplissez les informations :
   - Nom du compte : "vision-app-service"
   - ID du compte : sera généré automatiquement
   - Description : "Compte de service pour l'application Vision AI"
4. Cliquez sur "Créer et continuer"

### 1.4 Attribution des Rôles
1. Dans la section "Accorder à ce compte de service l'accès au projet", ajoutez les rôles suivants :
   - `Storage Object Viewer`
   - `Storage Object Creator`
   - `Cloud Vision API User`
2. Cliquez sur "Continuer"
3. Cliquez sur "Terminer"

### 1.5 Création des Clés d'API
1. Dans la liste des comptes de service, trouvez celui que vous venez de créer
2. Cliquez sur son nom
3. Allez dans l'onglet "Clés"
4. Cliquez sur "Ajouter une clé" > "Créer une nouvelle clé"
5. Choisissez le format "JSON"
6. Cliquez sur "Créer"
7. Un fichier JSON sera automatiquement téléchargé sur votre ordinateur

### 1.6 Création du Bucket Cloud Storage
1. Dans la console GCP, allez dans "Cloud Storage" > "Buckets"
2. Cliquez sur "Créer un bucket"
3. Donnez un nom unique à votre bucket
4. Choisissez la région la plus proche de vous
5. Cliquez sur "Créer"

## 2. Configuration de l'Application

### 2.1 Installation des Dépendances
```bash
pip install flask google-cloud-vision google-cloud-storage python-dotenv
```

### 2.2 Configuration des Credentials
1. Placez votre fichier `credentials.json` dans le dossier de l'application
2. Vérifiez que le chemin est correct dans `app.py` :
   ```python
   CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), 'credentials.json')
   ```

### 2.3 Configuration du Bucket
1. Modifiez la variable `BUCKET_NAME` dans `app.py` avec le nom de votre bucket :
   ```python
   BUCKET_NAME = 'votre-nom-de-bucket'
   ```

### 2.4 Configuration de la Clé Secrète
1. Créez un fichier `.env` à la racine du projet
2. Ajoutez la ligne suivante :
   ```
   SECRET_KEY=votre-clé-secrète-complexe
   ```
3. Pour générer une clé secrète sécurisée :
   ```python
   import secrets
   print(secrets.token_hex(32))
   ```

## 3. Sécurité

### 3.1 Fichier .gitignore
Assurez-vous que votre `.gitignore` contient :
```
# Fichiers de credentials et secrets
credentials.json
*.json
.env

# Environnement virtuel Python
venv/
env/
.env/
.venv/

# Fichiers de cache Python
__pycache__/
*.py[cod]
*$py.class
```

### 3.2 Permissions des Fichiers
```bash
chmod 600 credentials.json
chmod 600 .env
```

## 4. Lancement de l'Application

1. Activez votre environnement virtuel (si vous en utilisez un)
2. Lancez l'application :
   ```bash
   python app.py
   ```
3. L'application sera accessible sur `http://localhost:8080`

## 5. Vérification

Pour vérifier que tout fonctionne correctement :
1. L'application devrait démarrer sans erreur
2. Vous devriez pouvoir uploader une image
3. L'image devrait apparaître dans votre bucket GCP
4. Les résultats de l'analyse Vision AI devraient s'afficher

## 6. Dépannage

Si vous rencontrez des erreurs, vérifiez :
- Le chemin vers votre fichier de credentials
- Les permissions de votre compte de service
- Le nom de votre bucket
- Que les APIs sont bien activées
- Les logs de l'application pour plus de détails

## 7. Personnalisation

### 7.1 Logo et En-tête
1. Placez votre logo dans `static/images/logo.png`
2. Modifiez le fichier `layout.html` pour personnaliser :
   - Les couleurs
   - La taille du logo
   - Le nom de l'entreprise

### 7.2 Durée de Validité des URLs
Pour modifier la durée de validité des URLs signées (par défaut 1 heure) :
```python
expiration = datetime.now() + timedelta(hours=1)  # Modifiez la valeur selon vos besoins
``` 