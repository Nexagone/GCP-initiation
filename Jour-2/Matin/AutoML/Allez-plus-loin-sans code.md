# Atelier guidé : création d'un modèle simple avec AutoML sur GCP (sans code)

## Introduction

L'AutoML (Automated Machine Learning) est une approche qui démocratise l'accès à l'intelligence artificielle en automatisant le processus de développement des modèles de machine learning. Google Cloud Platform (GCP) propose plusieurs solutions sans code qui permettent même aux personnes sans expertise technique de créer des modèles performants. Cet atelier vous guidera à travers les étapes nécessaires pour créer un modèle simple à l'aide des outils AutoML de Google.

## Objectifs de l'atelier

- Comprendre les solutions d'IA sans code disponibles sur GCP
- Apprendre à utiliser Google Cloud AutoML Vision, Tables, ou Natural Language
- Préparer et importer des données dans l'environnement AutoML
- Configurer et entraîner un modèle sans écrire de code
- Évaluer les performances du modèle
- Déployer et utiliser le modèle créé

## Prérequis

- Un ordinateur avec accès à internet
- Un compte Google Cloud Platform (avec crédits ou facturation activée)
- Des données à analyser (nous expliquerons comment obtenir des exemples)

## Durée estimée : 2-3 heures

## Partie 1 : Introduction aux solutions d'IA sans code sur GCP

### Qu'est-ce que l'AutoML de Google ?

Google Cloud AutoML est une suite de produits qui permet de créer des modèles d'IA personnalisés sans avoir besoin de compétences approfondies en ML ou en programmation. Les principales solutions comprennent :

1. **AutoML Vision** : Pour la classification d'images et la détection d'objets
2. **AutoML Natural Language** : Pour l'analyse de sentiment, la classification de texte et l'extraction d'entités
3. **AutoML Translation** : Pour la traduction personnalisée
4. **AutoML Tables** : Pour l'analyse prédictive sur des données structurées (comme des feuilles de calcul)
5. **AutoML Video Intelligence** : Pour la classification et le suivi d'objets dans les vidéos

### Avantages des solutions sans code

- **Accessibilité** : Pas besoin de compétences en programmation
- **Rapidité** : Création de modèles en quelques heures au lieu de semaines
- **Performance** : Qualité comparable aux modèles créés par des experts
- **Interface utilisateur intuitive** : Processus guidé par des interfaces graphiques
- **Intégration facile** : API REST pour l'intégration dans vos applications

### Quand utiliser les solutions AutoML de Google ?

- Lorsque vous avez peu ou pas d'expertise en ML
- Pour des prototypes rapides
- Pour des projets avec des contraintes de temps et de ressources
- Lorsque vous avez besoin d'une solution personnalisée mais simple à mettre en œuvre

Pour cet atelier, nous nous concentrerons sur **AutoML Tables**, qui permet de créer des modèles de prédiction à partir de données tabulaires (similaires à des feuilles de calcul).

## Partie 2 : Préparation de l'environnement et des données

### Étape 1 : Configurer votre compte Google Cloud Platform

1. Accédez à [Google Cloud Console](https://console.cloud.google.com/)
2. Créez un nouveau projet ou sélectionnez un projet existant
3. Activez la facturation pour votre projet (nécessaire pour utiliser AutoML)
4. Activez les API AutoML en recherchant "AutoML" dans la barre de recherche de la console

### Étape 2 : Accéder à AutoML Tables

1. Dans la console Google Cloud, naviguez vers "Vertex AI" dans le menu de navigation
2. Sélectionnez "Datasets" dans le menu latéral
3. Cliquez sur "Créer un dataset"
4. Sélectionnez "Tables (Tabular)" comme type de données

### Étape 3 : Préparer les données pour AutoML Tables

Pour cet atelier, nous utiliserons un jeu de données sur les informations des clients d'une banque pour prédire si un client s'abonnera à un dépôt à terme.

Options pour obtenir les données :
- Télécharger un exemple de jeu de données bancaires depuis [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)
- Utiliser un jeu de données d'exemple fourni par Google
- Préparer votre propre jeu de données CSV ou Excel

Exigences pour le format des données :
- Format CSV, Excel ou BigQuery
- Une ligne d'en-tête contenant les noms des colonnes
- Données nettoyées (sans valeurs manquantes si possible)
- Au moins quelques centaines de lignes pour de meilleurs résultats

## Partie 3 : Création du jeu de données dans AutoML Tables

### Étape 1 : Importer les données

1. Dans l'écran de création de dataset, donnez un nom à votre dataset (ex: "bank_marketing")
2. Sélectionnez la source de vos données :
   - Importer un fichier CSV depuis votre ordinateur
   - Sélectionner un fichier depuis Google Cloud Storage
   - Importer depuis BigQuery
3. Suivez les instructions à l'écran pour télécharger ou sélectionner votre fichier
4. Cliquez sur "Continuer"

### Étape 2 : Configurer les paramètres du jeu de données

1. Vérifiez que toutes les colonnes ont été correctement importées
2. Examinez les types de données automatiquement détectés (numériques, catégorielles, textuelles, etc.)
3. Corrigez les types de données si nécessaire en cliquant sur le type de données à côté du nom de la colonne
4. Identifiez la colonne cible (celle que vous souhaitez prédire, ex: "deposit" pour "oui/non" si le client a souscrit un dépôt)
5. Cliquez sur "Créer" pour finaliser la création du jeu de données

### Étape 3 : Explorer et comprendre les données

1. Une fois le jeu de données créé, explorez les statistiques automatiquement générées :
   - Distribution des valeurs pour chaque colonne
   - Corrélations entre les colonnes
   - Valeurs manquantes et valeurs aberrantes
2. Prenez note des insights intéressants qui pourraient influencer votre modèle

## Partie 4 : Entraînement du modèle avec AutoML Tables

### Étape 1 : Configurer l'entraînement du modèle

1. À partir de la page de votre jeu de données, cliquez sur "Entraîner un nouveau modèle"
2. Sélectionnez la colonne cible (la variable que vous souhaitez prédire)
3. Choisissez le type de modèle en fonction de votre colonne cible :
   - Classification (pour prédire des catégories, comme "oui/non")
   - Régression (pour prédire des valeurs numériques continues)
4. Configurez les paramètres d'entraînement :
   - Budget d'entraînement (temps alloué à l'entraînement, plus c'est long, meilleur sera le modèle)
   - Optimisation (précision, équilibre précision/latence, latence minimale)

### Étape 2 : Sélectionner les colonnes à utiliser

1. Par défaut, toutes les colonnes sont utilisées pour l'entraînement
2. Désélectionnez les colonnes que vous ne souhaitez pas utiliser (comme les identifiants uniques ou les informations non pertinentes)
3. Vous pouvez également configurer le poids de certaines colonnes si vous estimez qu'elles sont plus importantes

### Étape 3 : Configurer la division des données

1. AutoML divisera automatiquement vos données en ensembles d'entraînement et de test
2. Par défaut, la division est de 80% pour l'entraînement et 20% pour le test
3. Vous pouvez ajuster ces pourcentages selon vos besoins

### Étape 4 : Lancer l'entraînement

1. Vérifiez toutes vos configurations
2. Cliquez sur "Démarrer l'entraînement"
3. L'entraînement peut prendre de quelques minutes à plusieurs heures selon la taille de vos données et le budget d'entraînement choisi

## Partie 5 : Évaluation du modèle

### Étape 1 : Comprendre les métriques d'évaluation

Une fois l'entraînement terminé, AutoML Tables fournit plusieurs métriques pour évaluer la performance de votre modèle :

Pour les modèles de classification :
- **AUC (Area Under the Curve)** : Mesure la capacité du modèle à distinguer les classes, plus c'est proche de 1, mieux c'est
- **Précision** : Proportion des prédictions positives correctes
- **Rappel** : Proportion des cas réellement positifs qui ont été correctement identifiés
- **Score F1** : Moyenne harmonique de la précision et du rappel

Pour les modèles de régression :
- **RMSE (Root Mean Square Error)** : Écart moyen entre les prédictions et les valeurs réelles
- **MAE (Mean Absolute Error)** : Moyenne des erreurs absolues
- **R² (Coefficient de détermination)** : Mesure la qualité de l'ajustement du modèle

### Étape 2 : Analyser la matrice de confusion (pour la classification)

1. La matrice de confusion montre combien d'exemples de chaque classe réelle ont été prédits dans chaque classe
2. Elle permet d'identifier les types d'erreurs que fait votre modèle
3. Analysez les faux positifs et faux négatifs pour comprendre où le modèle se trompe

### Étape 3 : Explorer l'importance des caractéristiques

1. AutoML Tables fournit un graphique d'importance des caractéristiques
2. Il indique quelles colonnes ont le plus influencé les prédictions du modèle
3. Utilisez ces informations pour mieux comprendre vos données et potentiellement améliorer votre modèle

### Étape 4 : Tester le modèle avec de nouvelles données

1. Dans la page du modèle, accédez à l'onglet "Test et utilisation"
2. Vous pouvez entrer manuellement des valeurs pour chaque caractéristique
3. Cliquez sur "Prédire" pour voir ce que le modèle prédit pour ces nouvelles données
4. Testez différentes combinaisons pour mieux comprendre le comportement du modèle

## Partie 6 : Déploiement et utilisation du modèle

### Étape 1 : Déployer le modèle

1. Dans la page du modèle, cliquez sur "Déployer et tester"
2. Sélectionnez "Déployer sur un endpoint"
3. Configurez les paramètres de déploiement :
   - Nom de l'endpoint
   - Région
   - Type de machine (selon vos besoins de performances et de coût)
4. Cliquez sur "Déployer" et attendez que le modèle soit mis en ligne

### Étape 2 : Utiliser le modèle déployé

Une fois déployé, vous pouvez utiliser votre modèle de plusieurs façons :

1. **Via l'interface web** :
   - Accédez à l'endpoint de votre modèle
   - Entrez manuellement les valeurs des caractéristiques
   - Obtenez des prédictions en temps réel

2. **Via l'API REST** :
   - Google Cloud génère automatiquement une API pour votre modèle
   - Vous pouvez l'intégrer dans vos applications web, mobiles ou de bureau
   - Documentation et exemples d'utilisation sont fournis dans la console

3. **Via Google Sheets** (pour certains cas) :
   - Vous pouvez connecter certains modèles à Google Sheets
   - Cela vous permet de faire des prédictions en masse sur vos données tabulaires

### Étape 3 : Surveiller les performances du modèle

1. Dans la console Google Cloud, vous pouvez surveiller l'utilisation de votre modèle
2. Métriques disponibles :
   - Nombre de prédictions
   - Temps de réponse
   - Erreurs éventuelles

## Partie 7 : Bonnes pratiques et conseils

### Améliorer la qualité des données

- Assurez-vous d'avoir suffisamment de données (idéalement des milliers de lignes)
- Équilibrez vos classes pour les problèmes de classification
- Nettoyez les valeurs aberrantes et incohérentes
- Gérez les valeurs manquantes avant d'importer les données

### Optimiser les performances du modèle

- Augmentez le budget d'entraînement pour des modèles plus précis
- Sélectionnez soigneusement les caractéristiques pertinentes
- Examinez les caractéristiques importantes et affinez votre jeu de données
- Testez différentes configurations d'optimisation

### Réduire les coûts

- Commencez avec un petit budget d'entraînement, augmentez si nécessaire
- Supprimez les modèles et endpoints inutilisés
- Utilisez des nœuds de prédiction de plus petite taille si le volume de requêtes est faible
- Considérez les prédictions par lots pour les grands volumes de données

## Partie 8 : Exemples de cas d'utilisation

### Services financiers

- Prédiction des risques de défaut de paiement
- Détection de fraudes
- Segmentation de clientèle
- Prédiction d'attrition des clients

### Commerce de détail

- Prévision des ventes
- Recommandations de produits
- Optimisation des stocks
- Analyse du panier d'achat

### Santé

- Prédiction de réadmissions hospitalières
- Analyse de risques pour les patients
- Optimisation des ressources médicales
- Prédiction des besoins en médicaments

## Conclusion

Dans cet atelier, vous avez appris à :
- Utiliser les solutions AutoML sans code de Google Cloud Platform
- Préparer et importer des données dans AutoML Tables
- Configurer et entraîner un modèle de machine learning sans écrire une seule ligne de code
- Évaluer les performances de votre modèle
- Déployer et utiliser votre modèle pour faire des prédictions

Cette approche sans code démocratise l'accès à l'IA et permet à chacun, quelle que soit son expertise technique, de tirer parti de la puissance du machine learning pour résoudre des problèmes métier concrets.

## Pour aller plus loin

1. **Explorez d'autres solutions AutoML de Google** : Vision, Natural Language, Translation
2. **Intégrez votre modèle dans une application** : Web, mobile ou tableur
3. **Apprenez à améliorer la qualité de vos données** : Techniques de nettoyage et de préparation
4. **Découvrez Google BigQuery ML** : Pour des analyses prédictives directement dans votre entrepôt de données

## Ressources supplémentaires

- [Documentation officielle de Google Cloud AutoML](https://cloud.google.com/automl/docs)
- [Tutoriels Google Cloud AutoML Tables](https://cloud.google.com/automl-tables/docs/tutorials)
- [Centre d'apprentissage Google Cloud](https://cloud.google.com/training)
- [Communauté Google Cloud](https://cloud.google.com/community)

