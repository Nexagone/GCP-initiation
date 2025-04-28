# Cheat Sheet des Commandes GCP

## Commandes de base gcloud

```bash
# Configuration initiale
gcloud init                                     # Configuration interactive de gcloud
gcloud config set project [PROJECT_ID]          # Définir le projet par défaut
gcloud config set compute/region [REGION]       # Définir la région par défaut  
gcloud config set compute/zone [ZONE]           # Définir la zone par défaut

# Informations sur l'environnement
gcloud info                                     # Afficher les informations sur l'installation
gcloud config list                              # Afficher la configuration actuelle
gcloud projects list                            # Lister tous les projets accessibles
gcloud components list                          # Lister les composants installés

# Gestion des composants
gcloud components install [COMPONENT]           # Installer un composant
gcloud components update                        # Mettre à jour tous les composants
gcloud components remove [COMPONENT]            # Supprimer un composant
```

## Compute Engine

```bash
# Instances
gcloud compute instances list                   # Lister les instances
gcloud compute instances create [NAME]          # Créer une instance
gcloud compute instances describe [NAME]        # Afficher les détails d'une instance
gcloud compute instances start [NAME]           # Démarrer une instance
gcloud compute instances stop [NAME]            # Arrêter une instance
gcloud compute instances delete [NAME]          # Supprimer une instance
gcloud compute ssh [NAME]                       # Se connecter en SSH à une instance

# Disques
gcloud compute disks list                       # Lister les disques
gcloud compute disks create [NAME]              # Créer un disque
gcloud compute disks snapshot [NAME]            # Créer un snapshot d'un disque

# Images
gcloud compute images list                      # Lister les images disponibles
gcloud compute images create [NAME] --source-disk=[DISK] # Créer une image depuis un disque

# Réseaux
gcloud compute networks list                    # Lister les réseaux VPC
gcloud compute networks create [NAME]           # Créer un réseau VPC
gcloud compute firewall-rules list              # Lister les règles de pare-feu
gcloud compute firewall-rules create [NAME]     # Créer une règle de pare-feu
```

## Cloud SQL

```bash
# Instances
gcloud sql instances list                       # Lister les instances
gcloud sql instances create [NAME]              # Créer une instance
gcloud sql instances describe [NAME]            # Afficher les détails d'une instance
gcloud sql instances patch [NAME]               # Modifier une instance
gcloud sql instances delete [NAME]              # Supprimer une instance
gcloud sql instances restart [NAME]             # Redémarrer une instance

# Bases de données
gcloud sql databases list --instance=[INSTANCE] # Lister les bases de données
gcloud sql databases create [DB_NAME] --instance=[INSTANCE] # Créer une base de données
gcloud sql databases delete [DB_NAME] --instance=[INSTANCE] # Supprimer une base de données

# Utilisateurs
gcloud sql users list --instance=[INSTANCE]     # Lister les utilisateurs
gcloud sql users create [USER] --instance=[INSTANCE] --password=[PASSWORD] # Créer un utilisateur
gcloud sql users set-password [USER] --instance=[INSTANCE] --password=[PASSWORD] # Modifier mot de passe

# Connexion
gcloud sql connect [INSTANCE] --user=[USER]     # Se connecter à une instance
```

## Cloud Storage

```bash
# Buckets
gsutil ls                                       # Lister les buckets
gsutil mb gs://[BUCKET_NAME]                    # Créer un bucket
gsutil rb gs://[BUCKET_NAME]                    # Supprimer un bucket
gsutil ls -l gs://[BUCKET_NAME]                 # Lister le contenu d'un bucket

# Objets
gsutil cp [LOCAL_FILE] gs://[BUCKET_NAME]/      # Télécharger un fichier
gsutil cp gs://[BUCKET_NAME]/[OBJECT] [LOCAL_PATH] # Télécharger un objet
gsutil rm gs://[BUCKET_NAME]/[OBJECT]           # Supprimer un objet
gsutil cp -r [LOCAL_DIR] gs://[BUCKET_NAME]/    # Télécharger un répertoire
gsutil cp -r gs://[BUCKET_NAME]/[DIR] [LOCAL_PATH] # Télécharger un répertoire

# Accès et permissions
gsutil iam ch [PERMISSION]:[MEMBER] gs://[BUCKET_NAME] # Ajouter une permission IAM
gsutil acl ch -u [USER_EMAIL]:READ gs://[BUCKET_NAME]/[OBJECT] # Modifier les ACL
```

## Cloud Functions

```bash
# Fonctions
gcloud functions list                           # Lister les fonctions
gcloud functions deploy [NAME] --runtime=[RUNTIME] --trigger-http # Déployer une fonction HTTP
gcloud functions deploy [NAME] --runtime=[RUNTIME] --trigger-bucket=[BUCKET] # Déployer avec trigger Storage
gcloud functions describe [NAME]                # Afficher les détails d'une fonction
gcloud functions delete [NAME]                  # Supprimer une fonction
gcloud functions logs read [NAME]               # Afficher les logs d'une fonction
gcloud functions call [NAME] --data='{"key":"value"}' # Appeler une fonction
```

## Cloud Run

```bash
# Services
gcloud run services list                        # Lister les services
gcloud run deploy [SERVICE] --image=[IMAGE]     # Déployer un service
gcloud run services describe [SERVICE]          # Afficher les détails d'un service
gcloud run services delete [SERVICE]            # Supprimer un service
gcloud run services update [SERVICE] --concurrency=[NUM] # Mettre à jour un service

# Révisions
gcloud run revisions list                       # Lister les révisions
gcloud run revisions describe [REVISION]        # Afficher les détails d'une révision
```

## IAM & Administration

```bash
# Rôles et permissions
gcloud iam roles list                           # Lister les rôles disponibles
gcloud iam roles describe [ROLE]                # Afficher les détails d'un rôle
gcloud projects add-iam-policy-binding [PROJECT_ID] --member=[MEMBER] --role=[ROLE] # Ajouter un rôle

# Service Accounts
gcloud iam service-accounts list                # Lister les comptes de service
gcloud iam service-accounts create [NAME] --display-name=[DISPLAY_NAME] # Créer un compte de service
gcloud iam service-accounts keys create [KEY_FILE] --iam-account=[EMAIL] # Créer une clé
```

## Kubernetes Engine (GKE)

```bash
# Clusters
gcloud container clusters list                  # Lister les clusters
gcloud container clusters create [NAME]         # Créer un cluster
gcloud container clusters describe [NAME]       # Afficher les détails d'un cluster
gcloud container clusters delete [NAME]         # Supprimer un cluster
gcloud container clusters get-credentials [NAME] # Configurer kubectl

# Nodes
gcloud container node-pools list --cluster=[CLUSTER] # Lister les node pools
gcloud container node-pools create [NAME] --cluster=[CLUSTER] # Créer un node pool
```

## BigQuery

```bash
# Datasets
bq ls                                           # Lister les datasets
bq mk [DATASET]                                 # Créer un dataset
bq rm -r [DATASET]                              # Supprimer un dataset

# Tables
bq ls [DATASET]                                 # Lister les tables d'un dataset
bq mk -t [DATASET].[TABLE] [SCHEMA]             # Créer une table
bq rm -t [DATASET].[TABLE]                      # Supprimer une table
bq head -n [N] [DATASET].[TABLE]                # Afficher les N premières lignes

# Requêtes
bq query --use_legacy_sql=false 'SELECT * FROM [DATASET].[TABLE] LIMIT 10' # Exécuter une requête
```

## Pub/Sub

```bash
# Topics
gcloud pubsub topics list                       # Lister les topics
gcloud pubsub topics create [TOPIC]             # Créer un topic
gcloud pubsub topics delete [TOPIC]             # Supprimer un topic
gcloud pubsub topics publish [TOPIC] --message="[MESSAGE]" # Publier un message

# Abonnements
gcloud pubsub subscriptions list                # Lister les abonnements
gcloud pubsub subscriptions create [SUB] --topic=[TOPIC] # Créer un abonnement
gcloud pubsub subscriptions delete [SUB]        # Supprimer un abonnement
gcloud pubsub subscriptions pull --auto-ack [SUB] # Tirer des messages
```

## Vertex AI

```bash
# Datasets
gcloud ai datasets list                         # Lister les datasets
gcloud ai datasets create --display-name=[NAME] --region=[REGION] # Créer un dataset
gcloud ai datasets delete [DATASET_ID]          # Supprimer un dataset

# Models
gcloud ai models list                           # Lister les modèles
gcloud ai models upload --display-name=[NAME] --container-image-uri=[URI] # Uploader un modèle
gcloud ai models delete [MODEL_ID]              # Supprimer un modèle
```

## Firestore

```bash
# Bases de données
gcloud firestore databases list                 # Lister les bases de données
gcloud firestore indexes list                   # Lister les index
gcloud firestore indexes composite create       # Créer un index composite
gcloud firestore indexes composite describe     # Afficher les détails d'un index
```

## Logging

```bash
# Logs
gcloud logging read "resource.type=gce_instance" --limit=10 # Lire les logs
gcloud logging read "severity>=ERROR" --project=[PROJECT] # Lire les logs d'erreur
gcloud logging write [LOG_NAME] "[MESSAGE]" --severity=INFO # Écrire un log
```

## Monitoring

```bash
# Alertes
gcloud monitoring policies list                 # Lister les politiques d'alerte
gcloud monitoring channels list                 # Lister les canaux de notification
gcloud monitoring dashboards list               # Lister les tableaux de bord
```

## Cloud Build

```bash
# Builds
gcloud builds list                              # Lister les builds
gcloud builds submit --tag=[IMAGE] [SOURCE]     # Soumettre un build
gcloud builds describe [BUILD_ID]               # Afficher les détails d'un build
```

## Astuces

```bash
# Filtrer les résultats
gcloud compute instances list --filter="name ~ 'web-*'" # Filtrer par nom
gcloud compute instances list --filter="zone:us-central1-a" # Filtrer par zone

# Format de sortie
gcloud compute instances list --format="table(name,zone,status)" # Format tableau
gcloud compute instances list --format="json" # Format JSON
gcloud compute instances list --format="yaml" # Format YAML
gcloud compute instances list --format="csv(name,zone,status)" # Format CSV

# Projets multiples
gcloud config set project [PROJECT_ID]          # Changer de projet actif
gcloud compute instances list --project=[PROJECT_ID] # Spécifier un projet pour une commande

# Automatisation
gcloud config set core/disable_prompts True     # Désactiver les invites interactives
```
