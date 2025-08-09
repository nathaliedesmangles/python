import os
import subprocess
import urllib.request
import sys
import shutil
import glob

# 1. Télécharger Python
python_url = "https://www.python.org/ftp/python/3.13.5/python-3.13.5-amd64.exe"
python_installer = "python_installer.exe"

print("Téléchargement de Python...")
urllib.request.urlretrieve(python_url, python_installer)

# 2. Installer Python
print("Installation de Python...")
subprocess.run([python_installer, "/quiet", "InstallAllUsers=1", "PrependPath=1", "Include_test=0"], check=True)
os.remove(python_installer)

# 3. Trouver le chemin du vrai Python installé
python_paths = glob.glob(r"C:\Program Files\Python3*\python.exe")
if not python_paths:
    python_paths = glob.glob(r"C:\Users\*\AppData\Local\Programs\Python\Python3*\python.exe")

if not python_paths:
    sys.exit("Impossible de trouver l'installation de Python.")

python_exe = python_paths[0]
print(f"Python trouvé : {python_exe}")

# 4. Installer VS Code
print("Installation de Visual Studio Code...")
subprocess.run(["winget", "install", "--id", "Microsoft.VisualStudioCode", "-e", "--source", "winget"], check=True)

# 5. Installer les bibliothèques Python
print("Mise à jour de pip et installation des bibliothèques...")
subprocess.run([python_exe, "-m", "pip", "install", "--upgrade", "pip"], check=True)
subprocess.run([python_exe, "-m", "pip", "install", "notebook", "pandas", "matplotlib", "numpy"], check=True)

print("Installation terminée.")
