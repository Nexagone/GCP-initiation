import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime
from sklearn.model_selection import train_test_split

# Initialisation de Faker
fake = Faker('fr_FR')

# Nombre d'échantillons à générer
NB_SAMPLES = 500

# Définition des quartiers (sans caractères spéciaux)
QUARTIERS = ['Nord', 'Sud', 'Est', 'Ouest', 'Centre']

# Fonction pour générer des caractéristiques de la maison
def generate_house_features():
    # Caractéristiques principales (arrondies)
    surface_m2 = round(random.uniform(30, 300) / 10) * 10  # Arrondi à la dizaine
    nb_chambres = max(1, int(surface_m2 / 40))
    nb_salles_bain = max(1, int(nb_chambres * 0.5))
    
    # Âge du bâtiment
    age_batiment = random.randint(0, 50)
    
    # Quartier
    quartier = random.choice(QUARTIERS)
    
    # Calcul du prix de base
    prix_base = surface_m2 * random.uniform(2000, 5000)
    
    # Facteurs de correction selon le quartier
    facteur_quartier = {
        'Centre': 1.3,
        'Nord': 1.1,
        'Sud': 1.0,
        'Est': 0.9,
        'Ouest': 0.9
    }[quartier]
    
    # Calcul du prix final
    prix = prix_base * facteur_quartier
    
    # Ajustement selon l'âge
    prix *= (1 - (age_batiment * 0.01))  # Réduction de 1% par an
    
    # Ajout d'un bruit aléatoire
    prix *= random.uniform(0.95, 1.05)
    
    # Arrondi du prix à la centaine
    prix = round(prix / 100) * 100
    
    return {
        'surface_m2': surface_m2,
        'nb_chambres': nb_chambres,
        'nb_salles_bain': nb_salles_bain,
        'age_batiment': age_batiment,
        'quartier': quartier,
        'prix': prix
    }

# Génération des données
data = []

# Garantir au moins un échantillon pour chaque quartier
for quartier in QUARTIERS:
    house = generate_house_features()
    house['quartier'] = quartier
    data.append(house)

# Générer le reste des échantillons
for _ in range(NB_SAMPLES - len(data)):
    house = generate_house_features()
    data.append(house)

# Création du DataFrame
df = pd.DataFrame(data)

# Séparation en ensembles d'entraînement et de test
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df[['quartier']])

# Vérification de la distribution des quartiers
print("\nDistribution des quartiers dans l'ensemble d'entraînement :")
print(train_df['quartier'].value_counts())

print("\nDistribution des quartiers dans l'ensemble de test :")
print(test_df['quartier'].value_counts())

# Sauvegarde des ensembles en UTF-8
train_file = 'house_data_train.csv'
test_file = 'house_data_test.csv'

train_df.to_csv(train_file, index=False, encoding='utf-8')
test_df.to_csv(test_file, index=False, encoding='utf-8')

print(f"\nDonnées générées avec succès dans les fichiers :")
print(f"- Ensemble d'entraînement : {train_file} ({len(train_df)} échantillons)")
print(f"- Ensemble de test : {test_file} ({len(test_df)} échantillons)")

print("\nAperçu des données d'entraînement :")
print(train_df.head())
print("\nAperçu des données de test :")
print(test_df.head()) 