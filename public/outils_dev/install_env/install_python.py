import urllib.request
import subprocess
import os
import sys
import winreg

PYTHON_VERSION = "3.13.5"
PYTHON_URL = f"https://www.python.org/ftp/python/{PYTHON_VERSION}/python-{PYTHON_VERSION}-amd64.exe"
INSTALLER = "python_installer.exe"

print(f"Téléchargement de Python {PYTHON_VERSION}...")
urllib.request.urlretrieve(PYTHON_URL, INSTALLER)
print("Téléchargement terminé.")

print("Installation silencieuse de Python (avec pip et ajout au PATH)...")
result = subprocess.run([INSTALLER, "/quiet", "InstallAllUsers=1", "PrependPath=1", "Include_test=0"], check=False)

if result.returncode == 0:
    print("Installation terminée avec succès.")
else:
    print(f"Erreur lors de l'installation, code {result.returncode}")
    sys.exit(1)

os.remove(INSTALLER)


def prepend_to_system_path(new_path):
    # Ouvrir la clé de registre Path système
    reg_path = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
    with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
        with winreg.OpenKey(hkey, reg_path, 0, winreg.KEY_READ) as env_key:
            old_path, _ = winreg.QueryValueEx(env_key, "Path")

    # Nettoyer les entrées
    path_parts = [p.strip() for p in old_path.split(';') if p.strip() and p.strip().lower() != new_path.lower()]
    # Insérer le nouveau chemin en tête
    path_parts.insert(0, new_path)

    new_path_value = ';'.join(path_parts)

    # Écrire la nouvelle valeur dans le registre
    with winreg.OpenKey(hkey, reg_path, 0, winreg.KEY_SET_VALUE) as env_key:
        winreg.SetValueEx(env_key, "Path", 0, winreg.REG_EXPAND_SZ, new_path_value)

    # Notifier le système de la modification d'environnement (optionnel)
    subprocess.run('setx PATH "{}" /M'.format(new_path_value), shell=True)

    print("✅ PATH système mis à jour avec", new_path)

# Exemple d’utilisation après installation Python
python_install_path = r"C:\Program Files\Python313"

prepend_to_system_path(python_install_path)
print("Redémarrez la session pour que la modification soit prise en compte.")

