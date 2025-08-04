import os
import subprocess
import urllib.request
import sys
import shutil

# Téléchargement de l'installateur Python
python_url = "https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"
python_installer = "python_installer.exe"

print("Téléchargement de Python...")
urllib.request.urlretrieve(python_url, python_installer)

# Installation silencieuse de Python
print("Installation de Python...")
subprocess.run([python_installer, "/quiet", "InstallAllUsers=1", "PrependPath=1", "Include_test=0"], check=True)

# Suppression de l'installateur
os.remove(python_installer)

# Installation de VS Code (via winget)
print("Installation de Visual Studio Code...")
subprocess.run(["winget", "install", "--id", "Microsoft.VisualStudioCode", "-e", "--source", "winget"], check=True)

# Mise à jour de pip et installation des bibliothèques
print("Installation des bibliothèques Python...")
subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"], check=True)
subprocess.run(["pip", "install", "notebook", "pandas", "matplotlib", "numpy"], check=True)

print("Installation terminée.")
