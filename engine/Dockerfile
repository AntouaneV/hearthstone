FROM python:3.8

# Copiez les fichiers de l'application dans le conteneur
COPY . /app

# Définissez /app comme répertoire de travail
WORKDIR /app

# Installez les dépendances de l'application
RUN pip install -r requirements.txt

# Exposez le port 8000 pour que l'application puisse être accessible depuis l'extérieur
EXPOSE 8000

# Définissez le script `entrypoint` comme script d'entrée du conteneur
ENTRYPOINT ["/app/entrypoint.sh"]