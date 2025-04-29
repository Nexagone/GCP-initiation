# Atelier guidé : création d'un modèle simple avec AutoML (avec code)

## Introduction

L'AutoML (Automated Machine Learning) est une approche qui automatise le processus de développement des modèles de machine learning, permettant même aux débutants de créer des modèles performants sans expertise approfondie en programmation ou en data science. Cet atelier vous guidera à travers les étapes nécessaires pour créer un modèle simple à l'aide d'outils AutoML.

## Objectifs de l'atelier

- Comprendre les principes de base de l'AutoML
- Préparer un jeu de données pour l'apprentissage automatique
- Utiliser une plateforme AutoML pour créer un modèle de prédiction
- Évaluer les performances du modèle
- Déployer et utiliser le modèle créé

## Prérequis

- Un ordinateur avec accès à internet
- Un compte Google (pour Google Colab et Google Cloud AutoML)
- Données à analyser (nous fournirons un exemple)

## Durée estimée : 2-3 heures

## Partie 1 : Comprendre l'AutoML

### Qu'est-ce que l'AutoML ?

L'AutoML automatise plusieurs étapes du machine learning, notamment :
- La préparation et le nettoyage des données
- La sélection des caractéristiques importantes
- Le choix des algorithmes adaptés
- L'optimisation des hyperparamètres
- L'évaluation du modèle

### Avantages de l'AutoML

- **Accessibilité** : Permet aux non-experts de créer des modèles ML
- **Gain de temps** : Automatise les tâches répétitives et chronophages
- **Performance** : Produit souvent des modèles très compétitifs
- **Reproductibilité** : Facilite la création de modèles cohérents

### Plateformes AutoML populaires

- Google Cloud AutoML
- Azure Automated Machine Learning
- Amazon SageMaker Autopilot
- H2O.ai AutoML
- Auto-Sklearn
- TPOT (Tree-based Pipeline Optimization Tool)

Pour cet atelier, nous utiliserons **Google Colab** avec la bibliothèque **AutoML** de H2O.ai, qui est open source et facile à utiliser.

## Partie 2 : Préparation des données

### Étape 1 : Accéder à Google Colab

1. Ouvrez votre navigateur et accédez à [Google Colab](https://colab.research.google.com)
2. Connectez-vous avec votre compte Google
3. Créez un nouveau notebook en cliquant sur "Nouveau notebook"

### Étape 2 : Installation des bibliothèques nécessaires

Exécutez la cellule de code suivante dans votre notebook Colab :

```python
!pip install h2o
```

### Étape 3 : Import des bibliothèques et initialisation

```python
import h2o
from h2o.automl import H2OAutoML
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Initialiser l'instance H2O
h2o.init()
```

### Étape 4 : Téléchargement du jeu de données

Pour cet atelier, nous utiliserons le jeu de données "Iris" qui est classique pour l'apprentissage supervisé.

```python
# Télécharger le jeu de données Iris depuis le dépôt H2O
iris = h2o.import_file("https://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris.csv")

# Afficher les premières lignes du jeu de données
iris.head()
```

### Étape 5 : Explorer et comprendre les données

```python
# Examiner la structure du jeu de données
iris.describe()

# Vérifier les dimensions du jeu de données
print(f"Dimensions: {iris.shape}")

# Vérifier s'il y a des valeurs manquantes
print(f"Valeurs manquantes par colonne: {iris.isna().sum()}")

# Visualiser la distribution des espèces
iris_df = iris.as_data_frame()
iris_df['species'].value_count().plot(kind='bar')
plt.title('Distribution des espèces')
plt.xlabel('Espèce')
plt.ylabel('Nombre d'échantillons')
plt.show()
```

### Étape 6 : Préparation des données pour l'entraînement

```python
# Définir les variables prédictives (X) et la variable cible (y)
X = iris.columns
y = "species"
X.remove(y)

# Diviser les données en ensembles d'entraînement et de test (70% / 30%)
train, test = iris.split_frame(ratios=[0.7], seed=42)

print(f"Taille de l'ensemble d'entraînement: {train.shape}")
print(f"Taille de l'ensemble de test: {test.shape}")
```

## Partie 3 : Création du modèle avec AutoML

### Étape 1 : Configuration de l'AutoML

```python
# Configurer l'instance AutoML
aml = H2OAutoML(
    max_runtime_secs=120,  # Limiter le temps d'exécution à 2 minutes
    max_models=10,         # Limiter à 10 modèles maximum
    seed=42,               # Pour la reproductibilité
    sort_metric="logloss"  # Métrique à optimiser
)
```

### Étape 2 : Entraînement des modèles

```python
# Lancer l'entraînement AutoML
aml.train(x=X, y=y, training_frame=train)
```

### Étape 3 : Examen des modèles générés

```python
# Afficher le leaderboard des modèles
lb = aml.leaderboard
print(lb)

# Obtenir le meilleur modèle
best_model = aml.leader
print(f"Le meilleur modèle est: {best_model}")
```

## Partie 4 : Évaluation du modèle

### Étape 1 : Évaluation sur l'ensemble de test

```python
# Évaluer le modèle sur l'ensemble de test
perf = best_model.model_performance(test)
print(perf)
```

### Étape 2 : Visualisation de la matrice de confusion

```python
# Obtenir la matrice de confusion
cm = best_model.confusion_matrix(test)
print("Matrice de confusion:")
print(cm)

# Visualisation avec matplotlib (conversion nécessaire)
cm_df = cm.as_data_frame()
plt.figure(figsize=(8, 6))
sns.heatmap(cm_df.iloc[:-1, :-1], annot=True, fmt="d", cmap="Blues")
plt.xlabel("Prédit")
plt.ylabel("Réel")
plt.title("Matrice de confusion")
plt.show()
```

### Étape 3 : Analyse des métriques de performance

```python
# Afficher les principales métriques
print(f"Précision: {perf.accuracy()[0][1]}")
print(f"Erreur: {perf.error()[0][1]}")
print(f"Log Loss: {perf.logloss()}")
```

## Partie 5 : Faire des prédictions avec le modèle

### Étape 1 : Prédictions sur l'ensemble de test

```python
# Faire des prédictions
predictions = best_model.predict(test)
predictions.head()
```

### Étape 2 : Créer un exemple pour la prédiction

```python
# Créer un exemple pour tester notre modèle
exemple = h2o.create_frame(
    rows=1,
    cols=4,
    categorical_fraction=0,
    integer_fraction=0,
    binary_fraction=0,
    time_fraction=0,
    real_range=100,
    integer_range=100,
    missing_fraction=0,
)

# Remplir avec des valeurs spécifiques
exemple[0, 0] = 5.1  # sepal_length
exemple[0, 1] = 3.5  # sepal_width
exemple[0, 2] = 1.4  # petal_length
exemple[0, 3] = 0.2  # petal_width

# Renommer les colonnes
exemple.names = X

# Faire une prédiction
prediction = best_model.predict(exemple)
print(f"Pour les caractéristiques {exemple.as_data_frame().iloc[0].to_dict()}, la prédiction est: {prediction['predict'][0]}")
```

## Partie 6 : Sauvegarder et déployer le modèle

### Étape 1 : Sauvegarder le modèle

```python
# Définir le chemin d'accès pour sauvegarder le modèle
model_path = h2o.save_model(model=best_model, path="./", force=True)
print(f"Modèle sauvegardé à: {model_path}")
```

### Étape 2 : Télécharger le modèle (si vous utilisez Colab)

```python
from google.colab import files
files.download(model_path)
```

### Étape 3 : Recharger le modèle (simulation)

```python
# Charger un modèle sauvegardé
loaded_model = h2o.load_model(model_path)
print("Modèle chargé avec succès!")
```

## Partie 7 : Exportation du modèle pour intégration

```python
# Exporter le modèle au format MOJO (Model Object, Optimized)
mojo_path = best_model.download_mojo(path="./", get_genmodel_jar=True)
print(f"MOJO exporté à: {mojo_path}")

# Télécharger le MOJO si vous utilisez Colab
from google.colab import files
files.download(mojo_path)
```

## Partie 8 : Explorer l'interprétabilité du modèle

```python
# Si le modèle est interprétable (comme un GBM ou un RF), examiner l'importance des variables
if hasattr(best_model, 'varimp'):
    varimp = best_model.varimp(use_pandas=True)
    print("Importance des variables:")
    print(varimp)
    
    # Visualiser l'importance des variables
    plt.figure(figsize=(10, 6))
    plt.barh(varimp['variable'][:10], varimp['relative_importance'][:10])
    plt.xlabel('Importance relative')
    plt.title('Top 10 des variables les plus importantes')
    plt.gca().invert_yaxis()  # Pour afficher la plus importante en haut
    plt.show()
```

## Conclusion

Dans cet atelier, vous avez appris à :
- Préparer des données pour un problème d'apprentissage automatique
- Utiliser AutoML pour créer et sélectionner automatiquement le meilleur modèle
- Évaluer les performances d'un modèle de ML
- Faire des prédictions avec le modèle
- Sauvegarder et exporter le modèle pour une utilisation future

## Pour aller plus loin

1. **Essayez avec vos propres données** : Appliquez les mêmes techniques à un jeu de données qui vous intéresse
2. **Explorez d'autres plateformes AutoML** : Google Cloud AutoML, Azure ML, Amazon SageMaker
3. **Ajustez les paramètres AutoML** : Modifiez le temps d'exécution, les métriques d'optimisation, etc.
4. **Apprenez à déployer en production** : Créez une API REST pour votre modèle

## Ressources supplémentaires

- [Documentation H2O AutoML](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html)
- [Google Cloud AutoML](https://cloud.google.com/automl)
- [Microsoft Azure AutoML](https://docs.microsoft.com/en-us/azure/machine-learning/concept-automated-ml)
- [Amazon SageMaker Autopilot](https://aws.amazon.com/sagemaker/autopilot/)

