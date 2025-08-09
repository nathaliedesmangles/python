import os
import subprocess
import urllib.request
import sys
import glob
import time

PYTHON_VERSION = "3.13.5"
PYTHON_URL = f"https://www.python.org/ftp/python/{PYTHON_VERSION}/python-{PYTHON_VERSION}-amd64.exe"
PYTHON_INSTALLER = "python_installer.exe"

def download_with_progress(url, filename):
    print(f"Téléchargement de {filename} depuis {url}")
    def progress(block_num, block_size, total_size):
        downloaded = block_num * block_size
        percent = downloaded / total_size * 100 if total_size > 0 else 0
        bar_len = 40
        filled_len = int(bar_len * percent // 100)
        bar = '=' * filled_len + '-' * (bar_len - filled_len)
        print(f"\r[{bar}] {percent:.1f}% ({downloaded}/{total_size} bytes)", end='')
    urllib.request.urlretrieve(url, filename, reporthook=progress)
    print("\nTéléchargement terminé.\n")

def run_cmd(cmd_list, description):
    print(description)
    result = subprocess.run(cmd_list)
    if result.returncode != 0:
        sys.exit(f"❌ Erreur lors de : {description}")
    print("✔️ OK\n")

print(f"== Installation de Python {PYTHON_VERSION} et outils associés ==")

download_with_progress(PYTHON_URL, PYTHON_INSTALLER)

run_cmd([PYTHON_INSTALLER, "/quiet", "InstallAllUsers=1", "PrependPath=1", "Include_test=0"], "Installation silencieuse de Python")

os.remove(PYTHON_INSTALLER)

print("Recherche de Python installé...")
python_paths = glob.glob(r"C:\Program Files\Python3*\python.exe")
if not python_paths:
    python_paths = glob.glob(r"C:\Users\*\AppData\Local\Programs\Python\Python3*\python.exe")

if not python_paths:
    sys.exit("❌ Impossible de trouver l'installation de Python.")

python_exe = python_paths[0]
print(f"Python trouvé : {python_exe}\n")

run_cmd(["winget", "install", "--id", "Microsoft.VisualStudioCode", "-e", "--source", "winget"], "Installation de Visual Studio Code")

run_cmd([python_exe, "-m", "pip", "install", "--upgrade", "pip"], "Mise à jour de pip")
run_cmd([python_exe, "-m", "pip", "install", "notebook", "pandas", "matplotlib", "numpy"], "Installation de Jupyter Notebook et bibliothèques")

print("🎉 Installation terminée avec succès !")
