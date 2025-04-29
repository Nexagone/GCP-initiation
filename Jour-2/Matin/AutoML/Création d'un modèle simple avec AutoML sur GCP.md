# Atelier: création d'un modèle simple avec AutoML sur GCP (sans code)

## Introduction (5 minutes)

L'AutoML (Automated Machine Learning) permet de créer des modèles d'IA sans compétences en programmation. Google Cloud Platform (GCP) propose plusieurs solutions "sans code" qui démocratisent l'accès à l'intelligence artificielle. En 1 heure, nous allons créer un modèle de prédiction simple mais fonctionnel.

## Prérequis
- Un compte Google Cloud Platform (avec crédits ou facturation activée)
- Un navigateur web

## Objectifs
- Découvrir les solutions AutoML de Google Cloud
- Créer un modèle prédictif sans écrire de code
- Comprendre les bases de l'évaluation d'un modèle

## Partie 1 : Solutions AutoML de Google Cloud (10 minutes)

### Les différentes solutions disponibles

Google Cloud propose plusieurs produits AutoML pour différents types de données :

1. **AutoML Tables** : Pour les données tabulaires (feuilles de calcul)
2. **AutoML Vision** : Pour la classification d'images et la détection d'objets
3. **AutoML Natural Language** : Pour l'analyse de texte
4. **AutoML Translation** : Pour la traduction personnalisée
5. **AutoML Video** : Pour l'analyse vidéo

Pour cet atelier express, nous nous concentrerons sur **AutoML Tables** car il est le plus accessible pour les débutants.

### Avantages de l'approche sans code
- Aucune compétence en programmation requise
- Interface intuitive et guidée
- Création de modèles en quelques clics
- Performances souvent comparables aux solutions codées manuellement

## Partie 2 : Configuration et accès (5 minutes)

1. Connectez-vous à [Google Cloud Console](https://console.cloud.google.com/)
2. Créez un nouveau projet ou sélectionnez un projet existant
3. Activez l'API Vertex AI si ce n'est pas déjà fait :
   - Recherchez "Vertex AI" dans la barre de recherche
   - Cliquez sur "Activer"
4. Accédez à Vertex AI dans le menu de navigation

## Partie 3 : Préparation des données (10 minutes)

Pour gagner du temps, nous utiliserons un jeu de données préparé à l'avance.

1. Téléchargez le jeu de données "Bank Marketing" depuis [ce lien (UCI ML Repository)](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)
   - Ce jeu de données contient des informations sur les clients d'une banque
   - L'objectif est de prédire si un client souscrira à un dépôt à terme (oui/non)

2. Explorez rapidement les données :
   - **age** : âge du client
   - **job** : type d'emploi
   - **marital** : statut marital
   - **education** : niveau d'éducation
   - **balance** : solde moyen annuel
   - **housing** : a un prêt immobilier (oui/non)
   - **loan** : a un prêt personnel (oui/non)
   - **deposit** (cible) : a souscrit un dépôt à terme (oui/non)

## Partie 4 : Création du jeu de données dans AutoML Tables (10 minutes)

1. Dans Vertex AI, cliquez sur "Datasets" puis "Créer un dataset"
2. Configurez votre dataset :
   - Donnez un nom (ex: "bank_marketing_express")
   - Sélectionnez le type "Tabular"
   - Choisissez l'objectif "Classification binaire"
3. Importez les données :
   - Sélectionnez "Upload files from your computer"
   - Téléchargez le fichier CSV préparé
   - Cliquez sur "Continuer"
4. Vérifiez la configuration automatique :
   - Confirmez que les types de données sont correctement détectés
   - Définissez la colonne "deposit" comme cible
   - Cliquez sur "Créer"

## Partie 5 : Entraînement du modèle (10 minutes)

1. Une fois le jeu de données créé, cliquez sur "Train new model"
2. Dans les paramètres d'entraînement :
   - Confirmez la colonne cible ("deposit")
   - Gardez les caractéristiques recommandées
   - Pour gagner du temps, réglez le budget d'entraînement sur 1 heure maximum
   - Sélectionnez l'optimisation pour la précision
3. Cliquez sur "Démarrer l'entraînement"

> Remarque : L'entraînement peut prendre jusqu'à 1 heure. Pour les besoins de cet atelier express, nous pouvons :
> - Soit utiliser un modèle pré-entraîné fourni par l'instructeur
> - Soit continuer l'atelier pendant que le modèle s'entraîne en arrière-plan

## Partie 6 : Comprendre les évaluations (10 minutes)

Pendant que le modèle s'entraîne, familiarisons-nous avec les métriques d'évaluation :

### Pour les problèmes de classification binaire :

1. **Précision** : Proportion des prédictions positives qui sont correctes
   - Formule : Vrais Positifs / (Vrais Positifs + Faux Positifs)
   - Utilisez cette métrique quand les faux positifs sont coûteux

2. **Rappel** : Proportion des cas réellement positifs qui sont correctement identifiés
   - Formule : Vrais Positifs / (Vrais Positifs + Faux Négatifs)
   - Utilisez cette métrique quand les faux négatifs sont coûteux

3. **Score F1** : Moyenne harmonique de la précision et du rappel
   - Bon compromis entre précision et rappel

4. **AUC** : Area Under the ROC Curve
   - Mesure la capacité du modèle à distinguer les classes
   - Une valeur de 0.5 équivaut à une prédiction aléatoire
   - Une valeur de 1.0 est une prédiction parfaite

### Interprétation des résultats

- Un bon modèle pour la prédiction de dépôts bancaires devrait avoir :
  - AUC > 0.75
  - Précision et rappel > 0.7
  - Score F1 > 0.7

## Partie 7 : Analyse des résultats du modèle (5 minutes)

Une fois l'entraînement terminé (ou en utilisant un modèle pré-entraîné) :

1. Examinez le tableau de bord d'évaluation :
   - Les métriques globales (AUC, précision, rappel)
   - La matrice de confusion
   - L'importance des caractéristiques

2. Analysez l'importance des caractéristiques :
   - Quelles variables ont le plus d'influence sur la décision d'un client de souscrire un dépôt ?
   - Y a-t-il des surprises dans ces résultats ?

3. Explorez la matrice de confusion :
   - Combien de clients susceptibles de souscrire n'ont pas été identifiés (faux négatifs) ?
   - Combien de clients ont été ciblés à tort (faux positifs) ?

## Partie 8 : Test et utilisation du modèle (5 minutes)

1. Accédez à l'onglet "Test & Use" de votre modèle
2. Testez des prédictions individuelles :
   - Créez un profil client fictif (âge, profession, statut marital, etc.)
   - Voyez si le modèle prédit qu'il souscrira un dépôt ou non
   - Notez la probabilité associée à la prédiction

3. Discutez des cas d'utilisation pratiques :
   - Ciblage marketing personnalisé
   - Optimisation des campagnes promotionnelles
   - Priorisation des prospects

## Conclusion et prochaines étapes (5 minutes)

### Ce que nous avons accompli :
- Découvert les solutions AutoML de Google Cloud
- Créé un jeu de données et un modèle prédictif sans code
- Appris à interpréter les métriques d'évaluation
- Testé le modèle avec des données fictives

### Prochaines étapes possibles :
1. **Déploiement du modèle** :
   - Création d'un endpoint pour les prédictions en temps réel
   - Intégration à des applications existantes

2. **Amélioration du modèle** :
   - Ajout de nouvelles caractéristiques
   - Nettoyage approfondi des données
   - Augmentation du budget d'entraînement

3. **Explorer d'autres solutions AutoML** :
   - AutoML Vision pour la reconnaissance d'images
   - AutoML Natural Language pour l'analyse de sentiment

## Ressources pour continuer l'apprentissage

- [Documentation Google Cloud AutoML Tables](https://cloud.google.com/vertex-ai/docs/tabular-data/classification-regression/overview)
- [Tutoriels Google Cloud](https://cloud.google.com/vertex-ai/docs/tutorials)
- [Codelabs Google Cloud](https://codelabs.developers.google.com/?cat=cloudai)

