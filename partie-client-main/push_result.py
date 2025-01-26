import json
import mysql.connector
import time

# Configuration de la base de données
DB_CONFIG = {
    "host": "10.5.0.1",
    "user": "root1",  # Par défaut, l'utilisateur root n'a pas de mot de passe dans XAMPP
    "password": "",
    "database": "resultat"
}

# Fonction pour insérer les données
def insert_data(data):
    try:
        # Connexion à la base de données
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Préparer la requête d'insertion
        query = """
        INSERT INTO monitoring (datetime, hostname, ping, ip, port_scan, os_scan, service_scan)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query, (
            data.get("datetime"),
            data.get("hostname"),
            data.get("ping"),
            data.get("ip"),
            data.get("port_scan"),
            data.get("os_scan"),
            data.get("service_scan"),
        ))

        # Validation et fermeture
        conn.commit()
        cursor.close()
        conn.close()
        print("Données insérées avec succès !")
    except mysql.connector.Error as err:
        print(f"Erreur de connexion à la base de données : {err}")
    except Exception as e:
        print(f"Erreur : {e}")

# Charger les données JSON à partir du fichier
with open('scan_results.json', 'r') as file:
    data = json.load(file)

insert_data(data)

delay = 10
for _ in range(3):
    insert_data(data)
    print(f"Attente de {delay} secondes avant la prochaine insertion...")
    time.sleep(delay)
