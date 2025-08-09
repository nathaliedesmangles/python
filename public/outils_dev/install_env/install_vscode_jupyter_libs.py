import subprocess
import sys

def run_cmd(cmd, desc):
    print(f"→ {desc} ...")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        sys.exit(f"Erreur pendant : {desc}")
    print("✔️ Terminé\n")

# 1. Installer Visual Studio Code
run_cmd(["winget", "install", "--id", "Microsoft.VisualStudioCode", "-e", "--source", "winget"], "Installation de Visual Studio Code")

# 2. Mise à jour pip
run_cmd([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], "Mise à jour de pip")

# 3. Installer jupyter, pandas, matplotlib, numpy
run_cmd([sys.executable, "-m", "pip", "install", "notebook", "pandas", "matplotlib", "numpy"], "Installation des bibliothèques Python")
