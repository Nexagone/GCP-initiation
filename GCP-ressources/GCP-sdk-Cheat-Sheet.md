# Cheat Sheet Google Cloud SDK (gcloud)

## Installation et Configuration

```bash
# Installation du SDK
# Linux
curl https://sdk.cloud.google.com | bash
# Windows - télécharger l'installateur depuis cloud.google.com/sdk/docs/install

# Initialisation
gcloud init                                      # Configuration interactive de base
gcloud auth login                                # Authentification via navigateur
gcloud auth application-default login            # Authentification pour les applications locales

# Configuration
gcloud config set project [PROJECT_ID]           # Définir le projet par défaut
gcloud config set compute/region [REGION]        # Définir la région par défaut
gcloud config set compute/zone [ZONE]            # Définir la zone par défaut
gcloud config configurations create [NAME]       # Créer une configuration nommée
gcloud config configurations activate [NAME]     # Activer une configuration
gcloud config list                               # Afficher la configuration active
```

## Gestion des Projets

```bash
gcloud projects list                             # Lister tous les projets accessibles
gcloud projects create [PROJECT_ID]              # Créer un nouveau projet
gcloud projects describe [PROJECT_ID]            # Afficher les détails d'un projet
gcloud projects delete [PROJECT_ID]              # Supprimer un projet
gcloud config set project [PROJECT_ID]           # Changer de projet actif
```

## Compute Engine

```bash
# Instances
gcloud compute instances list                    # Lister les instances
gcloud compute instances create [INSTANCE_NAME] \
    --machine-type=[MACHINE_TYPE] \
    --image-family=[IMAGE_FAMILY] \
    --image-project=[IMAGE_PROJECT]              # Créer une instance

gcloud compute instances describe [INSTANCE_NAME] # Détails d'une instance
gcloud compute instances start [INSTANCE_NAME]   # Démarrer une instance
gcloud compute instances stop [INSTANCE_NAME]    # Arrêter une instance
gcloud compute instances delete [INSTANCE_NAME]  # Supprimer une instance
gcloud compute ssh [INSTANCE_NAME]               # Connexion SSH

# Disques
gcloud compute disks list                        # Lister les disques
gcloud compute disks create [DISK_NAME] --size=[SIZE] # Créer un disque
gcloud compute instances attach-disk [INSTANCE_NAME] \
    --disk=[DISK_NAME]                           # Attacher un disque

# Images et snapshots
gcloud compute images list                       # Lister les images disponibles
gcloud compute images create [IMAGE_NAME] --source-disk=[DISK_NAME] # Créer une image
gcloud compute snapshots create [SNAPSHOT_NAME] \
    --source-disk=[DISK_NAME]                    # Créer un snapshot

# Réseaux et pare-feu
gcloud compute networks list                     # Lister les réseaux VPC
gcloud compute networks create [NETWORK_NAME]    # Créer un réseau VPC
gcloud compute firewall-rules list               # Lister les règles de pare-feu
gcloud compute firewall-rules create [RULE_NAME] \
    --network=[NETWORK] \
    --allow=[PROTOCOL]:[PORT]                    # Créer une règle de pare-feu
```

## Cloud SQL

```bash
# Instances
gcloud sql instances list                        # Lister les instances
gcloud sql instances create [INSTANCE_NAME] \
    --database-version=[VERSION] \
    --tier=[MACHINE_TYPE]                        # Créer une instance

gcloud sql instances describe [INSTANCE_NAME]    # Détails d'une instance
gcloud sql instances patch [INSTANCE_NAME] \
    --activation-policy=ALWAYS                   # Modifier une instance
gcloud sql instances restart [INSTANCE_NAME]     # Redémarrer une instance
gcloud sql instances delete [INSTANCE_NAME]      # Supprimer une instance

# Bases de données
gcloud sql databases list \
    --instance=[INSTANCE_NAME]                   # Lister les bases de données
gcloud sql databases create [DATABASE_NAME] \
    --instance=[INSTANCE_NAME]                   # Créer une base de données
gcloud sql databases delete [DATABASE_NAME] \
    --instance=[INSTANCE_NAME]                   # Supprimer une base de données

# Utilisateurs
gcloud sql users list \
    --instance=[INSTANCE_NAME]                   # Lister les utilisateurs
gcloud sql users create [USER_NAME] \
    --instance=[INSTANCE_NAME] \
    --password=[PASSWORD]                        # Créer un utilisateur
gcloud sql users set-password [USER_NAME] \
    --instance=[INSTANCE_NAME] \
    --password=[PASSWORD]                        # Modifier un mot de passe

# Connexion via proxy
gcloud sql connect [INSTANCE_NAME] --user=[USER_NAME] # Connexion directe
# Téléchargement et utilisation du proxy Cloud SQL
wget https://dl.google.com/cloudsql/cloud_sql_proxy_x64.linux
chmod +x cloud_sql_proxy_x64.linux
./cloud_sql_proxy_x64.linux \
    -instances=[INSTANCE_CONNECTION_NAME]=tcp:5432
```

## Cloud Storage

```bash
# Buckets
gsutil ls                                        # Lister les buckets
gsutil mb gs://[BUCKET_NAME]                     # Créer un bucket
gsutil rb gs://[BUCKET_NAME]                     # Supprimer un bucket (vide)
gsutil rb -f gs://[BUCKET_NAME]                  # Force la suppression (récursive)

# Objets
gsutil ls gs://[BUCKET_NAME]                     # Lister les objets dans un bucket
gsutil cp [LOCAL_FILE] gs://[BUCKET_NAME]/       # Uploader un fichier
gsutil cp gs://[BUCKET_NAME]/[OBJECT] [LOCAL_FILE] # Télécharger un objet
gsutil rm gs://[BUCKET_NAME]/[OBJECT]            # Supprimer un objet
gsutil cp -r [LOCAL_DIR] gs://[BUCKET_NAME]/     # Uploader un répertoire
gsutil rsync -r [LOCAL_DIR] gs://[BUCKET_NAME]/  # Synchroniser un répertoire

# Gestion des accès
gsutil acl ch -u [USER_EMAIL]:R gs://[BUCKET_NAME]/[OBJECT] # Donner accès en lecture
gsutil iam ch serviceAccount:[EMAIL]:objectCreator gs://[BUCKET_NAME] # IAM sur bucket
gsutil defacl set private gs://[BUCKET_NAME]     # Définir ACL par défaut
```

## Kubernetes Engine (GKE)

```bash
# Clusters
gcloud container clusters list                   # Lister les clusters
gcloud container clusters create [CLUSTER_NAME] \
    --num-nodes=[NUM_NODES]                      # Créer un cluster
gcloud container clusters resize [CLUSTER_NAME] \
    --node-pool=[POOL_NAME] \
    --num-nodes=[NUM_NODES]                      # Redimensionner un cluster
gcloud container clusters get-credentials [CLUSTER_NAME] # Configurer kubectl
gcloud container clusters delete [CLUSTER_NAME]  # Supprimer un cluster

# Node pools
gcloud container node-pools list \
    --cluster=[CLUSTER_NAME]                     # Lister les node pools
gcloud container node-pools create [POOL_NAME] \
    --cluster=[CLUSTER_NAME] \
    --machine-type=[MACHINE_TYPE] \
    --num-nodes=[NUM_NODES]                      # Créer un node pool
gcloud container node-pools delete [POOL_NAME] \
    --cluster=[CLUSTER_NAME]                     # Supprimer un node pool

# kubectl (après avoir obtenu les credentials)
kubectl get pods --all-namespaces                # Lister tous les pods
kubectl create -f [YAML_FILE]                    # Créer depuis un fichier YAML
kubectl apply -f [YAML_FILE]                     # Appliquer un fichier YAML
kubectl describe pod [POD_NAME]                  # Décrire un pod
kubectl logs [POD_NAME]                          # Afficher les logs d'un pod
```

## Cloud Functions

```bash
# Fonctions
gcloud functions list                            # Lister les fonctions
gcloud functions deploy [FUNCTION_NAME] \
    --runtime=[RUNTIME] \
    --trigger-http \
    --entry-point=[FUNCTION_ENTRYPOINT] \
    --source=[SOURCE_DIR]                        # Déployer une fonction HTTP

gcloud functions deploy [FUNCTION_NAME] \
    --runtime=[RUNTIME] \
    --trigger-bucket=[BUCKET] \
    --entry-point=[FUNCTION_ENTRYPOINT] \
    --source=[SOURCE_DIR]                        # Déployer fonction avec trigger Storage

gcloud functions describe [FUNCTION_NAME]        # Détails d'une fonction
gcloud functions logs read [FUNCTION_NAME]       # Lire les logs d'une fonction
gcloud functions call [FUNCTION_NAME] \
    --data='{"name":"value"}'                    # Appeler une fonction
gcloud functions delete [FUNCTION_NAME]          # Supprimer une fonction
```

## Cloud Run

```bash
# Services
gcloud run services list                         # Lister les services
gcloud run deploy [SERVICE_NAME] \
    --image=[IMAGE_URL] \
    --platform=managed \
    --region=[REGION] \
    --allow-unauthenticated                      # Déployer un service

gcloud run services describe [SERVICE_NAME]      # Détails d'un service
gcloud run services update [SERVICE_NAME] \
    --concurrency=[CONCURRENCY]                  # Mettre à jour un service
gcloud run services delete [SERVICE_NAME]        # Supprimer un service

# Révisions
gcloud run revisions list                        # Lister les révisions
gcloud run revisions describe [REVISION_NAME]    # Détails d'une révision
```

## IAM & Sécurité

```bash
# Rôles et autorisations
gcloud iam roles list                           # Lister tous les rôles
gcloud iam roles create [ROLE_ID] \
    --title=[TITLE] \
    --permissions=[PERMISSIONS]                 # Créer un rôle personnalisé
gcloud iam roles describe [ROLE_ID]             # Décrire un rôle

# Attribution de rôles
gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member=user:[USER_EMAIL] \
    --role=[ROLE]                               # Attribuer un rôle à un utilisateur

gcloud projects remove-iam-policy-binding [PROJECT_ID] \
    --member=user:[USER_EMAIL] \
    --role=[ROLE]                               # Révoquer un rôle

# Comptes de service
gcloud iam service-accounts list                # Lister les comptes de service
gcloud iam service-accounts create [NAME] \
    --display-name="[DISPLAY_NAME]"             # Créer un compte de service
gcloud iam service-accounts keys create [KEY_FILE] \
    --iam-account=[SA_EMAIL]                    # Créer une clé de compte de service
```

## App Engine

```bash
# Déploiement
gcloud app deploy                               # Déployer une application
gcloud app deploy --version=[VERSION]           # Déployer avec une version spécifique
gcloud app browse                               # Ouvrir l'app dans le navigateur
gcloud app logs read                            # Lire les logs

# Gestion
gcloud app versions list                        # Lister les versions
gcloud app versions start [VERSION]             # Démarrer une version
gcloud app versions stop [VERSION]              # Arrêter une version
gcloud app versions delete [VERSION]            # Supprimer une version
```

## BigQuery

```bash
# Datasets
bq ls                                           # Lister les datasets
bq mk [DATASET]                                 # Créer un dataset
bq show [DATASET]                               # Afficher les détails d'un dataset
bq rm -r -f [DATASET]                           # Supprimer un dataset

# Tables
bq ls [DATASET]                                 # Lister les tables d'un dataset
bq mk -t [DATASET].[TABLE] [SCHEMA]             # Créer une table
bq mk -t [DATASET].[TABLE] [SCHEMA_FILE]        # Créer une table à partir d'un fichier
bq show [DATASET].[TABLE]                       # Afficher les détails d'une table
bq head -n [NUMBER] [DATASET].[TABLE]           # Afficher les premières lignes
bq rm -t [DATASET].[TABLE]                      # Supprimer une table

# Import/Export
bq load --source_format=[FORMAT] \
    [DATASET].[TABLE] [DATA_SOURCE] [SCHEMA]    # Charger des données
bq extract [DATASET].[TABLE] [DESTINATION]      # Extraire des données

# Requêtes
bq query --use_legacy_sql=false \
    'SELECT * FROM `[PROJECT].[DATASET].[TABLE]` LIMIT 10' # Exécuter une requête
```

## Pub/Sub

```bash
# Topics
gcloud pubsub topics list                       # Lister les topics
gcloud pubsub topics create [TOPIC]             # Créer un topic
gcloud pubsub topics publish [TOPIC] \
    --message="[MESSAGE]"                       # Publier un message
gcloud pubsub topics delete [TOPIC]             # Supprimer un topic

# Abonnements
gcloud pubsub subscriptions list                # Lister les abonnements
gcloud pubsub subscriptions create [SUB] \
    --topic=[TOPIC]                             # Créer un abonnement
gcloud pubsub subscriptions pull --auto-ack [SUB] # Tirer des messages
gcloud pubsub subscriptions delete [SUB]        # Supprimer un abonnement
```

## Logging et Monitoring

```bash
# Logging
gcloud logging read "resource.type=gce_instance" --limit=10 # Lire les logs
gcloud logging read "severity>=ERROR" --format=json # Logs d'erreur en JSON
gcloud logging write [LOG_NAME] "[MESSAGE]" \
    --severity=INFO                             # Écrire un log

# Monitoring
gcloud monitoring metrics list                  # Lister les métriques disponibles
gcloud monitoring policies list                 # Lister les politiques d'alerte
gcloud monitoring channels list                 # Lister les canaux de notification
```

## Deployment Manager

```bash
# Déploiements
gcloud deployment-manager deployments list      # Lister les déploiements
gcloud deployment-manager deployments create [NAME] \
    --config=[CONFIG_FILE]                      # Créer un déploiement
gcloud deployment-manager deployments update [NAME] \
    --config=[CONFIG_FILE]                      # Mettre à jour un déploiement
gcloud deployment-manager deployments describe [NAME] # Décrire un déploiement
gcloud deployment-manager deployments delete [NAME] # Supprimer un déploiement
```

## Astuces

```bash
# Formatage des sorties
gcloud [COMMAND] --format=json                  # Sortie en JSON
gcloud [COMMAND] --format=yaml                  # Sortie en YAML
gcloud [COMMAND] --format=csv                   # Sortie en CSV
gcloud [COMMAND] --format="table(col1,col2)"    # Sortie en tableau avec colonnes spécifiques

# Filtrage
gcloud [COMMAND] --filter="property=value"      # Filtrer par propriété exacte
gcloud [COMMAND] --filter="property~value"      # Filtrer avec expression régulière
gcloud [COMMAND] --filter="property>value"      # Comparaison numérique

# Automatisation
gcloud config set disable_prompts true          # Désactiver toutes les invites (non-interactif)
gcloud [COMMAND] --quiet                        # Exécuter une commande sans confirmation

# Aide et documentation
gcloud help [COMMAND]                           # Afficher l'aide pour une commande
gcloud [COMMAND] --help                         # Version courte de l'aide
gcloud topic TOPIC                              # Documentation sur un sujet spécifique

# Profils et configurations
gcloud config configurations activate [NAME]    # Activer une configuration existante
gcloud config configurations create [NAME]      # Créer une nouvelle configuration
gcloud config configurations list               # Lister toutes les configurations
```
