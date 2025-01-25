import json
import requests

# URL de votre script PHP sur la machine cible
url = "http://10.5.0.1/insert.php"

# Chemin du fichier JSON
file_path = "scan_results.json"

try:
    # Lire le contenu du fichier JSON
    with open(file_path, 'r') as file:
        data = json.load(file)

    # En-têtes HTTP
    headers = {'Content-Type': 'application/json'}

    # Envoyer les données au serveur
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Afficher la réponse
    print("Response:", response.status_code, response.json())
except FileNotFoundError:
    print(f"Erreur : Le fichier {file_path} est introuvable.")
except json.JSONDecodeError:
    print(f"Erreur : Le fichier {file_path} contient un JSON invalide.")
except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la connexion au serveur : {e}")
