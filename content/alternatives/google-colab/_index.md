+++
title = 'Google Colab'
weight = 171
+++

![Google Colab](./colab.png?width=25vw)

**Google Colab**, ou ***Colaboratory***, est un service cloud gratuit proposé par Google, basé sur Jupyter Notebook. Colab permet d'exécuter du code Python directement dans le navigateur sans nécessiter de configuration préalable, tout en offrant un accès gratuit aux processeurs graphiques, pour accélérer les calculs.

## Accéder à Google Colab

Pour commencer à utiliser Google Colab, suivez ces étapes simples :

### **Méthode 1**: Via le site de Google Colab

1. Allez sur le site: [Google Colab](https://colab.research.google.com/).
2. Cliquez sur le bouton **Open Colab**.
3. Si la fenêtre **Ouvrir le notebook** s'ouvre, cliquez sur le bouton **+ Nouveau notebook** pour créer un nouveau notebook. Sinon, une fois sur l'interface de Colab, vous pouvez créer un nouveau notebook en utilisant le menu **Fichier** et en sélectionnant **Nouveau notebook**.

![Nouveau notebook](./nouveau-notebook.png?width=40vw)

![Menu Fichier](./menu-fichier.png?width=40vw)

Les notebooks Colab permettent d'écrire et d'exécuter du code Python. Par exemple, pour exécuter une cellule de code, cliquez dessus et appuyez sur le bouton de lecture ou utilisez le raccourci clavier `Ctrl+Entrée`.

### **Méthode 2**: Via votre compte Google Drive (Si vous en avez un)

1. Ouvrez votre compte **Google Drive**, cliquez sur **Nouveau**, puis sur **Plus** et sélectionnez ***Google Colaboratory***.

![Ouvrir Colab via Google Drive](./drive-colab.png?width=40vw)

## Importer un fichier de l'ordinateur vers Colab

Pour importer un fichier `.ipynb` (notebook Jupyter) ou `.csv` (fichier de données) **depuis votre ordinateur local vers Google Colab**, vous pouvez utiliser l’une des deux méthodes suivantes :

### **Méthode 1** : Utiliser l'interface de Google Colab (plus simple)

#### Pour un fichier `.ipynb` :

1. Va sur [https://colab.research.google.com/](https://colab.research.google.com/)
2. Clique sur l’onglet **"Téléverser"** (Upload).
3. Sélectionne ton fichier `.ipynb` depuis ton ordinateur.

#### Pour un fichier `.csv` :

1. Dans un notebook Colab ouvert, exécute la cellule suivante :

   ```python
   from google.colab import files
   uploaded = files.upload()
   ```
2. Cela ouvrira une boîte de dialogue pour téléverser des fichiers.
3. Une fois le fichier `.csv` téléversé, tu peux l'utiliser comme suit :

   ```python
   import pandas as pd
   df = pd.read_csv('nom_du_fichier.csv')
   df.head()
   ```

### **Méthode 2** : Monter Google Drive et accéder aux fichiers

Si tu veux garder les fichiers disponibles à long terme :

1. Monte ton Google Drive :

   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
2. Accède aux fichiers (ex. un `.csv`) avec un chemin comme :

   ```python
   df = pd.read_csv('/content/drive/MyDrive/chemin/vers/fichier.csv')
   ```

## Utilisation des bibliothèques Python

Colab permet d'utiliser des bibliothèques populaires pour l'analyse et la visualisation des données. Par exemple, pour générer des données aléatoires avec `NumPy` et les visualiser avec `Matplotlib` :

```python
import numpy as np
import matplotlib.pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]
plt.figure(figsize=(10, 6))
plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.show()
```

Les notebooks Colab sont enregistrés dans votre compte Google Drive, ce qui facilite le partage et la collaboration. Vous pouvez partager vos notebooks avec d'autres utilisateurs, qui peuvent les commenter ou les modifier.


## Pour en savoir plus sur Colab

[Lire ce notebook](https://colab.research.google.com/notebooks/intro.ipynb)

