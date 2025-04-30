# Guide d'utilisation : Application d'analyse d'images avec Google Vision API

Ce guide vous explique comment configurer, installer et utiliser l'application d'analyse d'images en local sur votre machine.

## Prérequis

- [Python](https://www.python.org/downloads/) 3.8 ou supérieur
- [Pip](https://pip.pypa.io/en/stable/installation/) (gestionnaire de paquets Python)
- Compte Google Cloud Platform (GCP) avec facturation activée
- [gcloud CLI](https://cloud.google.com/sdk/docs/install) (facultatif, mais recommandé)

## Configuration initiale GCP

### 1. Créer un projet GCP

1. Accédez à la [console Google Cloud](https://console.cloud.google.com/)
2. Cliquez sur le menu déroulant en haut et sélectionnez "Nouveau projet"
3. Nommez votre projet (ex: "demo-vision-api") et cliquez sur "Créer"
4. Notez l'ID de votre projet, vous en aurez besoin plus tard

### 2. Activer les APIs nécessaires

1. Dans le menu de navigation, accédez à "APIs et Services" > "Bibliothèque"
2. Recherchez et activez les APIs suivantes :
   - "Cloud Vision API"
   - "Cloud Storage API" (si vous prévoyez de déployer sur GCP plus tard)

### 3. Créer un compte de service et une clé

1. Dans le menu de navigation, accédez à "IAM et administration" > "Comptes de service"
2. Cliquez sur "Créer un compte de service"
3. Donnez un nom à votre compte de service (ex: "vision-app-local")
4. Pour les rôles, attribuez :
   - "Vision AI User" (Utilisateur Vision AI)
   - "Storage Admin" (Administrateur Storage), si nécessaire
5. Cliquez sur "Continuer" puis "Terminé"
6. Trouvez le compte de service créé dans la liste, cliquez sur les trois points verticaux puis sur "Gérer les clés"
7. Cliquez sur "Ajouter une clé" > "Créer une clé"
8. Sélectionnez le format JSON et cliquez sur "Créer"
9. La clé sera téléchargée automatiquement. **Conservez-la précieusement** et renommez-la en `key.json`

## Installation de l'application

### 1. Cloner ou télécharger les fichiers du projet

Assurez-vous d'avoir tous les fichiers nécessaires dans un dossier dédié à l'application.

### 2. Créer un environnement virtuel Python

```bash
# Naviguer vers le dossier du projet
cd chemin/vers/votre/projet

# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Windows :
venv\Scripts\activate
# Sur macOS/Linux :
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Placer votre clé d'API dans le dossier du projet

Copiez le fichier `key.json` téléchargé précédemment à la racine du dossier du projet.

### 5. Créer le dossier pour stocker les images téléchargées

```bash
mkdir -p static/uploads
```

## Lancement de l'application

```bash
# Définir la variable d'environnement pour les identifiants GCP
# Sur Windows (Invite de commande)
set GOOGLE_APPLICATION_CREDENTIALS=chemin/absolu/vers/key.json

# Sur Windows (PowerShell)
$env:GOOGLE_APPLICATION_CREDENTIALS="chemin/absolu/vers/key.json"

# Sur macOS/Linux
export GOOGLE_APPLICATION_CREDENTIALS="chemin/absolu/vers/key.json"

# Lancer l'application
python app.py
```

L'application sera accessible à l'adresse : [http://localhost:8080](http://localhost:8080)

## Utilisation de l'application

1. **Accéder à l'application** : Ouvrez votre navigateur et visitez [http://localhost:8080](http://localhost:8080)

2. **Télécharger une image** : Cliquez sur le bouton "Choisir un fichier" pour sélectionner une image de votre ordinateur
   - Formats acceptés : JPG, JPEG, PNG, GIF
   - Taille maximale recommandée : 5 Mo

3. **Analyser l'image** : Cliquez sur le bouton "Analyser l'image"

4. **Explorer les résultats** : Vous verrez les résultats de l'analyse, notamment :
   - Détection d'objets et étiquettes
   - Reconnaissance faciale
   - Points d'intérêt détectés
   - Texte extrait (OCR)
   - Analyse de contenu sensible

5. **Analyser une autre image** : Cliquez sur "Analyser une autre image" pour recommencer

## Fonctionnalités démontrées

Cette application illustre comment intégrer l'API Vision de Google dans une application web pour :

- **Détection d'objets** : Identifie les objets, animaux, paysages et autres éléments présents dans l'image
- **Reconnaissance faciale** : Détecte les visages humains et leur nombre
- **Détection de points d'intérêt** : Reconnaît les monuments et lieux célèbres
- **OCR** : Extrait du texte présent dans l'image
- **Détection de contenu sensible** : Évalue si l'image contient du contenu pour adultes, violent ou médical

## Dépannage

### Problèmes d'authentification
- Vérifiez que votre fichier `key.json` est correctement placé
- Assurez-vous que la variable d'environnement `GOOGLE_APPLICATION_CREDENTIALS` pointe vers ce fichier

### L'analyse échoue
- Vérifiez que la Vision API est bien activée dans votre projet GCP
- Assurez-vous que votre compte de service dispose des autorisations nécessaires
- Vérifiez la taille et le format de votre image

### Problèmes de port
Si le port 8080 est déjà utilisé :
1. Modifiez la valeur du port dans `app.py` (cherchez `port = int(os.environ.get('PORT', 8080))`)
2. Ou lancez avec une variable d'environnement : `PORT=8080 python app.py`

