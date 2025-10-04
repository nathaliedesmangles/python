+++
title = "Installer un module (ex. Matplotlib) dans Visual Studio Code (MacOS)"
weight = 29
+++

{{% notice style="primary" title="Python et VS Code déjà installés ?" %}}
Vous pouvez aller directement à **l'étape 4**.
{{% /notice %}}


## **Étape 1** : Installer Python sur MacOS

1. Ouvrez Safari et allez sur [https://www.python.org/downloads](https://www.python.org/downloads)
2. Cliquez sur “Download Python” (la version recommandée).
3. Ouvrez le fichier `.pkg` téléchargé et suivez les étapes d’installation.
4. Vérifiez l’installation :
   - Ouvrez **Terminal** (dans Applications > Utilitaires).
   - Tapez : `python3 --version` → vous devriez voir quelque chose comme `Python 3.13.7`.


## **Étape 2** : Installer Visual Studio Code

1. Allez sur [https://code.visualstudio.com](https://code.visualstudio.com)
2. Téléchargez la version Mac et installez-la.
3. Ouvrez VS Code et installez l’extension **Python** :
   - Cliquez sur l’icône des extensions (à gauche, en forme de blocs).
   - Recherchez “Python” et installez celle de **Microsoft**.


## **Étape 3** : Créer un projet Python

1. Créez un dossier sur votre Mac (ex. : `programmation-sciences`)
2. Dans VS Code, allez dans **Fichier → Ouvrir un dossier** et sélectionnez ce dossier.
3. Créez un nouveau fichier : `test.ipynb`


## **Étape 4** : Installer matplotlib (ou autre bibliothèque)

![Matplotlib](../matplotlib.jpg?width=30vw)

1. Dans VS Code, ouvrez le **Terminal intégré** :
   - Menu **Terminal** → **Nouveau terminal**

2. Tapez la commande suivante :
   ```bash
   pip3 install matplotlib
   ```
   - Pour une autre bibliothèque, remplacez `matplotlib` par le nom souhaité (ex. : `numpy`, `pandas`, etc.)


## **Étape 5** : Vérifier l’installation 

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

![NumPy](../numpy.jpg?width=20vw)

1. Dans une cellule, écrire :

   ```python
   import numpy as np
   arr = np.array([1, 2, 3, 4, 5])

   print(arr)
   ```
2. Exécuter le programme (bouton ▶️).
3. Les données entre `[ ]` s'affichent → numpy est bien installé !

**Pandas**

![Pandas](../pandas.jpg?width=30vw)

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
3. Les données tabulaires apparaissent → pandas est bien installé !


---

## Problèmes fréquents

- Si `pip3` ne fonctionne pas, essayez : `python3 -m pip install matplotlib`
- Si vous voyez un message disant que Python n’est pas reconnu, redémarrez votre Mac ou vérifiez que l’installation est bien terminée.
- Pour vérifier que matplotlib est bien installé :
  ```bash
  pip3 show matplotlib
  ```
