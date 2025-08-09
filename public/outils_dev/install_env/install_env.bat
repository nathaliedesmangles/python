@echo off
set PYTHON_URL=https://www.python.org/ftp/python/3.13.5/python-3.13.5-amd64.exe
set PYTHON_INSTALLER=python_installer.exe

echo Téléchargement de Python...
powershell -Command "(New-Object Net.WebClient).DownloadFile('%PYTHON_URL%', '%PYTHON_INSTALLER%')"

echo Installation de Python...
%PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

echo Suppression de l'installateur...
del %PYTHON_INSTALLER%

echo Installation de Visual Studio Code...
winget install --id Microsoft.VisualStudioCode -e --source winget

echo Installation des bibliothèques Python...
python -m pip install --upgrade pip
pip install notebook pandas matplotlib numpy

echo Installation terminée.
pause
