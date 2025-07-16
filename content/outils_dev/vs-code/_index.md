+++
pre = "Utilisation de VS Code"
title = " "
weight = 23
+++

![Visual Studio Code](./VsCode.png?width=15vw)

## Installation & premier lancement

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

![Zones interface](./zones.png?width=45vw)


| **Lettre** | **En français**             |
| :--------: | --------------------------- |
| A          | **Barre d’activités**       |
| B          | **Volet latéral principal** |
| C          | **Groupes d’éditeurs**      |
| D          | **Panneau**                 |
| E          | **Barre d’état**            |

### Barre d’activité 

La **barre d’activité** située à gauche de l'éditeur, est une zone essentielle de l'interface utilisateur. Elle donne accès à plusieurs vues et fonctionnalités importantes. Elle contient les boutons suivants :

* <p>Le bouton <strong>Explorateur</strong> (<em>Explorer</em>)<img src="./explorer-icon.png" alt="Explorer" width="30" height="30"> vous donne accès au panneau Explorateur, où vos fichiers apparaîtront lorsque vous ouvrirez un dossier.</p>

* <p>Le bouton <strong>Recherche</strong> (<em>Search</em>)<img src="./search-icon.png" alt="Search" width="30" height="30"> ouvre le panneau Recherche, où vous pouvez rechercher du texte dans les fichiers d'un dossier ouvert.</p>

* <p>Le bouton <strong>Contrôle de code source</strong> (<em>Source Control</em>)<img src="./source-control-icon.png" alt="Source Control" width="30" height="30"> ouvre le panneau Contrôle de code source, où vous pouvez suivre les modifications apportées à vos fichiers à l'aide de Git.</p>

* <p>Le bouton <strong>Exécuter et déboguer</strong> (<em>Run and Debug</em>)<img src="./run-debug-icon.png" alt="Run and Debug" width="30" height="30"> vous donne accès au débogueur VS Code.</p>

* <p>Le bouton <strong>Extensions</strong><img src="./extensions-icon.png" alt="Extensions" width="30" height="30"> ouvre un panneau où l'on peut installer et gérer les extensions de VS Code. Les extensions sont des modules qui ajoutent des fonctionnalités à VS Code.</p>

> En fonction des extensions que vous avez installées, la barre d'activité peut inclure d'autres icônes.

[Vidéo YouTube: Interface de VS Code](https://youtu.be/Ql2ni66uXRc?si=XNz3oc5KV5H4jNFi)

## Personnaliser l’apparence

* Menu : **Fichier > Préférences > Thème de couleur**
* Essaie **"Dark+"**, **"Light"**, ou installe de nouveaux thèmes dans les extensions

## Ouvrir ou créer un projet

1. **Fichier → Ouvrir un dossier...** (`Ctrl+K Ctrl+O`).
![Ouvrir dossier](./menu-open-folder.png?width=25vw)
2. Crée ou sélectionne un dossier, puis clique **Sélectionner un dossier**.
3. Le dossier s’affiche dans l’Explorateur de VS Code, prêt à être utilisé .

## Créer & éditer des fichiers

1. Sélectionner la vue Explorateur dans la **barre d’activité** et sélectionner le bouton **Nouveau fichier...** pour créer un nouveau fichier dans votre espace de travail.
2. Saisissez le nom du fichier et appuyez sur **Entrée**.
	* Un fichier est ajouté à votre espace de travail et un éditeur s'ouvre dans la zone principale de la fenêtre.

![Créer et éditer fichiers](./explorer-new-file.png?width=50vw)

## Exécuter du code

Pour un script Python ou un bloc-notes Jupyter :

1. Ouvre `script.py` ou `script.ipynb`
2. Clique sur le bouton **Run ▶️** en haut à droite ou utilise le raccourci **Ctrl + F5**

![Exécuter](./execution-python.png?width=40vw)

## Installer et configurer VS Code pour Python

### 1. Installation de VS Code

**Pour ceux qui ont un système d'exploitation Windows, voici deux fichiers exécutables qui installeront automatiquement VS Code, Python et toutes les librairies nécessaires :** 
- [Première étape](1-vscode_python.exe)
- [Deuxième étape](2-libraries_extensions.exe)

**Pour une installation manuelle : voici les liens utiles pour installer les outils de développement (sur votre ordinateur personnel):**

- Télécharger et installer Python : [Python](Python.org)
- Télécharger et installer Visual Studio Code : [Visual Studio Code - Mac, Linux, Windows](https://code.visualstudio.com/download)
- Les **extensions** et **bibliothèques** à installer dans VS Code: Python, Run, Pandas,
Numpy, Matplotlib, SciPy [Tutoriel pour installer des extensions sur VS Code](https://www.youtube.com/watch?v=AUt8NgwMbOo)
- Installer Jupyter Notebook sur Visual Studio Code (en anglais) : [How to Install Jupyter Notebook in VSCode | Jupyter Notebook in Visual Studio Code (Easy)](https://www.youtube.com/watch?v=xS5ZXOC4e6A&t=45s)


### 2. Installer Python

1. Va sur [https://python.org](https://python.org) > Télécharge et installe Python
2. Coche **"Add Python to PATH"** avant de cliquer sur "Install Now"

### 3. Installer l’extension Python

1. Dans VS Code, clique sur **Extensions (icône des blocs)** ou `Ctrl+Shift+X`
2. Recherche **Python**
3. Clique sur **Installer** (éditeur : Microsoft)


#### Extensions utiles

* **Python** (Microsoft) : exécution et débogage.
* **Jupyter** : bloc-notes Jupyter.
* **NumPy** : Fonctions mathématiques statistiques.
* **Matplotlib** : Graphiques.
* **SciPy** : Fonctions scientifiques et graphiques (ex: droite de régression linéaire)
* **Pandas** : Traitement de fichiers CSV (extraction et nettoyage des données)

## Astuces clavier & productivité

* **Glisser-déposer** fichiers pour les ouvrir.
* **Sauvegarde** souvent avec **Ctrl + S**
* **Commenter/décommenter une ligne** : `Ctrl+/`.
* Utilise **Ctrl + P** pour ouvrir rapidement un fichier dans ton projet
* **Aller à une ligne** : `Ctrl+G`.
* **Formatage** : `Ctrl+K Ctrl+F`.
* **Renommer symboles** : `F2`.
* **IntelliSense** : suggestions automatiques avec `Ctrl+Space` 



---

## Références

* [Tutorial: Get started with Visual Studio Code](https://code.visualstudio.com/docs/getstarted/getting-started)
* [Interface de VS Code](https://code.visualstudio.com/docs/getstarted/userinterface)
* [Getting started with Visual Studio Code](https://code.visualstudio.com/docs/introvideos/basics)  
* [Trucs & Astuces](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)