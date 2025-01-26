<?php
// Connexion à la base de données
$host = 'localhost';
$user = 'root';
$password = ''; // Mot de passe par défaut pour XAMPP
$dbname = 'monitoring';

$conn = new mysqli($host, $user, $password, $dbname);

// Vérifiez la connexion
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Lire les données JSON envoyées via POST
$data = file_get_contents('php://input');
$json_data = json_decode($data, true);

// Vérifier si les données JSON sont valides
if (json_last_error() === JSON_ERROR_NONE) {
    // Préparer la requête d'insertion
    $stmt = $conn->prepare(
        "INSERT INTO logs (datetime, hostname, ip, ping, port_scan, os_scan, service_scan) 
        VALUES (?, ?, ?, ?, ?, ?, ?)"
    );

    if ($stmt) {
        // Associer les paramètres
        $stmt->bind_param(
            "sssssss", // Types des paramètres : "s" pour string
            $json_data['datetime'],
            $json_data['hostname'],
            $json_data['ip'],
            $json_data['ping_8.8.8.8'],
            $json_data['port_scan'],
            $json_data['os_scan'],
            $json_data['service_scan']
        );

        // Exécuter la requête
        if ($stmt->execute()) {
            echo json_encode(["status" => "success", "message" => "Data inserted successfully"]);
        } else {
            echo json_encode(["status" => "error", "message" => $stmt->error]);
        }

        // Fermer la requête
        $stmt->close();
    } else {
        echo json_encode(["status" => "error", "message" => "Failed to prepare the statement"]);
    }
} else {
    echo json_encode(["status" => "error", "message" => "Invalid JSON"]);
}

// Fermer la connexion
$conn->close();
?>
