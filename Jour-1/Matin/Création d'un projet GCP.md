# Création d'un projet GCP : Récapitulatif pratique

## 1. Accès à la console GCP
- Rendez-vous sur console.cloud.google.com
- Connectez-vous avec votre compte Google

## 2. Création du projet
- Dans la barre supérieure, cliquez sur le sélecteur de projet
- Cliquez sur "Nouveau projet"
- Donnez un nom à votre projet (ce nom sera visible par les utilisateurs)
- Optionnel : modifiez l'ID du projet (identifiant unique)
- Sélectionnez l'organisation parente si applicable
- Cliquez sur "Créer"

## 3. Configuration initiale du projet

### Configuration de la facturation
- Accédez à "Facturation" dans le menu de navigation
- Associez un compte de facturation existant ou créez-en un nouveau
- Cette étape est obligatoire pour utiliser la plupart des services GCP

### Configuration des IAM (Identity and Access Management)
- Accédez à "IAM et administration"
- Ajoutez des utilisateurs et attribuez-leur des rôles appropriés
- Les rôles courants incluent : Propriétaire, Éditeur, Lecteur, ou des rôles spécifiques à certains services

### Activation des APIs nécessaires
- Accédez à "APIs et services" > "Bibliothèque"
- Recherchez et activez les APIs dont vous avez besoin pour votre projet
  - Exemples: Compute Engine, Cloud Storage, BigQuery, etc.

## 4. Configuration du réseau (optionnel)
- Accédez à "VPC Network" pour configurer votre réseau virtuel
- Créez des sous-réseaux selon vos besoins
- Configurez les règles de pare-feu

## 5. Activation des services spécifiques
En fonction de vos besoins, vous pouvez activer:
- Compute Engine pour les machines virtuelles
- Cloud Storage pour le stockage d'objets
- BigQuery pour l'analyse de données
- Cloud Functions pour les fonctions sans serveur
- Et bien d'autres services...
