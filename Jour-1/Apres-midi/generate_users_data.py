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
    return fake.date_between(start_date=start_date, end_date=end_date).strftime('%Y-%m-%d')

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

# Fonction pour générer une profession détaillée
def generate_detailed_profession():
    base_job = fake.job()
    specializations = [
        "spécialisé en", "expert en", "conseiller en", "consultant en",
        "ingénieur en", "technicien en", "analyste en", "responsable en"
    ]
    domains = [
        "gestion de projet", "développement web", "analyse de données",
        "sécurité informatique", "cloud computing", "intelligence artificielle",
        "marketing digital", "communication", "ressources humaines",
        "finance internationale", "logistique", "qualité"
    ]
    experience = f"avec {random.randint(2, 20)} ans d'expérience"
    return f"{base_job} {random.choice(specializations)} {random.choice(domains)} {experience}"

# Création des données
users_data = []
for _ in range(NB_USERS):
    user = {
        'prenom': fake.first_name(),
        'nom': fake.last_name(),
        'email': fake.email(),
        'date_naissance': generate_birth_date(),
        'telephone': generate_phone_number(),
        'adresse': fake.street_address(),
        'code_postal': fake.postcode(),
        'ville': fake.city(),
        'pays': 'France',
        'profession': generate_detailed_profession(),
        'entreprise': fake.company(),
        'salaire_annuel': random.randint(25000, 120000),
        'statut_marital': generate_marital_status(),
        'nombre_enfants': random.randint(0, 4),
        'niveau_etudes': generate_education_level(),
        'date_inscription': fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d'),
        'derniere_connexion': fake.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d %H:%M:%S'),
        'abonne_newsletter': random.choice(['true', 'false']),
        'preferences_communication': random.choice(['Email', 'SMS', 'Courrier', 'Téléphone']),
        'interets': ', '.join(random.sample([
            'Technologie', 'Sport', 'Voyage', 'Cuisine', 'Musique',
            'Cinéma', 'Lecture', 'Art', 'Mode', 'Jeux vidéo'
        ], random.randint(1, 4)))
    }
    users_data.append(user)

# Écriture dans un fichier CSV sans en-têtes
filename = 'users_data.csv'
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    for user in users_data:
        writer.writerow(user.values())

print(f"Données générées avec succès dans le fichier {filename}")
print(f"Nombre d'utilisateurs générés : {NB_USERS}") 