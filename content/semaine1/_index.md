+++
chapter = true
pre = "<b>1.</b>"
title = " Présentation du cours et l'environnement de travail"
weight = 101
+++

## Objectifs pédagogiques

À la fin de la leçon, vous devrez être en mesure de :

* Comprendre les objectifs du cours et les règlements du collège à respecter (Quiz WooClap)
* Vous connecter à votre compte OneDrive scolaire.
* Créer une structure de dossiers pour le cours.
* Comprendre l'interface de VS Code
* Ouvrir un dossier et un fichier (.ipynb) dans VS Code.
* Créer un fichier `.ipynb` dans VS Code.
* Écrire et exécuter du code Python simple.
* Sauvegarder vos fichiers de code.

---

## 1. Présentation du cours

> [Cliquez ici pour ouvrir le plan de cours et trouver le quiz interactif](../Cours/)

{{%notice style="cyan" title="Réponses se trouvent dans le plan de cours"%}}
Utilisez le **plan de cours** et au besoin les **calendriers scolaires** pour trouver les bonnes réponses aux questions du quiz.
Vous avez **20 minutes** pour répondre à toutes les questions.
{{% /notice%}}

>> Pause 5 minutes

## 2. L'environnement de travail - Activité guidée

### **Étape 1** – Se connecter à votre compte OneDrive du cégep

* ***OneDrive*** est un stockage et synchronisation de fichiers personnels ou scolaires dans le cloud et accessible à partir de n’importe quel emplacement sur n’importe quel appareil. Idéal pour le travail en cours et le partage avec des personnes spécifiques. Les documents sont privés jusqu’à ce que vous les partagez. 

Suivez les étapes sur la page [**Se connecter à OneDrive**](../outils_dev/oneDrive) pour vous connecter à votre compte OneDrive scolaire.

{{%notice style="accent" title="Important"%}}
* À chaque fois que vous accéder à votre poste de travail, assurez-vous que l’icône du nuage est bleue comme ci-dessous : ![OneDrive bleu](./onedrive-bleu.png)
* C’est à vous de veiller à la bonne sauvegarde de vos travaux. En cas de problème, l’enseignante pourra difficilement vous aider, alors soyez vigilants dès le début.
{{% /notice%}}


### **Étape 2** – Organisation des fichiers

{{% notice style="cyan" title="Sachez que.." %}}
Vous pouvez changer les noms des dossiers suggérés, en autant que vous utilisiez des noms représentatifs.
{{% /notice %}}

1. Dans l’explorateur de fichiers (OneDrive), allez dans le dossier `Documents` et créez un sous-dossier nommé `programmation-sciences`.
![Créer nouveau dossier](./gestion_fichiers/creer-dossier.png?width=30vw)

![Créer dossier prog-sciences](./gestion_fichiers/dossier_progsciences.png?width=30vw)

2. Dans ce dossier, créer au moins trois (3) sous-dossiers nommés `semaine01-environnement`, `semaine02-intro-python` et `semaine03-algorithme`.
![Structure semaines](./gestion_fichiers/structure-semaines.png?width=45vw)

3. Allez sur Moodle et téléchargez le fichier `semaine01.ipynb`.
![Moodle](./gestion_fichiers/moodle.png?width=40vw)

4. Allez dans l'**Explorateur de fichiers** et le dossier **Téléchargement**.
![Dossier Téléchargements](./gestion_fichiers/telechargements.png?width=25vw)

Si l'extension (.ipynb) du fichier n'apparait pas, cliquez sur **Afficher**>**Afficher**>**Extensions des noms de fichiers**
![Afficher extensions](./gestion_fichiers/afficher-ext.png?width=40vw)

![Extensions affichées](./gestion_fichiers/extensions-affichees.png?width=20vw)

5. **Déplacez** (**`Ctrl + X`** et **`Ctrl + V`**) ou **glissez-déposez** le fichier `semaine01.ipynb` de **Téléchargements** vers le dossier **semaine01-environnement**.

![Glisser-Déposer](./gestion_fichiers/glisser-deposer.png?width=30vw)

>> Pause 5 minutes

### **Étape 3** – Découverte de VS Code et utilisation d'un bloc-notes Jupyter

Nous allons travailler avec VS Code, un éditeur de code, et comprendre comment ouvrir un dossier de travail avec un fichier présent. Nous allons par la suite créer un fichier qui nous permettra d’écrire du code.

1. Pour ouvrir VS Code, cliquez la **barre de recherche** (loupe) en bas de votre écran, puis écrivez tout simplement **VS**, la première application visible devrait être ***Visual Studio Code***.
![Recherche - Ouvrir VS Code](./vscodejupyter/ouvrir-vs-code.png?width=20vw)

2. Lorsque vous ouvrez VS Code pour la première fois, la page d'accueil devrait s'afficher et proposer différentes actions pour démarrer.

![Accueil VS Code](./vscode-welcome.png?width=50vw)

3. Identifiez les zones principales

![Accueil VS Code](./vscodejupyter/1_interface_vscode.png?width=50vw)

[Description des zones principales](./outils_dev/vs-code/#interface-principale)

4. Sélectionnez l’onglet **Explorateur** sur la barre latérale. 

5. Sélectionner le menu **Fichier > Ouvrir le dossier…**, choisir le dossier **programmation-sciences**

![Ouvrir dossier dans VS Code](./vscodejupyter/ouvrir-le-dossier.png?width=35vw)

{{% notice style="cyan" title="Sachez que.." %}}
Pour ouvrir un dossier vous pouvez aussi aller dans la page d'accueil, cliquer sur le lien **Ouvrir un dossier...**, puis, chercher le dossier à ouvrir:  
![Ouvrir dossier dans VS Code](./vs-code-ouvrir-dossier.png?width=20vw)
{{% /notice %}}

6. Assurez-vous que le fichier téléchargé et déplacé précédemment se trouve dans le sous-dossier `semaine01-environnement`

7. Cliquez sur le nom du fichier pour l'ouvrir dans l'**Éditeur** (à droite).

8. Cliquez sur la flèche à droite de la cellule (pour exécuter le code). Vous devriez voir ceci:

![Bloc-notes ouvert](./vscodejupyter/bloc-notes-ouvert.png?width=50vw)


### **Étape 4** – Créer un nouveau bloc-notes Jupyter

1. Dans l'Explorateur de VS Code, cliquer sur **Nouveau fichier**

2. Nommez-le fichier `premier_notebook.ipynb`.

![Nouveau fichier](./vscodejupyter/nouveau-fichier.png?width=30vw)

![Nouveau notebook](./vscodejupyter/nouveau-notebook.png?width=25vw)

3. Ajoutez un cellule de type Marquage (***Markdown***)

![Aout cellule md](./vscodejupyter/ajout-cell-md.png?width=35vw)


4. Ajoutez le contenu suivant:
   ```markdown
   # Semaine 1 – Environnement de développement
   ## Mon premier bloc-notes

   Nom de l'étudiant.e: 
   ```

![Cellule Markdown](./vscodejupyter/cell-md.png?width=35vw)

5. Ajouter un cellule **Code** (Python) et écrire le commentaire (`#`) et code ci-dessous

![Aout cellule Code](./vscodejupyter/ajout-cell-code.png?width=30vw)

![Cellule Python](./vscodejupyter/cell-code.png?width=30vw)

Puis cliquer sur **Exécuter Tout**.

![Executer tout](./vscodejupyter/exec-tout.png?width=40vw)

6. Sauvegarder avec **Ctrl + S** ou **Fichier > Enregistrer**.

> Le point blanc sur l'onglet du fichier devrai disparaitre.

![Point blanc](./vscodejupyter/point-blanc2.png?width=30vw)

7. Activer la **sauvegarde automatique**, via l'onglet `Fichier`, puis cliquez sur `Enregistrement automatique`.

![Enreg. auto](./vscodejupyter/enregistrement-auto.png?width=35vw)

Vous devriez maintenant voir un crochet à gauche de cette option.

![crochet](./crochet.png?width=30vw)

* Pour ce fichier, VS Code détectera les modifications et fera la sauvegarde automatiquement, mais vous pouvez à tout moment appuyer sur **Ctrl + S** pour forcer la sauvegarde.


8. Créer une nouvelle cellule de code et ajoutez ceci:
   ```python
   3 * (4 + 2)
   ```

9. Assurez-vous que la sauvegarde automatique s'est faite, c'est-à-dire que le point blanc sur l'onglet du fichier a disparu et a été remplacé par un `X`. Ce qui signifie que le fichier est sauvegardé.

![X](./vscodejupyter/X.png?width=30vw)

> Vous pouvez à nouveau cliquer sur **Exécuter tout** pour voir le résultat de la dernière cellule de code.


---

## Bonnes pratiques

1. Organisez bien vos projets :

* Utilisez un **dossier par thème ou par semaine**
* Nommez vos fichiers clairement : `calcul_masse.ipynb`, `analyse_temp.ipynb`

2. La sauvegarde automatique ou sauvegardez régulièrement

3. Fermez les notebooks proprement

* En haut à droite du nom d’un notebook, cliquez sur `X` pour fermer le fichier.

---

## Retour réflexif

* Avez-vous rencontré des problèmes ?
* Qu’est-ce qui vous semble encore flou ?
* Que fait exactement un notebook quand on l’exécute ?

---

## À faire avant le prochain cours

1. Lire la matière sur [Introduction à Python](../semaine2/)
2. Faire les [exercices se trouvant à la fin de la leçon 2](../semaine2/#exercices-à-faire-avant-le-cours)