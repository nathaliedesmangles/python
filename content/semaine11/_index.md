+++
chapter = true
pre = "<b>Semaine 11.</b>"
title = "Lecture/écriture de fichiers texte (CSV)"
weight = 110
+++


## Objectif de la leçon

Apprendre à lire et écrire des fichiers `.csv` (valeurs séparées par des virgules) avec Python pour automatiser le traitement de données scientifiques (ex. : résultats de laboratoire, données expérimentales).

---

## Qu’est-ce qu’un fichier CSV?

* Un fichier texte simple où chaque ligne contient une série de valeurs séparées par des virgules (ou des points-virgules).
* Utilisé pour représenter des tableaux de données : résultats d’expériences, séries de mesures, etc.
* Peut être ouvert avec un tableur comme Excel ou LibreOffice Calc.

**Exemple de fichier `mesures.csv` :**

```
temps,temperature
0,22.5
5,24.1
10,26.3
15,28.0
```

## Lecture de fichier CSV sans module (méthode simple avec *open()*)

```python
with open("mesures.csv", "r") as fichier:
    lignes = fichier.readlines()

for ligne in lignes[1:]:  # Ignorer l’en-tête
    temps, temperature = ligne.strip().split(",")
    print(f"Temps : {temps} min, Température : {temperature} °C")
```

## Écriture de données dans un fichier CSV

```python
with open("resultats.csv", "w") as fichier:
    fichier.write("temps,temperature\n")
    fichier.write("0,22.5\n")
    fichier.write("5,24.1\n")
```

## Bonne pratique : toujours fermer le fichier (ou utiliser *with*)

---
