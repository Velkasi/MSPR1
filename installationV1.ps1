# ================================
# Script d'installation pour Windows
# ================================

# Message d'introduction
Write-Output "=== Début de l'installation ==="

# Étape 1 : Vérification et installation de Python
Write-Output "Vérification de Python..."
if (-not (Get-Command "python" -ErrorAction SilentlyContinue)) {
    Write-Output "Python n'est pas installé. Installation avec Chocolatey..."
    
    # Vérifie si Chocolatey est installé, sinon l'installe
    if (-not (Get-Command "choco" -ErrorAction SilentlyContinue)) {
        Write-Output "Installation de Chocolatey..."
        Set-ExecutionPolicy Bypass -Scope Process -Force
        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
        Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    }

    # Installe Python avec Chocolatey
    choco install python -y
} else {
    Write-Output "Python est déjà installé."
}

# Étape 2 : Vérification et installation de pip
Write-Output "Vérification de pip..."
if (-not (Get-Command "pip" -ErrorAction SilentlyContinue)) {
    Write-Output "pip n'est pas installé. Installation..."
    python -m ensurepip --upgrade
} else {
    Write-Output "pip est déjà installé."
}

# Étape 3 : Installation de nmap
Write-Output "Vérification de nmap..."
if (-not (Get-Command "nmap" -ErrorAction SilentlyContinue)) {
    Write-Output "nmap n'est pas installé. Installation avec Chocolatey..."
    choco install nmap -y
} else {
    Write-Output "nmap est déjà installé."
}

# Étape 4 : Installation des dépendances Python
Write-Output "Installation des dépendances Python..."
if (Test-Path "requirements.txt") {
    pip install -r requirements.txt
} else {
    Write-Output "Le fichier requirements.txt est introuvable. Veuillez le créer."
}

# Message de fin
Write-Output "=== Installation terminée avec succès ==="
