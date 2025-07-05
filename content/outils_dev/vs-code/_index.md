+++
pre = "Utilisation de VS Code"
title = " "
weight = 23
+++

![Visual Studio Code](./VsCode.png?width=15vw)

<!--
[![youtube.com/watch?v=maul...](https://images.openai.com/thumbnails/url/KnBhpHicu1mSUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw7JKvbPjMwzzwpNNs4IjrcMDks0SHcPcy4uykku0DWp8AoNrsj2Tq7MzNC1LM4KczdKzcn1CQ6wCHfPd1QrBgAtSiow)](https://www.youtube.com/watch?v=MAuLRELi2YA)
-->

## Installation & premier lancement

### Étapes :

1. Aller sur le site officiel : [https://code.visualstudio.com](https://code.visualstudio.com)
2. Cliquer sur **Download for Windows**
3. Lancer le fichier téléchargé (`VSCodeSetup.exe`)
4. Accepter les conditions → clique sur **Suivant** plusieurs fois
5. Cocher **"Add to PATH"** si disponible
6. Cliquer sur **Installer**
7. Lorsque l'installation est terminée, cliquer sur le raccourci **Visual Studio Code** dans le menu **Démarrer** ou cherche “Visual Studio Code” dans la barre de recherche

> Tu devrais voir l’écran d’accueil (Bienvenue ou *Welcome*) 

![Bienvenue](./welcome.png?width=45vw)

## Interface principale

* **Barre d’activité** (gauche) : accès à l’explorateur, extensions, etc.
* **Volet Explorateur** : tes fichiers/sous-dossiers.
* **Éditeur** : là où tu écris ton code.
* **Barre d’onglets** : navigation entre fichiers ouverts.
* **Terminal intégré** (en bas, pas visible sur l'image).
* **Barre d’état** : info sur format du fichier, erreurs, etc.

![Zones interface](./zones.png?width=40vw)


| **Lettre** | **Nom anglais**    | **En français**             |
| :--------: | ------------------ | --------------------------- |
| A          | *Activity Bar*     | **Barre d’activités**       |
| B          | *Primary Side Bar* | **Volet latéral principal** |
| C          | *Editor Groups*    | **Groupes d’éditeurs**      |
| D          | *Panel*            | **Panneau**                 |
| E          | *Status Bar*       | **Barre d’état**            |

### Barre d’activité 

La **barre d’activité** située à gauche de l'éditeur, est une zone essentielle de l'interface utilisateur. Elle donne accès à plusieurs vues et fonctionnalités importantes. Elle contient les boutons suivants :

* Le bouton **Explorateur** (*Explorer*) vous donne accès au panneau Explorateur, où vos fichiers apparaîtront lorsque vous ouvrirez un dossier.
* Le bouton **Recherche** (*Search*) ouvre le panneau Recherche, où vous pouvez rechercher du texte dans les fichiers d'un dossier ouvert.
* Le bouton **Contrôle de code source** (*Source Control*) ouvre le panneau Contrôle de code source, où vous pouvez suivre les modifications apportées à vos fichiers à l'aide de Git.
* Le bouton **Exécuter et déboguer** (*Run and Debug*) vous donne accès au débogueur VS Code.
* Le bouton **Extensions** ouvre un panneau où l'on peut installer et gérer les extensions de VS Code. Les extensions sont des modules qui ajoutent des fonctionnalités à VS Code.

> En fonction des extensions que vous avez installées, la barre d'activité peut inclure d'autres icônes.

[Vidéo YouTube: Interface de VS Code](https://youtu.be/Ql2ni66uXRc?si=XNz3oc5KV5H4jNFi)


## Ouvrir ou créer un projet

1. **Fichier → Ouvrir un dossier...** (`Ctrl+K Ctrl+O`).
![Ouvrir dosier](./menu-open-folder.png?width=25vw)
2. Crée ou sélectionne un dossier (ex. `mon-projet`), puis clique **Sélectionner un dossier**.
3. Le dossier s’affiche dans l’Explorateur, prêt à être utilisé .


## Créer & éditer des fichiers

* Clique droit sur le volet Explorateur → **Nouveau fichier** → nomme-le (`projet.ipynb`, `script.py`, etc.).
* Le voici ouvert dans l’éditeur.
* Les captures montrent l’éditeur avec du code actif ([4]).

![Créer et éditer fichiers](./creer_editer.png?width=25vw)

## Installation des outils

**Pour ceux qui ont un système d'exploitation Windows, voici deux fichiers exécutables qui installeront automatiquement VS Code, Python et toutes les librairies nécessaires :** 
- [Première étape](1-vscode_python.exe)
- [Deuxième étape](2-libraries_extensions.exe)

**Pour une installation manuelle : voici les liens utiles pour installer les outils de développement (sur votre ordinateur personnel):**

- Télécharger et installer Python : [Python](Python.org)
- Télécharger et installer Visual Studio Code : [Visual Studio Code - Mac, Linux, Windows](https://code.visualstudio.com/download)
- Les **extensions** et **bibliothèques** à installer dans VS Code: Python, Run, Pandas,
Numpy, Matplotlib, SciPy [Tutoriel pour installer des extensions sur VS Code](https://www.youtube.com/watch?v=AUt8NgwMbOo)
- Installer Jupyter Notebook sur Visual Studio Code (en anglais) : [How to Install Jupyter Notebook in VSCode | Jupyter Notebook in Visual Studio Code (Easy)](https://www.youtube.com/watch?v=xS5ZXOC4e6A&t=45s)

### Extensions utiles

* **Python** (Microsoft) : exécution et débogage.
* **Jupyter** : bloc-notes Jupyter.
* **NumPy** : Fonctions mathématiques statistiques.
* **Matplotlib** : Graphiques.
* **SciPy** : Fonctions scientifiques et graphiques (ex: droite de régression linéaire)
* **Pandas** : Traitement de fichiers CSV (extraction et nettoyage des données)

## Astuces clavier & productivité

* **Glisser-déposer** fichiers pour les ouvrir.
* **Commenter** : `Ctrl+/`.
* **Aller à une ligne** : `Ctrl+G`.
* **Formatage** : `Ctrl+K Ctrl+F`.
* **Renommer symboles** : `F2`.
* **IntelliSense** : suggestions automatiques avec `Ctrl+Space` 

---

## Références

* [Tutorial: Get started with Visual Studio Code](https://code.visualstudio.com/docs/getstarted/getting-started?utm_source=chatgpt.com)
* [Interface de VS Code](https://code.visualstudio.com/docs/getstarted/userinterface?utm_source=chatgpt.com)
* [Getting started with Visual Studio Code](https://code.visualstudio.com/docs/introvideos/basics?utm_source=chatgpt.com)  
* [My first VS Code Extension](https://www.reddit.com/r/vscode/comments/og0mo4/snipped_my_first_vs_code_extension_create_fancy/?utm_source=chatgpt.com)
* [Trucs & Astuces](https://code.visualstudio.com/docs/getstarted/tips-and-tricks?utm_source=chatgpt.com)



===========================




## Découverte de l’interface

| Élément           | Description                                    |
| ----------------- | ---------------------------------------------- |
| Barre latérale    | Explorer, Rechercher, Contrôle Git, Extensions |
| Onglet "Explorer" | Voir et ouvrir fichiers/dossiers               |
| Zone centrale     | Éditeur de texte                               |
| Barre du haut     | Onglets des fichiers ouverts                   |
| Terminal intégré  | Accès direct à la ligne de commande            |


## Ouvrir ou créer un fichier ou dossier

### Ouvrir un dossier :

1. Menu **Fichier > Ouvrir un dossier**
2. Choisis le dossier de ton projet

### Créer un fichier :

1. Clique droit dans le panneau Explorer > **Nouveau fichier**
2. Exemple : `script.py` ou `index.html`


## Configurer VS Code pour Python

### Installer Python

1. Va sur [https://python.org](https://python.org) > Télécharge et installe Python
2. Coche **"Add Python to PATH"** avant de cliquer sur "Install Now"

### Installer l’extension Python

1. Dans VS Code, clique sur **Extensions (icône des blocs)** ou `Ctrl+Shift+X`
2. Recherche **Python**
3. Clique sur **Installer** (éditeur : Microsoft)


## Exécuter du code

### Pour un script Python :

1. Ouvre `script.py`
2. Clique sur le bouton **Run ▶️** en haut à droite
3. Ou utilise le raccourci **Ctrl + F5**


## Utiliser le terminal intégré

1. Menu : **Terminal > Nouveau terminal**
2. Tu peux exécuter des commandes comme :

```bash
python script.py
```

ou

```bash
dir
```

(sous Windows)


## Extensions utiles

| Extension          | Pour quoi faire ?                   |
| ------------------ | ----------------------------------- |
| Python (Microsoft) | Exécuter et déboguer du code Python |
| Jupyter            | Ouvrir des notebooks `.ipynb`       |
| Live Server        | Voir tes pages HTML en direct       |
| Prettier           | Formater ton code                   |
| GitLens            | Suivre les modifications dans Git   |


## Personnaliser l’apparence

* Menu : **Fichier > Préférences > Thème de couleur**
* Essaie **"Dark+"**, **"Light"**, ou installe de nouveaux thèmes dans les extensions


## Astuces pour débutants

* Tu peux **glisser-déposer** des fichiers dans VS Code pour les ouvrir
* Le raccourci **Ctrl + /** commente/décommente une ligne
* Sauvegarde souvent avec **Ctrl + S**
* Utilise **Ctrl + P** pour ouvrir rapidement un fichier dans ton projet

