
import zipfile, os, json, shutil, re
from pathlib import Path
import pandas as pd

ARCHIVE_PATH = "projet_final.zip"
EXTRACTION_DIR = "copies_corrigees"
NOTE_CSV = "corrections.csv"
NOTE_PAR_CRITERE = {
    "Planification": 5,
    "Code fonctionnel": 5,
    "Comparaison ADN": 5,
    "Tableau final": 5,
    "Visualisation": 5,
    "Markdown lettrés": 5,
    "Conclusion critique": 5,
}

if os.path.exists(EXTRACTION_DIR):
    shutil.rmtree(EXTRACTION_DIR)
os.makedirs(EXTRACTION_DIR, exist_ok=True)

with zipfile.ZipFile(ARCHIVE_PATH, "r") as archive:
    archive.extractall(EXTRACTION_DIR)

notebook_paths = list(Path(EXTRACTION_DIR).rglob("*.ipynb"))

def corriger_notebook(nb_path):
    with open(nb_path, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    contenu = "\n".join(cell.get("source", []) if isinstance(cell.get("source", []), list) else [] 
                        for cell in notebook.get("cells", []))

    notes = {}
    notes["Planification"] = NOTE_PAR_CRITERE["Planification"] if "objectif" in contenu.lower() or "étapes" in contenu.lower() else 0
    notes["Code fonctionnel"] = NOTE_PAR_CRITERE["Code fonctionnel"] if "def " in contenu and "lambda" in contenu else 5
    notes["Comparaison ADN"] = NOTE_PAR_CRITERE["Comparaison ADN"] if "comparer" in contenu else 0
    notes["Tableau final"] = NOTE_PAR_CRITERE["Tableau final"] if "match" in contenu.lower() and "mean" in contenu.lower() else 0
    notes["Visualisation"] = NOTE_PAR_CRITERE["Visualisation"] if "plt.bar" in contenu or "matplotlib" in contenu else 0
    nb_cells = notebook.get("cells", [])
    markdowns = [cell for cell in nb_cells if cell.get("cell_type") == "markdown"]
    notes["Markdown lettrés"] = NOTE_PAR_CRITERE["Markdown lettrés"] if len(markdowns) >= 3 else 0
    notes["Conclusion critique"] = NOTE_PAR_CRITERE["Conclusion critique"] if "conclusion" in contenu.lower() or "discussion" in contenu.lower() else 0

    return notes

resultats = []
for path in notebook_paths:
    nom_etudiant = path.parts[-2] if len(path.parts) >= 2 else path.stem
    notes = corriger_notebook(path)
    total = sum(notes.values())
    notes["Nom"] = nom_etudiant
    notes["Total"] = total
    resultats.append(notes)

df_notes = pd.DataFrame(resultats)
df_notes = df_notes[["Nom"] + list(NOTE_PAR_CRITERE.keys()) + ["Total"]]
df_notes.to_csv(NOTE_CSV, index=False)

print(f"Correction terminée. Résultats enregistrés dans : {NOTE_CSV}")
