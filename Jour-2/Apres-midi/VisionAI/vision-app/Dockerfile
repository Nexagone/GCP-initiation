# Utiliser une image Python officielle
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier les fichiers de l'application
COPY . .

# Définir les variables d'environnement
ENV PORT=8080

# Exposer le port
EXPOSE 8080

# Commande pour démarrer l'application
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app