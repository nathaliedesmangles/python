+++
title = "Installer un module (ex. Matplotlib) dans Visual Studio Code (Windows)"
weight = 28
+++


### 1. Vérifier que Python est installé

1. Clique sur le menu **Démarrer** de Windows.
2. Tape `python` et vérifie qu’il apparaît dans la liste.
3. Si rien n’apparaît → il faut installer Python depuis le site officiel :
   * [https://www.python.org/downloads/windows/](https://www.python.org/downloads/)
   (prendre la dernière version stable, cocher **Add Python to PATH** pendant l’installation).


### 2. Ouvrir Visual Studio Code

1. Lancer **Visual Studio Code**.
2. Ouvrir votre dossier ou fichier `.ipynb` de travail.


### 3. Ouvrir le terminal dans VS Code

1. Dans le menu en haut, cliquer sur **Terminal → Nouveau terminal**.
   (le terminal apparaît en bas de la fenêtre).

![Terminal](./terminal.png?width=40vw)


### 4. Installer matplotlib

![Matplotlib](./matplotlib.jpg?width=30vw)

1. Dans le terminal, taper la commande suivante puis sur **Entrée** :

   ```bash
   pip install matplotlib
   ```
2. Attendre la fin du téléchargement (quelques secondes).
3. Si tout va bien, un message confirme l’installation.

{{% notice style="cyan" title="Autres modules (Numpy, pandas)" %}}
* Vous pouvez faire la même commande pour installer les bibliothèques *NumPy* et *Pandas*.
* Vous pouvez aussi installer les trois bibliothèques en une seule commande:
   ```bash
   pip install matplotlib numpy pandas
   ```
* Pour vérifier les installation, voir le point 5. ci-dessous.
{{% /notice %}}

### 5. Vérifier l’installation 

**Matplotlib**

1. Dans un fichier Python, écrire :

   ```python
   import matplotlib.pyplot as plt

   plt.plot([1, 2, 3], [2, 4, 6])
   plt.show()
   ```
2. Exécuter le programme (bouton ▶️).
3. Le graphique s'affiche → matplotlib est bien installé !

**NumPy**

![NumPy](./numpy.jpg?width=20vw)

1. Dans une cellule, écrire :

   ```python
   import numpy as np
   arr = np.array([1, 2, 3, 4, 5])

   print(arr)
   ```
2. Exécuter le programme (bouton ▶️).
3. Les données entre `[ ]` s'affichent → numpy est bien installé !

**Pandas**

![Pandas](./pandas.jpg?width=30vw)

1. Dans une cellule, écrire :

  ```python
  import pandas as pd

  data = {
    "voiture": ["BMW", "Volvo", "Ford"],
    "annee": [2013, 2017, 2022]
  }

  vehicules = pd.DataFrame(data)

  print(vehicules)
  ```

2. Exécuter le programme (bouton ▶️).
3. Les données tabulaires apparaîssent → pandas est bien installé !

---

## Problèmes fréquents

* **Message "pip n’est pas reconnu"** → Python n’est pas installé correctement ou l’option ***Add to PATH*** a été oubliée → réinstaller Python en cochant cette option.
* **Pas le bon interpréteur Python** → En bas à droite de VS Code, vérifier que c’est bien la version de Python installée.

