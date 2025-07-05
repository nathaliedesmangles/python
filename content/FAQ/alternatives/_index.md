+++
chapter = true
title = "Alternatives à VS Code"
weight = 11
+++

## Deux alternatives populaires

Si vous cherchez une alternative simple et accessible à VS Code avec Jupyter, **Google Colab** est une excellente option. Colab est un environnement de notebooks en ligne gratuit, offert par Google, qui ne nécessite aucune installation. Il vous permet d’écrire et d’exécuter du code Python directement dans votre navigateur, tout en profitant d’un accès facile à des bibliothèques scientifiques populaires comme NumPy, pandas, ou matplotlib. C’est l’outil idéal pour débuter en programmation scientifique ou collaborer à distance, puisqu’il s’intègre à Google Drive et permet de partager vos notebooks aussi facilement qu’un document Google Docs.

De son côté, **PyCharm** est un environnement de développement intégré (IDE) puissant conçu spécialement pour Python. Contrairement à Google Colab, il s’installe sur votre ordinateur, mais offre une panoplie de fonctionnalités avancées comme l’autocomplétion intelligente, le débogueur intégré, et la gestion de projets complexes. Pour les débutants ou les utilisateurs intermédiaires qui souhaitent aller plus loin que les notebooks Jupyter, PyCharm représente une solution robuste et professionnelle. Il existe en version gratuite (Community) et en version payante (Professional) avec essai gratuit.![Google Colab](./colab.png?width=25vw)

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


---

![PyCharm](./pycharm.jpeg?width=25vw)

1. Développé par JetBrains, PyCharm est à ce jour une plateforme très populaire pour Python. Cette plateforme hybride est couramment utilisée pour le développement d’applications Python, et notamment par de grandes entreprises telles que Twitter, Facebook, Amazon ou Pinterest.

2. Compatible avec Windows, Linux et macOS, PyCharm contient des modules et des packages aidant les développeurs à programmer des logiciels avec Python plus rapidement et avec moins d’efforts.

## Installation et configuration

### Télécharger PyCharm

1. Téléchargez PyCharm en cliquant sur le [lien de téléchargement](https://www.jetbrains.com/pycharm/download).

2. Cliquez sur le bouton ***Download***

![Télécharger PyCharm pour Windows](./telecharger.png?width=30vw)

3. Sauvegardez le fichier `.exe` (en date de juin 2025, c'est `pycharm-2025.1.1.1.exe`)

### Installation

- Les instructions varient selon votre système d’exploitation. Pour Windows: 

1. Lancez l'installation en cliquant deux fois sur le fichier `pycharm-2025.1.1.1.exe` téléchargé précédemment.
2. Autorisez l'application
3. Suivez les étapes en cliquant sur ***Next**.
4. Cochez les cases de configuration de PyCharm, puis cliquez sur ***Next***, puis ***Install***
![Options](./options.png?width=40vw)
5. Patientez, le temps que l'installation se fasse6.  (*environ 2-3 minutes*).
6. Redémarrer votre ordinateur. Deux choix possibles:
	1. Choisir l'option ***Reboot now***, puis cliquez sur ***Finish***.
	2. Choisir l'option ***I want to manually reboot later***, pour  redémarrer l'ordinateur plus tard. Cliquez sur ***Finish***.

### Lancer PyCharm

1. Retrouvez l'application PyCharm à l'aide de la loupe **Recherche** sur la barre des tâches
![Chercher PyCharm](./recherche.png?width=15vw)

>Lors du premier lancement de PyCharm, il vous sera demandé de vous connecter à votre compte JetBrains ou de démarrer une évaluation gratuite.

### Écran d’accueil

Lorsque vous ouvrez PyCharm pour la première fois, vous êtes accueilli par l’écran d’accueil.

![Accueil](./accueil.png?width=40vw)

Depuis l’écran d’accueil de PyCharm, vous pouvez explorer cinq sections principales :

1. **Onglet "Learn PyCharm"** : il contient des liens vers la documentation et d'autres ressources. Vous pouvez également vous inscrire à l’outil interactif "Feature Trainer", conçu pour vous enseigner rapidement des astuces de productivité dans PyCharm.

2. **Onglet "Plugins"** : il vous permet d’installer des extensions supplémentaires comme des thèmes personnalisés ou des raccourcis clavier (keymaps), utiles si vous venez d’un autre éditeur ou IDE.

3. **Keymaps** : installer des keymaps facilite la transition depuis d’autres éditeurs. Pour rechercher, commencez à taper "keymaps", par exemple, et PyCharm vous proposera les keymaps disponibles pour les éditeurs les plus populaires. Choisissez celui qui vous convient le mieux et cliquez pour l’installer.

4. **Section "Customize"** : elle vous permet de modifier certains paramètres courants. Par exemple, vous pouvez changer le thème Darcula pour IntelliJ Light. Vous pouvez également synchroniser l’apparence avec celle de votre système d’exploitation. Si vous avez installé un keymap ou un thème, vous devrez les activer ici.

5. **Onglet "Projects"** : c’est ici que vous pouvez créer, ouvrir ou cloner un projet pour commencer à travailler.

### Vidéo sur YouTube

[L'installation en vidéo](https://youtu.be/2EB8siO-_OM)

## Créer un premier projet dans PyCharm.

Pour cette étape, vous pouvez:

- Regarder la vidéo sur YouTube: [vidéo](https://youtu.be/W5p8v4yhxjk)
ou 
- Lire (en anglais) les instruction sur [le site de PyCharm](https://www.jetbrains.com/guide/python/tutorials/getting-started-pycharm/your-first-project/)

## Comprendre l'interface de PyCharm

Pour cette étape, vous pouvez:

- Regarder la vidéo sur YouTube: [vidéo](https://youtu.be/QInZSbPbnnY)
Ou
- Lire le tutoriel sur [le site de PyCharm](https://www.jetbrains.com/guide/python/tutorials/getting-started-pycharm/understanding-the-ui/)

