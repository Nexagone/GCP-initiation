# Déploiement et Configuration d'une Instance Cloud SQL

## 1. Accès à Cloud SQL
- Depuis la console GCP, allez dans le menu de navigation
- Recherchez et sélectionnez "SQL" dans la section Base de données

## 2. Création de l'instance
- Cliquez sur "Créer une instance"
- Choisissez le type de base de données :
  - MySQL
  - PostgreSQL
  - SQL Server
- Cliquez sur "Suivant"

## 3. Configuration de l'instance
- Nommez votre instance (ID d'instance unique)
- Définissez un mot de passe pour l'utilisateur root/postgres/sqlserver
- Choisissez la région et la zone de disponibilité
- Sélectionnez la version du moteur de base de données

## 4. Configuration des ressources
- Choisissez la configuration machine (vCPUs et mémoire)
- Sélectionnez le type de stockage (SSD ou HDD)
- Définissez la capacité de stockage initiale
- Configurez l'autoscaling du stockage si nécessaire

## 5. Configuration de la disponibilité
- Choisissez entre :
  - Instance unique (moins coûteuse)
  - Instance à haute disponibilité (avec réplica secondaire)
- Configurez les sauvegardes automatiques
  - Définissez la fenêtre de sauvegarde
  - Configurez la rétention des sauvegardes

## 6. Configuration réseau et sécurité
- Dans l'onglet "Connexions" :
  - Activez/désactivez l'adresse IP publique
  - Configurez les réseaux autorisés (liste d'adresses IP)
  - Configurez l'accès via le service Cloud SQL Auth Proxy
  - Configurez la connexion via Private Service Connect ou Service Networking

## 7. Configurez les options avancées (optionnel)
- Dans l'onglet "Indicateurs de base de données" :
  - Configurez les paramètres personnalisés du moteur de BDD
- Dans l'onglet "Maintenance" :
  - Définissez la fenêtre de maintenance
- Activez éventuellement les journaux, l'audit, etc.

## 8. Création de l'instance
- Cliquez sur "Créer" et attendez le provisionnement (peut prendre plusieurs minutes)

## 9. Post-création
- Créez des bases de données additionnelles
- Créez des utilisateurs supplémentaires
- Configurez les réplicas de lecture si nécessaire
- Importez des données existantes

## 10. Connexion à l'instance
- Via la console GCP (shell Cloud SQL)
- Via le proxy Cloud SQL Auth
- Via les applications clientes en utilisant les paramètres de connexion
- Via les applications hébergées sur GCP (App Engine, Compute Engine, etc.)
