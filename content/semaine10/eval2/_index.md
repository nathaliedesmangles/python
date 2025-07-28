+++
title = "Évaluation 2 (25%)"
weight = 108
draft = true
+++





Voici un \*\*examen pratique de 2 heures\*\* conçu pour évaluer les compétences mentionnées. Il comprend \*\*5 questions progressives\*\*, certaines en lien avec des contextes scientifiques, et couvrant \*\*conditions\*\*, \*\*boucles\*\*, \*\*listes\*\*, \*\*chaînes\*\*, et \*\*matplotlib\*\*. Les étudiants peuvent utiliser \*\*VS Code\*\* et \*\*une feuille de notes recto-verso\*\*.



---



\# 🔬 Examen pratique – Programmation Python (durée : 2h)



\*\*Instructions générales :\*\*



\* Répondez directement dans les cellules de code.

\* Nommez le fichier `examen\_prenom\_nom.py`.

\* Commentez brièvement chaque solution pour expliquer votre raisonnement.

\* Sauvegardez vos figures avec `plt.savefig("nom\_de\_fig.png")` si applicable.



---



\## 🌡️ Question 1 – Conditions et science (20 pts)



Un patient subit une série de tests médicaux. Son taux de glucose (en mmol/L) est mesuré. Selon la valeur, une recommandation est donnée :



| Taux de glucose | Recommandation           |

| --------------- | ------------------------ |

| < 4.0           | Risque d'hypoglycémie    |

| 4.0 à 7.0       | Normal                   |

| > 7.0 à 11.0    | Surveillance recommandée |

| > 11.0          | Diabète possible         |

\*\*Écrire un programme qui :\*\*



\* demande à l’utilisateur de saisir son taux de glucose (`float`)

\* affiche la recommandation appropriée à l’aide de `if / elif / else`



---



\## 🔁 Question 2 – Boucles : simulation de dégradation chimique (25 pts)



Une substance radioactive perd 12% de sa masse chaque heure. Écrire un programme qui :



1\. demande la masse initiale (ex. 100 g),

2\. affiche pour chaque heure :



&nbsp;  \* l’heure

&nbsp;  \* la masse restante

3\. s’arrête dès que la masse est inférieure à 10% de la masse initiale.



Utilise une \*\*boucle `while`\*\*, avec un compteur d’heures.



\*\*Exemple de sortie :\*\*



```

Heure 0 : 100.0 g

Heure 1 : 88.0 g

Heure 2 : 77.44 g

...

```



---



\## 🧪 Question 3 – Listes, chaînes et génétique (20 pts)



On analyse une séquence d’ADN représentée par la chaîne :



```python

sequence = "ATGCGATACGCTTGC"

```



1\. Convertis la chaîne en \*\*liste de nucléotides\*\*.

2\. Parcours la liste et compte le \*\*nombre de A, T, G, C\*\*.

3\. Affiche les résultats avec des `f-strings` comme suit :



```

A: 3

T: 4

G: 3

C: 5

```



---



\## 🧩 Question 4 – Listes imbriquées et moyenne de résultats (20 pts)



On analyse des résultats d’expériences. Chaque sous-liste contient les résultats d’un groupe d’étudiants :



```python

groupes = \[\[13, 15, 16], \[12, 18, 20], \[10, 11, 9]]

```



1\. Affiche la moyenne de chaque groupe, arrondie à 2 décimales.

2\. Affiche le plus haut résultat parmi \*\*tous les groupes\*\*.

3\. Transforme tous les résultats inférieurs à 12 en `"Échec"` (modifie la liste en place).



\*\*Exemple de sortie attendue :\*\*



```

Moyenne du groupe 1 : 14.67

Moyenne du groupe 2 : 16.67

Moyenne du groupe 3 : 10.00

Meilleure note tous groupes : 20

Liste modifiée : \[\[13, 15, 16], \[12, 18, 20], \['Échec', 'Échec', 'Échec']]

```



---



\## 📊 Question 5 – Visualisation avec matplotlib (15 pts)



Tu disposes des températures moyennes mensuelles à Montréal (°C) :



```python

mois = \["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Août", "Sep", "Oct", "Nov", "Déc"]

temperatures = \[-9.7, -7.2, -1.2, 6.1, 13.2, 18.3, 21.2, 20.0, 15.3, 8.7, 2.1, -5.3]

```



1\. Crée un graphique avec les mois sur l’axe des x et les températures sur l’axe des y.

2\. Ajoute :



&nbsp;  \* un \*\*titre\*\*

&nbsp;  \* les \*\*noms des axes\*\*

&nbsp;  \* une \*\*grille\*\*

3\. Sauvegarde le graphique sous le nom `temperature\_mtl.png`.



---



\## Barème suggéré (total 100 pts)



| Compétence évaluée                        | Points |

| ----------------------------------------- | ------ |

| Conditions simples et imbriquées          | 20     |

| Boucle `while` (structure, arrêt)         | 25     |

| Listes et chaînes de caractères           | 20     |

| Listes imbriquées, parcours, modification | 20     |

| Visualisation matplotlib                  | 15     |



---



Voici ce que je vais vous fournir maintenant :



---



✅ \*\*1. Corrigé enseignant\*\*

✅ \*\*2. Grille d’évaluation critériée\*\*

✅ \*\*3. Contenu prêt à copier-coller dans un fichier `.ipynb`\*\*

(titres, énoncés, cellules de code, formaté pour distribution aux étudiants)



---



\## 📘 1. Corrigé enseignant



\### Question 1 – Conditions



```python

glucose = float(input("Entrez votre taux de glucose (mmol/L) : "))



if glucose < 4.0:

&nbsp;   print("Risque d'hypoglycémie")

elif glucose <= 7.0:

&nbsp;   print("Normal")

elif glucose <= 11.0:

&nbsp;   print("Surveillance recommandée")

else:

&nbsp;   print("Diabète possible")

```



---



\### Question 2 – Boucle while



```python

masse\_initiale = float(input("Masse initiale (g) : "))

masse = masse\_initiale

heure = 0



while masse >= 0.1 \* masse\_initiale:

&nbsp;   print(f"Heure {heure} : {masse:.2f} g")

&nbsp;   masse \*= 0.88

&nbsp;   heure += 1

```



---



\### Question 3 – Listes et chaînes



```python

sequence = "ATGCGATACGCTTGC"

nucleotides = list(sequence)



print(f"A: {nucleotides.count('A')}")

print(f"T: {nucleotides.count('T')}")

print(f"G: {nucleotides.count('G')}")

print(f"C: {nucleotides.count('C')}")

```



---



\### Question 4 – Listes imbriquées



```python

groupes = \[\[13, 15, 16], \[12, 18, 20], \[10, 11, 9]]



\# Moyennes

for i, groupe in enumerate(groupes):

&nbsp;   moyenne = sum(groupe) / len(groupe)

&nbsp;   print(f"Moyenne du groupe {i+1} : {moyenne:.2f}")



\# Meilleure note

meilleure = max(\[note for groupe in groupes for note in groupe])

print(f"Meilleure note tous groupes : {meilleure}")



\# Remplacement des échecs

for i in range(len(groupes)):

&nbsp;   for j in range(len(groupes\[i])):

&nbsp;       if groupes\[i]\[j] < 12:

&nbsp;           groupes\[i]\[j] = "Échec"



print("Liste modifiée :", groupes)

```



---



\### Question 5 – Graphique matplotlib



```python

import matplotlib.pyplot as plt



mois = \["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Août", "Sep", "Oct", "Nov", "Déc"]

temperatures = \[-9.7, -7.2, -1.2, 6.1, 13.2, 18.3, 21.2, 20.0, 15.3, 8.7, 2.1, -5.3]



plt.plot(mois, temperatures, marker='o', color='blue')

plt.title("Températures moyennes à Montréal")

plt.xlabel("Mois")

plt.ylabel("Température (°C)")

plt.grid()

plt.savefig("temperature\_mtl.png")

plt.show()

```



---



\## 📝 2. Grille d’évaluation critériée



| Compétence               | Critères                                                                  | Points |

| ------------------------ | ------------------------------------------------------------------------- | ------ |

| \*\*Conditions\*\*           | Conditions correctes, bonnes comparaisons, sortie correcte                | /20    |

| \*\*Boucle while\*\*         | Utilisation correcte de la boucle, bon critère d'arrêt, affichage attendu | /25    |

| \*\*Listes et chaînes\*\*    | Conversion correcte, bon comptage, affichage clair                        | /20    |

| \*\*Listes imbriquées\*\*    | Parcours, modification conditionnelle, calculs précis                     | /20    |

| \*\*Graphique matplotlib\*\* | Tracé correct, titres/étiquettes/grille, fichier sauvegardé               | /15    |

| \*\*TOTAL\*\*                |                                                                           | /100   |



---



\## 📦 3. Contenu `.ipynb` pour les étudiants



Voici le contenu \*\*prêt à copier dans un bloc-notes `.ipynb`\*\* :



---



```json

{

&nbsp;"cells": \[

&nbsp; {

&nbsp;  "cell\_type": "markdown",

&nbsp;  "metadata": {},

&nbsp;  "source": \[

&nbsp;   "# 🔬 Examen pratique – Programmation Python\\n",

&nbsp;   "\*\*Durée : 2h\*\* – VS Code + feuille de notes recto-verso autorisés.\\n",

&nbsp;   "\\n",

&nbsp;   "\*\*Instructions :\*\*\\n",

&nbsp;   "- Répondez directement dans les cellules de code ci-dessous.\\n",

&nbsp;   "- Sauvegardez le fichier sous le nom `examen\_nom\_prenom.py`.\\n",

&nbsp;   "- Commentez votre code pour expliquer votre raisonnement.\\n",

&nbsp;   "- Testez vos programmes avec des valeurs pertinentes.\\n"

&nbsp;  ]

&nbsp; },

&nbsp; {

&nbsp;  "cell\_type": "markdown",

&nbsp;  "metadata": {},

&nbsp;  "source": \[

&nbsp;   "## 🌡️ Question 1 – Conditions et science (20 pts)"

&nbsp;  ]

&nbsp; },

&nbsp; {

&nbsp;  "cell\_type": "code",

&nbsp;  "metadata": {},

&nbsp;  "source": \[

&nbsp;   "# Écris un programme qui demande un taux de glucose (mmol/L)\\n",

&nbsp;   "# et affiche une recommandation selon les valeurs suivantes :\\n",

&nbsp;   "# <4.0 → Hypoglycémie / 4-7 → Normal / 7-11 → Surveillance / >11 → Diabète possible\\n",

&nbsp;   "\\n",

&nbsp;   "# Ton code ici :\\n"

&nbsp;  ],

&nbsp;  "execution\_count": null,

&nbsp;  "outputs": \[]

&nbsp; },

&nbsp; {

&nbsp;  "cell\_type": "markdown",

&nbsp;  "metadata": {},

&nbsp;  "source": \[

&nbsp;   "## 🔁 Question 2 – Boucles : dégradation chimique (25 pts)"

&nbsp;  ]

&nbsp; },

&nbsp; {

&nbsp;  "cell\_type": "code",

&nbsp;  "metadata": {},

&nbsp;  "source": \[

&nbsp;   "# Une substance perd 12% par heure. On arrête quand elle atteint moins de 10% de sa masse initiale.\\n",

&nbsp;   "# Affiche l'heure et la masse restante à chaque étape.\\n",

&nbsp;   "\\n",

&nbsp;   "# Ton code ici :\\n"

&nbsp;  ],

&nbsp;  "execution\_count": null,

&nbsp;  "outputs": \[]

&nbsp; },

&nbsp; {

&nbsp;  "cell\_type": "markdown",

&nbsp;  "metadata": {},

&nbsp;  "source": \[

&nbsp;   "## 🧪 Question 3 – Chaînes et listes (20 pts)"

&nbsp;  ]

&nbsp; },

&nbsp; {

&nbsp;  "cell\_type": "code",

&nbsp;  "metadata": {},

&nbsp;  "source": \[

&nbsp;   "# À partir de la chaîne d’ADN suivante, convertis en liste,\\n",

&nbsp;   "# puis compte le nombre de A, T, G, C.\\n",

&nbsp;   "\\n",

&nbsp;   "sequence = \\"ATGCGATACGCTTGC\\"\\n",

&nbsp;   "\\n",

&nbsp;   "# Ton code ici :\\n"

&nbsp;  ],

&nbsp;  "execution\_count": null,

&nbsp;  "outputs": \[]

&nbsp; },

&nbsp; {

&nbsp;  "cell\_type": "markdown",

&nbsp;  "metadata": {},

&nbsp;  "source": \[

&nbsp;   "## 🧩 Question 4 – Listes imbriquées et statistiques (20 pts)"

&nbsp;  ]

&nbsp; },

&nbsp; {

&nbsp;  "cell\_type": "code",

&nbsp;  "metadata": {},

&nbsp;  "source": \[

&nbsp;   "groupes = \[\[13, 15, 16], \[12, 18, 20], \[10, 11, 9]]\\n",

&nbsp;   "\\n",

&nbsp;   "# 1. Affiche la moyenne de chaque groupe\\n",

&nbsp;   "# 2. Affiche la meilleure note de tous les groupes\\n",

&nbsp;   "# 3. Remplace les notes < 12 par \\"Échec\\"\\n",

&nbsp;   "\\n",

&nbsp;   "# Ton code ici :\\n"

&nbsp;  ],

&nbsp;  "execution\_count": null,

&nbsp;  "outputs": \[]

&nbsp; },

&nbsp; {

&nbsp;  "cell\_type": "markdown",

&nbsp;  "metadata": {},

&nbsp;  "source": \[

&nbsp;   "## 📊 Question 5 – Graphique matplotlib (15 pts)"

&nbsp;  ]

&nbsp; },

&nbsp; {

&nbsp;  "cell\_type": "code",

&nbsp;  "metadata": {},

&nbsp;  "source": \[

&nbsp;   "import matplotlib.pyplot as plt\\n",

&nbsp;   "\\n",

&nbsp;   "mois = \[\\"Jan\\", \\"Fév\\", \\"Mar\\", \\"Avr\\", \\"Mai\\", \\"Juin\\", \\"Juil\\", \\"Août\\", \\"Sep\\", \\"Oct\\", \\"Nov\\", \\"Déc\\"]\\n",

&nbsp;   "temperatures = \[-9.7, -7.2, -1.2, 6.1, 13.2, 18.3, 21.2, 20.0, 15.3, 8.7, 2.1, -5.3]\\n",

&nbsp;   "\\n",

&nbsp;   "# Trace un graphique (ligne) avec les températures par mois.\\n",

&nbsp;   "# Ajoute un titre, des noms d’axes, une grille.\\n",

&nbsp;   "# Sauvegarde le graphique sous le nom \\"temperature\_mtl.png\\".\\n",

&nbsp;   "\\n",

&nbsp;   "# Ton code ici :\\n"

&nbsp;  ],

&nbsp;  "execution\_count": null,

&nbsp;  "outputs": \[]

&nbsp; }

&nbsp;],

&nbsp;"metadata": {

&nbsp; "kernelspec": {

&nbsp;  "display\_name": "Python 3",

&nbsp;  "language": "python",

&nbsp;  "name": "python3"

&nbsp; },

&nbsp; "language\_info": {

&nbsp;  "name": "python",

&nbsp;  "version": "3.10"

&nbsp; }

&nbsp;},

&nbsp;"nbformat": 4,

&nbsp;"nbformat\_minor": 5

}

```



