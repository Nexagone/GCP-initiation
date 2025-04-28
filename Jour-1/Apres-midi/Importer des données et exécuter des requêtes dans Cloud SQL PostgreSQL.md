# Atelier pratique : Importer des données et exécuter des requêtes dans Cloud SQL PostgreSQL

## 1. Introduction à Cloud SQL

Cloud SQL est un service de base de données entièrement géré qui facilite la configuration, la maintenance, la gestion et l'administration de bases de données relationnelles dans le cloud. Il offre plusieurs moteurs de base de données :
- MySQL
- PostgreSQL
- SQL Server

### Avantages de Cloud SQL
- Entièrement géré (mises à jour automatiques, sauvegardes, réplication)
- Haute disponibilité
- Sécurité intégrée
- Évolutivité
- Intégration avec d'autres services cloud

## 2. Préparation de l'environnement

### Prérequis
- Un compte avec accès à la console Cloud SQL
- Droits d'administration sur l'instance Cloud SQL
- Données à importer (fichiers CSV, SQL dumps, ou autres formats)
- Client SQL ou interface d'administration (par exemple : Cloud Shell, MySQL Workbench, pgAdmin)

### Création/Configuration de l'instance
1. Accédez à la console Cloud SQL
2. Sélectionnez "Créer une instance"
3. Choisissez le moteur de base de données (MySQL, PostgreSQL, SQL Server)
4. Configurez les paramètres de base :
   - Nom de l'instance
   - Mot de passe administrateur
   - Région et zone
   - Version du moteur
5. (Optionnel) Configurez les options avancées :
   - Taille de la machine
   - Stockage
   - Haute disponibilité
   - Sauvegardes automatiques
   - Maintenance

## 3. Importer des données

### Méthode 1 : Importation depuis des fichiers CSV
1. Préparation des fichiers CSV
   - Vérifiez le format (séparateurs, en-têtes, encodage)
   - Stockez les fichiers dans un bucket Cloud Storage

2. Importation via la console
   - Accédez à votre instance
   - Allez dans "Importation"
   - Sélectionnez le fichier source dans Cloud Storage
   - Spécifiez la base de données et les options d'importation
   - Lancez l'importation

3. Importation via ligne de commande (PostgreSQL)
   ```sql
   -- Utilisation de la commande COPY
   COPY nom_table FROM 'chemin/vers/fichier.csv' 
   WITH (FORMAT CSV, HEADER, DELIMITER ',');
   
   -- Ou avec psql
   \copy nom_table FROM 'chemin/vers/fichier.csv' WITH CSV HEADER DELIMITER ','
   ```

### Méthode 2 : Importation d'un dump SQL
1. Préparation du dump SQL
   - Créez un dump depuis votre base de données existante avec `pg_dump`
     ```bash
     pg_dump -h [HÔTE] -U [UTILISATEUR] -d [NOM_BDD] -F c -f sauvegarde.dump
     ```
   - Stockez le fichier dans Cloud Storage

2. Importation via la console
   - Accédez à votre instance
   - Allez dans "Importation"
   - Sélectionnez le fichier dump dans Cloud Storage
   - Lancez l'importation

3. Importation via ligne de commande
   ```bash
   # Pour un dump au format personnalisé (-F c)
   pg_restore -h [IP_INSTANCE] -U [UTILISATEUR] -d [NOM_BDD] -v sauvegarde.dump
   
   # Pour un dump au format SQL plein texte
   psql -h [IP_INSTANCE] -U [UTILISATEUR] -d [NOM_BDD] -f sauvegarde.sql
   ```

### Méthode 3 : Migration depuis une base externe
1. Configuration de la réplication
2. Utilisation des outils de migration de données
   - Database Migration Service
   - Outils spécifiques aux moteurs de base de données

## 4. Exécuter des requêtes

### Connexion à la base de données
1. Via la console Cloud SQL
   - Utilisez l'éditeur SQL intégré
   
2. Via Cloud Shell
   ```bash
   # Connexion à PostgreSQL via Cloud Shell
   gcloud sql connect [NOM_INSTANCE] --user=[UTILISATEUR] --database=[NOM_BDD]
   ```

3. Via un client SQL externe (comme pgAdmin)
   - Configurez un proxy Cloud SQL ou utilisez une connexion IP autorisée
   ```bash
   # Configuration du proxy Cloud SQL
   ./cloud_sql_proxy -instances=[PROJET:RÉGION:INSTANCE]=tcp:5432
   
   # Puis connectez-vous avec pgAdmin ou psql
   psql -h localhost -p 5432 -U [UTILISATEUR] -d [NOM_BDD]
   ```

### Types de requêtes SQL

#### Requêtes de base
```sql
-- Sélectionner toutes les données d'une table
SELECT * FROM table_name;

-- Sélectionner des colonnes spécifiques
SELECT colonne1, colonne2 FROM table_name;

-- Filtrer les résultats
SELECT * FROM table_name WHERE condition;

-- Trier les résultats
SELECT * FROM table_name ORDER BY colonne ASC/DESC;

-- Limiter le nombre de résultats
SELECT * FROM table_name LIMIT 10;
```

#### Requêtes avancées spécifiques à PostgreSQL
```sql
-- Jointures
SELECT t1.colonne1, t2.colonne2
FROM table1 t1
JOIN table2 t2 ON t1.id = t2.id;

-- Agrégations
SELECT colonne1, COUNT(*), AVG(colonne_numerique)
FROM table_name
GROUP BY colonne1;

-- Sous-requêtes
SELECT *
FROM table_name
WHERE colonne1 IN (SELECT colonne1 FROM autre_table WHERE condition);

-- Expressions de table communes (CTE)
WITH cte_name AS (
  SELECT colonne1, colonne2
  FROM table_name
  WHERE condition
)
SELECT * FROM cte_name;

-- Fenêtrage (Window functions)
SELECT 
    colonne1,
    valeur,
    AVG(valeur) OVER (PARTITION BY colonne1) as moyenne_par_groupe,
    RANK() OVER (ORDER BY valeur DESC) as classement
FROM table_name;

-- JSON/JSONB
SELECT 
    id,
    donnees_json->>'nom' as nom,
    (donnees_json->'adresse'->>'ville')::text as ville
FROM table_with_json
WHERE donnees_json @> '{"statut": "actif"}';

-- Requêtes récursives
WITH RECURSIVE hierarchie AS (
    -- Requête d'ancrage
    SELECT id, parent_id, nom, 1 as niveau
    FROM organisation
    WHERE parent_id IS NULL
    
    UNION ALL
    
    -- Partie récursive
    SELECT o.id, o.parent_id, o.nom, h.niveau + 1
    FROM organisation o
    JOIN hierarchie h ON o.parent_id = h.id
)
SELECT * FROM hierarchie ORDER BY niveau, nom;
```

#### Requêtes de modification
```sql
-- Insérer des données
INSERT INTO table_name (colonne1, colonne2)
VALUES (valeur1, valeur2);

-- Mettre à jour des données
UPDATE table_name
SET colonne1 = nouvelle_valeur
WHERE condition;

-- Supprimer des données
DELETE FROM table_name
WHERE condition;
```

## 5. Optimisation des performances

### Bonnes pratiques
1. Indexez correctement vos tables
   ```sql
   CREATE INDEX idx_nom ON table_name(colonne);
   
   -- Index B-tree (par défaut)
   CREATE INDEX idx_btree ON table_name(colonne);
   
   -- Index GIN (pour les recherches textuelles et tableaux)
   CREATE INDEX idx_gin ON table_name USING GIN (colonne_jsonb);
   
   -- Index GIST (pour les données géospatiales)
   CREATE INDEX idx_gist ON table_name USING GIST (colonne_geo);
   ```

2. Analysez vos requêtes
   ```sql
   -- Affiche le plan d'exécution
   EXPLAIN SELECT * FROM table_name WHERE condition;
   
   -- Affiche le plan d'exécution avec temps d'exécution
   EXPLAIN ANALYZE SELECT * FROM table_name WHERE condition;
   
   -- Utilisation de VACUUM pour nettoyer la base
   VACUUM (ANALYZE) table_name;
   ```

3. Mettez à jour les statistiques
   ```sql
   -- Mettez à jour les statistiques d'une table
   ANALYZE table_name;
   
   -- Configurez l'autovacuum
   ALTER TABLE table_name SET (autovacuum_enabled = true);
   ```

4. Surveillez les performances via la console Cloud SQL
   - Métriques de CPU, mémoire, stockage, E/S
   - Journaux d'audit et d'erreurs
   - Visualisez les requêtes lentes dans les logs PostgreSQL

## 6. Exercices pratiques

### Exercice 1 : Importation de données
1. Importez un ensemble de données d'exemple (clients, commandes, produits)
2. Vérifiez l'intégrité des données importées

### Exercice 2 : Requêtes simples
1. Sélectionnez tous les clients d'une région spécifique
2. Trouvez les produits les plus chers
3. Identifiez les commandes passées dans un intervalle de dates

### Exercice 3 : Requêtes avancées
1. Calculez le chiffre d'affaires par client
2. Trouvez les produits jamais commandés
3. Identifiez les tendances de vente mensuelles

## 7. Ressources complémentaires

- [Documentation officielle Cloud SQL pour PostgreSQL](https://cloud.google.com/sql/docs/postgres)
- [Bonnes pratiques pour Cloud SQL PostgreSQL](https://cloud.google.com/sql/docs/postgres/best-practices)
- [Tutoriels sur SQL](https://www.w3schools.com/sql/)
- [Documentation officielle PostgreSQL](https://www.postgresql.org/docs/)
- [PostgreSQL Exercices pratiques](https://pgexercises.com/)
- [Tutoriel interactif PostgreSQL](https://www.postgresqltutorial.com/)

## 8. Dépannage courant

### Problèmes de connexion
- Vérifiez les autorisations de réseau et les règles de pare-feu
- Confirmez que les identifiants sont corrects
- Vérifiez que l'instance est en cours d'exécution

### Problèmes d'importation
- Vérifiez le format et l'encodage des fichiers
- Assurez-vous que vous avez les autorisations nécessaires
- Consultez les journaux d'erreurs pour plus de détails

### Problèmes de performances
- Vérifiez l'utilisation des ressources
- Examinez les plans d'exécution des requêtes
- Considérez la mise à niveau de votre instance si nécessaire
