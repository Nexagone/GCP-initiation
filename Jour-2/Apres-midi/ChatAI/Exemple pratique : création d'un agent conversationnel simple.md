# Application de Chat avec Dialogflow

Cette application permet de créer un agent conversationnel simple en utilisant Google Cloud Dialogflow et Flask.

## Prérequis

- Python 3.7 ou supérieur
- Un compte Google Cloud Platform (GCP)
- Un projet Dialogflow configuré
- Les credentials Google Cloud Platform

## Installation

1. **Cloner le dépôt**
   ```bash
   git clone [URL_DU_REPO]
   cd chat-app
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration de Google Cloud Platform

1. **Créer un projet GCP**
   - Allez sur [console.cloud.google.com](https://console.cloud.google.com/)
   - Créez un nouveau projet ou sélectionnez un projet existant
   - Notez l'ID du projet

2. **Activer les APIs nécessaires**
   - Dans la console GCP, allez dans "APIs et services" > "Bibliothèque"
   - Activez les APIs suivantes :
     - Dialogflow API
     - Cloud Natural Language API

3. **Créer les credentials**
   - Dans "APIs et services" > "Identifiants"
   - Cliquez sur "Créer des identifiants" > "Compte de service"
   - Nommez le compte (ex: "dialogflow-service")
   - Sélectionnez le rôle "Dialogflow API Admin"
   - Créez et téléchargez la clé au format JSON

## Configuration de Dialogflow

1. **Créer un agent**
   - Allez sur [dialogflow.cloud.google.com](https://dialogflow.cloud.google.com/)
   - Créez un nouvel agent
   - Liez-le à votre projet GCP

2. **Configurer les intentions**
   - Créez des intentions (ex: "salutation", "au revoir")
   - Ajoutez des exemples de phrases pour chaque intention
   - Définissez les réponses pour chaque intention

## Configuration de l'application

1. **Créer le fichier .env**
   ```bash
   cp .env.example .env
   ```

2. **Configurer les variables d'environnement**
   ```
   DIALOGFLOW_PROJECT_ID=votre-project-id
   GOOGLE_APPLICATION_CREDENTIALS=chemin/vers/votre/fichier-credentials.json
   ```

## Utilisation

1. **Démarrer l'application**
   ```bash
   python app.py
   ```

2. **Accéder à l'interface**
   - Ouvrez votre navigateur à l'adresse : `http://localhost:5000`
   - L'interface de chat s'affiche

3. **Tester la conversation**
   - Tapez un message dans le champ de saisie
   - Appuyez sur Entrée ou cliquez sur "Envoyer"
   - L'agent Dialogflow répondra en fonction de la configuration

## Structure du projet

```
chat-app/
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── .env                  # Variables d'environnement
├── static/               # Fichiers statiques
│   ├── css/             # Styles CSS
│   ├── js/              # Scripts JavaScript
│   └── images/          # Images
└── templates/            # Templates HTML
    ├── layout.html      # Template de base
    └── index.html       # Page principale
```

## Déploiement

1. **Construire l'image Docker**
   ```bash
   docker build -t chat-app .
   ```

2. **Lancer le conteneur**
   ```bash
   docker run -p 5000:5000 chat-app
   ```

## Dépannage

- **Erreur de credentials** : Vérifiez le chemin du fichier JSON dans `.env`
- **Erreur de projet** : Vérifiez l'ID du projet dans `.env`
- **Pas de réponse** : Vérifiez la configuration des intentions dans Dialogflow
- **Erreur de connexion** : Vérifiez que les APIs sont bien activées dans GCP

## Notes importantes

- L'agent est configuré pour utiliser le français comme langue par défaut
- Les réponses dépendent de la configuration de votre agent Dialogflow
- Assurez-vous que votre agent Dialogflow est bien entraîné
- Gardez vos credentials en sécurité et ne les partagez pas

## Ressources utiles

- [Documentation Dialogflow](https://cloud.google.com/dialogflow/docs)
- [Documentation Google Cloud](https://cloud.google.com/docs)
- [Documentation Flask](https://flask.palletsprojects.com/) 