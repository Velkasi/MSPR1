REM Indication du lancement
echo Lancement du script d'installation ...

REM Output file path
set "outputPath=%USERPROFILE%\python-3.9.0-amd64.exe"
set "nmapPath=%USERPROFILE%\nmap-7.95-setup.exe"
set "npcapPath=%USERPROFILE%\npcap-1.79.exe"

REM Debug location
echo Le chemin du fichier Python est: %outputPath%
echo Le chemin du fichier Nmap est: %nmapPath%
echo Le chemin du fichier Nmap est: %npcapPath%

REM Etape 1: Telechargement de python
echo Telechargement de Python ... "
powershell -Command "Invoke-WebRequest -UseBasicParsing -Uri 'https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe' -OutFile '%outputPath%'"

REM 1.1: Verification du telechargement
if exist "%outputPath%" (
echo Le telechargement de Python est reussi !
) else (
echo Erreur: Le fichier n'a pas ete telecharge.
pause
exit /b

)

REM Etape 2: Telechargement de Nmap
echo Telechargement de Nmap ...
powershell -Command "Invoke-WebRequest -UseBasicParsing -Uri 'https://nmap.org/dist/nmap-7.95-setup.exe' -OutFile '%nmapPath%'"

REM 2.1: Verification du telechargement Nmap
if exist "%nmapPath%" (
echo Le telechargement de Nmap est reussi !
) else (
echo Erreur: Le fichier Nmap n'a pas ete telecharge.
pause
exit /b

)

REM Etape 3: Installation de Npcap
echo Telechargement de Npcap
powershell -Command "Invoke-WebRequest -UseBasicParsing -Uri 'https://npcap.org/dist/npcap-1.79.exe' -OutFile '%npcapPath%'"

REM 3.1: Verification du telechargement Npcap
if exist "%npcapPath%" (
echo Le telechargement de Npcap est reussi !
) else (
echo Erreur: Le fichier Npcap n'a pas ete telecharge.
pause
exit /b

)

REM Etape 4: Installation silencieuse de python
echo Installation de Python ...
start "" "%outputPath%" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

REM Etape 5: Installation silencieuse de Npcap
echo Installation de Npcap ...
start "" "%npcapPath%"

REM 6: Temporisation pendant l'installation Npcap
echo Setup Npcap pour l'installation a faire !!
timeout /t 120

REM Etape 7: Installation silencieuse de Nmap
echo Installation de Nmap ...
start "" "%nmapPath%" /s

REM 8: Temporisation pendant l'installation
echo Attente de la fin de l'installation ...
timeout /t 30

REM Verif de version Python
echo Verification de la version de Python
python -- version

pause