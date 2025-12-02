# ---------------------------
# 1. Choix de l'image Python
# ---------------------------
FROM python:3.13-slim

# ---------------------------
# 2. Variables d'environnement pour la prod
# ---------------------------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ---------------------------
# 3. Définir le répertoire de travail
# ---------------------------
WORKDIR /app

# ---------------------------
# 4. Copier les fichiers nécessaires
# ---------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ---------------------------
# 5. Exposer le port (celui que Flask utilisera)
# ---------------------------
EXPOSE 5000

# ---------------------------
# 6. Commande pour lancer l'app
# ---------------------------
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

