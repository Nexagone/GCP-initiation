import csv
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialisation de Faker
fake = Faker('fr_FR')

# Nombre d'utilisateurs à générer
NB_USERS = 1000

# Fonction pour générer une date de naissance aléatoire
def generate_birth_date():
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2005, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date)

# Fonction pour générer un numéro de téléphone français
def generate_phone_number():
    return f"0{random.randint(6,7)}{fake.random_number(digits=8)}"

# Fonction pour générer un statut marital
def generate_marital_status():
    status = ['Célibataire', 'Marié(e)', 'Divorcé(e)', 'Veuf(ve)', 'Pacsé(e)']
    return random.choice(status)

# Fonction pour générer un niveau d'éducation
def generate_education_level():
    levels = [
        'Baccalauréat',
        'BTS/DUT',
        'Licence',
        'Master',
        'Doctorat',
        'Autre'
    ]
    return random.choice(levels)

# Création des données
users_data = []
for _ in range(NB_USERS):
    user = {
        'id': fake.uuid4(),
        'prenom': fake.first_name(),
        'nom': fake.last_name(),
        'email': fake.email(),
        'date_naissance': generate_birth_date(),
        'telephone': generate_phone_number(),
        'adresse': fake.street_address(),
        'code_postal': fake.postcode(),
        'ville': fake.city(),
        'pays': 'France',
        'profession': fake.job(),
        'entreprise': fake.company(),
        'salaire_annuel': random.randint(25000, 120000),
        'statut_marital': generate_marital_status(),
        'nombre_enfants': random.randint(0, 4),
        'niveau_etudes': generate_education_level(),
        'date_inscription': fake.date_between(start_date='-5y', end_date='today'),
        'derniere_connexion': fake.date_time_between(start_date='-1y', end_date='now'),
        'abonne_newsletter': random.choice([True, False]),
        'preferences_communication': random.choice(['Email', 'SMS', 'Courrier', 'Téléphone']),
        'interets': ', '.join(random.sample([
            'Technologie', 'Sport', 'Voyage', 'Cuisine', 'Musique',
            'Cinéma', 'Lecture', 'Art', 'Mode', 'Jeux vidéo'
        ], random.randint(1, 4)))
    }
    users_data.append(user)

# Écriture dans un fichier CSV
filename = 'users_data.csv'
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = users_data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for user in users_data:
        writer.writerow(user)

print(f"Données générées avec succès dans le fichier {filename}")
print(f"Nombre d'utilisateurs générés : {NB_USERS}") 