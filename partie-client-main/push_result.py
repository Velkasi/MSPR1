import json
import mysql.connector

# Configuration de la base de données
DB_CONFIG = {
    "host": "10.5.0.1",
    "user": "root",  # Par défaut, l'utilisateur root n'a pas de mot de passe dans XAMPP
    "password": "",
    "database": "monitoring"
}

# Fonction pour insérer les données
def insert_data(data):
    try:
        # Connexion à la base de données
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Préparer la requête d'insertion
        query = """
        INSERT INTO logs (datetime, hostname, ping_8_8_8_8, ip, port_scan, os_scan, service_scan)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query, (
            data.get("datetime"),
            data.get("hostname"),
            data.get("ping_8.8.8.8"),
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
    except Exception as e:
        print(f"Erreur : {e}")

# Charger les données JSON
json_data = """
{
    "datetime": "2025-01-25 22:45:48",
    "hostname": "DESKTOP-MO735KL",
    "ping_8.8.8.8": "5ms",
    "ip": "localhost",
    "port_scan": "135/tcp  open\n137/tcp  filtered\n445/tcp  open\n5040/tcp  open\n49664/tcp  open\n49665/tcp  open\n49666/tcp  open\n49667/tcp  open\n49668/tcp  open\n49672/tcp  open",
    "os_scan": "Running: Microsoft Windows 10",
    "service_scan": "135/tcp  msrpc  Microsoft\n445/tcp  microsoft-ds?  Service"
}
"""

data = json.loads(json_data)
insert_data(data)
