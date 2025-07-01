+++
title = "Prise en main de l'outil informatique"
weight = 10
+++


## Objectifs pédagogiques

- Apprendre à s'organiser pour le cours
- Se connecter et utiliser **OneDrive**
- Créer une structure de dossiers pour le cours
- Télécharger un fichier, le retrouver et le placer dans le bon dossier
- Prendre en main **VS Code** et **Jupyter Notebook**
- Activez l'extension des fichiers

## 1. Se connecter à OneDrive
1. **Ouvrir OneDrive :**
- Cliquez sur la petite flèche en bas à droite de l'écran (dans la barre de menu).
- Si l'icone de **OneDrive** ressemble à celle-ci, c'est que vous n'est pas connecté.
![alt text](<Capture d’écran du 2024-08-17 13-28-32.png>)
- Si l'icone est comme la suivante, c'est que vous êtes connecté.
   - Assurez-vous que vous êtes bien conencté à votre compte du collège.
   - Dans ce cas, passez à l'étape suivante.

{{%notice style="warning" title="Attention"%}}
**IMPORTANT :** Au risque de perdre tous les travaux que vous êtes en train d'effectuer, vous devez en tout temps et à chaque fois que vous accéder à votre poste de travail, vérifier et vous assurer que l’icône du nuage est bleue comme ci-dessous : ![alt text](<Capture d'écran 2025-05-30 173548.png>)
C’est à vous de veiller à la bonne sauvegarde de vos travaux. En cas de problème, l’enseignant pourra difficilement vous aider, alors soyez vigilants dès le début.
{{% /notice%}}

2. **Connexion à OneDrive :**
- Cliquez sur l'icone du nuage, une fenêtre de connexion s'ouvrira. Entrez votre adresse email associée à votre compte Microsoft et cliquez sur ***Se connecter***.
- Suivez les instructions pour entrer votre mot de passe et configurer votre compte.
![alt text](<Capture d’écran du 2024-08-17 13-29-04.png>)

## 2. Création d'un dossier pour le cours
- Vous pouvez ouvrir votre dossier **OneDrive**.
![alt text](<Capture d'écran 2025-05-30 174517.png>)
- En utilisant le bouton de droite de la souris, cliquez dans l'espace de droite (vous devriez avoir une page blanche).
![alt text](<Capture d’écran du 2024-08-17 13-35-40.png>)
- Nommez ce nouveau dossier avec le nom suivant : ***Programmation en sciences***.
![alt text](<Capture d'écran 2025-05-30 182644.png>)
- Double-cliquez sur ce nouveau dossier puis créez 6 sous-dossiers avec les noms suivants :
   - ***Semaine 1***
   - ***Semaine 2***
   - ***Semaine 3***
   - ...

## 3. Télécharger et déplacer un fichier dans le répertoire ***Semaine 1***

Vous allez manipuler de nombreux fichiers qui devront être placés dans les bons répertoires afin de ne pas vous perdre dans vos travaux. Pour cela, nous allons faire un premier exemple afin de prendre en main les bases du téléchargement et de la copie d'un fichier sur **Windows**.

Cliquez **une fois** sur le fichier ci-après : [**Premier fichier**](premier_fichier_python.ipynb)

Vous remarquez l'ouverture d'une petite fenêtre en haut à droite de votre écran, cliquez sur le petit dossier présent à droite du nom du fichier :

![alt text](<Capture d'écran 2025-05-30 184345.png>)

{{%notice style="note" title="Note"%}}
Il est possible que ce soit légèrement différent pour vous en fonction du navigateur utilisé (Microsoft Edge, Google Chrome...). L'exemple ci-dessus est montré à partir du navigateur Firefox, le principe reste le même.
{{%/notice%}}

{{%notice style="warning" title="Attention"%}}
Plus vous cliquez sur **Premier Fichier**, plus il se télécharge et se duplique. Exemple d'un cas où vous cliquez plusieurs fois sur le fichier :
![alt text](<Capture d'écran 2025-05-30 185120.png>)

Comment procéder ?

Lorsque vous êtes dans le répertoire ***Téléchargements***, supprimez directement les fichiers dupliquées en faisant un clic gauche pour sélectionner le fichier puis un clic droit sur la même ligne puis cliquer sur **Supprimer** :

![alt text](<2025-05-30 19_15_57-Semaine 1 _ Explorateur de fichiers.png>)


{{%/notice%}}

L'explorateur de fichier s'est automatiquement ouvert dans le dossier ***Téléchargements***. Nous allons déplacer le fichier pour le mettre dans notre répertoire ***Semaine 1***.

- Faites un clic gauche sur le fichier pour le sélectionner
- Sur la même ligne, faites un clic droit puis cliquer sur **Couper**

![alt text](<2025-05-30 18_59_33-Semaine 1 _ Explorateur de fichiers.png>)

- A partir de l'explorateur de fichier, naviguez vers le dossier de votre OneDrive - ***Semaine 1*** :

![alt text](<2025-05-30 19_03_18-Exercice SN _ Explorateur de fichiers.png>)

- Lorsque vous êtes dans votre répertoire ***Semaine 1***, faites un clic droit dans le dossier puis faites **Coller** :

![alt text](<2025-05-30 19_06_28-Semaine 1 _ Explorateur de fichiers.png>)

{{%notice style="note" title="Attention"%}}
Vous allez devoir répéter cette manipulation de nombreuses fois pendant ce cours. Il est très important de la maîtriser.
{{%/notice%}}

Votre dossier doit ressembler à ça :

![alt text](<Capture d'écran 2025-05-31 122342.png>)

## 4. Ouvrir un dossier de travail qui est sur OneDrive

Nous allons travailler avec **VS Code** et comprendre comment ouvrir un dossier de travail avec un fichier présent. Nous allons par la suite créer un fichier qui nous permettra d'écrire du code.

Pour ouvrir **VS Code**, cliquez la barre de recherche en bas de votre écran, puis écrivez tout simplement **VS**, le premier logiciel visible devrait être **Visual Studio Code**.

1. **Ouvrir un dossier dans VS Code :**
   - Sélectionnez l'onglet **Explorateur** sur la barre latérale de gauche. Et ensuite `Ouvrir le dossier`.
   ![alt text](<Capture d’écran du 2024-08-17 15-47-41.png>)
   - Sélectionnez votre dossier OneDrive, puis ouvrez le dossier que vous avez créé précédemment.
   ![alt text](<Capture d’écran du 2024-08-17 15-49-28.png>)
   - Cliquez sur `Sélectionner un dossier`
   ![alt text](<Capture d’écran du 2024-08-17 13-45-12-1.png>)

   Il est normal de ne pas voir vos fichiers lorsque vous sélectionnez un dossier de travail.

   Une fois le dossier ouvert, vous devriez voir le fichier sur **VS Code** dans la partie gauche de votre explorateur de fichier.
   ![alt text](<Capture d'écran 2025-05-31 141823.png>)
   

   Un simple clic gauche vous permet d'ouvrir votre fichier.

   Voilà ! Votre environnement de travail est créé et vous avez réussi à ouvrir votre premier fichier sur **VS Code**

   Nous allons maintenant voir comment créer un fichier à partir du même dossier.   

## 5. Créer un premier fichier `.ipynb`
1. **Créer un fichier Jupyter Notebook :**
   - Cliquez sur l'icône suivante pour créer un nouveau fichier :
   ![alt text](<Capture d'écran 2025-05-31 141320.png>)
   - Nommez le fichier avec l'extension `.ipynb` (par exemple, `deuxieme_fichier_python.ipynb`) et appuyez sur la touche de votre clavier **Entrée**.
   ![alt text](<Capture d'écran 2025-05-31 142138.png>)
   - Le fichier s'ouvrira automatiquement dans l'éditeur **Jupyter** de **VS Code** (fenêtre à droite), où vous pourrez commencer à écrire et exécuter du code **Python**.
   - Cliquez simplement sur l'icône **+ Code** pour créer une cellule.
   ![alt text](<Capture d'écran 2025-05-31 142255.png>)

   Si vous avez créé trop de cellule et que vous voulez les supprimer, positionnez vous sur la cellule et cliquez sur la corbeille tout à droite :
   ![alt text](<2025-05-31 14_47_38-deuxième_fichier_python.png>)
   

## 6. Écrire un premier programme
  - Dans la fenêtre de droite, écrivez `print("Bonjour!")` dans le premier encadré.
  - Appuyez sur le button "Jouer" pour exécuter le code.
      - Vous pouvez alternativement appuyer sur les touches `Ctrl+Entrée` pour lancer l'exécution d'un bloc de code.
  ![alt text](<2025-05-31 14_49_45-deuxième_fichier_python.png>)

## 7. Activation de l'enregistrement automatique

L'avantage de l'enregistrement automatique est qu'à chaque fois que vous saisirez du code ou du texte dans vos fichiers **Jupyter Notebook**, ils s'enregistreront automatiquement.

   - Cliquez sur **Fichier** en haut à gauche de votre **VS Code**, puis cochez **Enregistrement automatique** comme sur l'image ci-dessous
   ![alt text](<Capture d'écran 2025-05-31 165838.png>)

## 8. Activer l'extension des fichiers cachés
   - Une extension de nom de fichier vous permet de savoir quel est le type du fichier. L'extension de nom de fichier est situé après le `.` de votre nom de fichier :
      - `.docx` va correspondre à des fichiers **Word**
         
         Ex : remise_projet.**docx**
      - `.xlsx` pour des fichiers **Excel**

         Ex : atelier_chimie.**xlsx**
      - `.ipynb` pour des fichier **Jupyter Notebook**

         Ex : premier_programme.**ipynb**

   - A date, vous ne les voyez pas dans vos dossiers, c'est pourquoi vous allez les activer avec la manipulation suivante :
   ![alt text](<2025-05-31 14_40_02-Prise en main de l'outil informatique.png>)
   
## 9. Prise en main de Safe Exam Browser

La majorité de vos tests vont s'effectuer sur Moodle à l'aide de Safe Exam Browser. Nous allons faire un premier test pour que vous puissiez prendre en main cet outil et être à l'aise le jour de votre premier test.
   - Ouvrez un navigateur web et rendez vous sur le site **[Moodle](https://cmontmorency.moodle.decclic.qc.ca/login/index.php)** du collège.
   - Vos identifiants se trouvent sur la lettre d'admission que vous avez reçue sur le site **colnet**.
   - Connectez vous puis rendez vous sur le site du cours à la **semaine 1**.
   - Ouvrez le **quiz** et faites-le. Aucun stress, ce n'est absolument pas noté!

{{%notice style="note" title="Note"%}}
**Safe Exam Browser** peut prendre un peu de temps à s'exécuter. Dans le cas où rien ne s'ouvre, appelez-moi et nous verrons ça ensemble.
{{%/notice%}}

