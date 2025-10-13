+++
chapter = true
pre = "<b>12-14</b>"
title = " Projet Enquête ADN - Identifier le coupable"
weight = 112
draft = true
+++


## Objectifs de la séance

* Présentation du projet (généralités)
* Présentation de la partie 1
* Présentation de la grille de correction
* Travailler sur la partie 1


## Fichiers fournis (sur Moodle)

* Les **fichiers CSV complets** (`adn_suspects.csv` et `adn_scene.csv`).
	* Contiennent des **valeurs de données plausibles biologiquement** (en paires de bases).
	* Le **contexte cohérent** pour 10 suspects.
* Le bloc-notes (`projet_ADN.ipynb`) de départ à utiliser.


## Objectifs du projet

### Partie 1 - Préparation des données et identification

* Afficher et nettoyer les données
* Comparer les profils ADN

### Partie 2 - Identification du suspect et visualisation des résultats

**Visualiser les résultats**
   * Identifier le **suspect ayant la plus petite différence moyenne**.
   * Créer un **graphique en barres** comparant les trois loci du coupable et de l’échantillon.
   * Ajouter des **barres d’erreur** simulant l'incertitude expérimentale (±2 pb).
   * Tracer une **régression linéaire** entre les loci du suspect et ceux de la scène.

### Partie 3 - Présentation des résultats

**Communiquer les résultats**

   * Enregistrer dans un fichier texte le nom du coupable et son score de similarité (`resultats_adn.txt`).
   * Mise en forme du bloc-notes (ajout de commentaires pertinents, ).

---

## Contexte 

Une scène de crime a été découverte dans un laboratoire de biologie cellulaire.
Sur une pipette abandonnée, un fragment d’ADN a été trouvé.
Le laboratoire a séquencé **trois loci génétiques** (L1, L2, L3) — des régions variables entre individus.

Les profils ADN de **10 suspects** ont été enregistrés. Cependant, certaines mesures contiennent des **valeurs manquantes** (erreurs d’électrophorèse).
Votre rôle sera de comparer l’ADN trouvé sur la scène à celui des suspects afin d’**identifier le coupable le plus probable**.

## Exemple de données

## Fichier 1 — `adn_suspects.csv`

| Nom     | L1  | L2  | L3  |
| ------- | --- | --- | --- |
| André   | 210 | 320 | 415 |
| Benoit  | 198 | 305 | NaN |
| Chloé   | 205 | 315 | 420 |
| David   | 212 | 318 | 417 |
| Emma    | 208 | NaN | 419 |
| Félix   | 207 | 319 | 415 |
| Gabriel | NaN | 317 | 416 |
| Hugo    | 199 | 312 | 410 |
| Inès    | 215 | 325 | 421 |
| Jade    | 206 | 316 | NaN |

> *Les valeurs représentent des longueurs de fragments d’ADN en paires de bases (pb).*


## Fichier 2 — `adn_scene.csv`

| Echantillon | L1  | L2  | L3  |
| ----------- | --- | --- | --- |
| ADN_trouvé  | 208 | 317 | 418 |





---



## Notions travaillées

| Notion Python                 | Application dans le projet                  |
| ----------------------------- | ------------------------------------------- |
| Lecture/écriture de fichiers  | `pd.read_csv()`, `open()`                   |
| Gestion de données manquantes | `pd.isna()`, `fillna()`                     |
| Boucles et dictionnaires      | Calcul des scores                           |
| NumPy                         | Moyennes, différences absolues, `polyfit()` |
| Matplotlib                    | `bar()`, `errorbar()`, titres, légendes     |
| Régression linéaire           | `np.polyfit()` et `np.polyval()`            |



## Régression linéaire

Pour le coupable présumé, ajoute une **régression linéaire** pour visualiser la correspondance entre les loci du suspect et ceux de la scène :

```python
x = np.array(scene)
y = np.array(suspect)
a, b = np.polyfit(x, y, 1)
plt.plot(x, y, 'o', label='Données')
plt.plot(x, a*x + b, '-', label=f"Régression : y = {a:.2f}x + {b:.2f}")
plt.xlabel("ADN scène (pb)")
plt.ylabel(f"ADN {coupable} (pb)")
plt.legend()
plt.show()
```


## Livrables

* Script ou notebook complet (`projet_adn_prenomNom.ipynb`)
* Graphiques clairs avec titres et légendes
* Fichier `resultats_adn.txt`
* Brève **conclusion écrite** (5 lignes max) :
	* Indiquer qui est le suspect le plus probable et pourquoi ?

## Exemple de code de base

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Lecture des fichiers CSV
suspects = pd.read_csv("adn_suspects.csv")
scene = pd.read_csv("adn_scene.csv").iloc[0, 1:].to_numpy()



# Nettoyage des données (remplir les NaN par les moyennes)
suspects = suspects.fillna(suspects.mean(numeric_only=True))

# Comparaison entre chaque suspect et l'échantillon
scores = {}
for i, row in suspects.iterrows():
    diff = np.abs(row[1:].to_numpy() - scene)
    scores[row["Nom"]] = diff.mean()

# Identifier le suspect le plus proche
coupable = min(scores, key=scores.get)
print("Scores de ressemblance :", scores)
print("Coupable probable :", coupable)

# Graphique comparatif
suspect = suspects[suspects["Nom"] == coupable].iloc[0, 1:].to_numpy()
loci = ["L1", "L2", "L3"]

plt.bar(loci, suspect, yerr=2, label=coupable, alpha=0.6)
plt.bar(loci, scene, yerr=2, label="ADN scène", alpha=0.6)
plt.ylabel("Longueur du fragment (pb)")
plt.title(f"Comparaison ADN : scène vs {coupable}")
plt.legend()
plt.show()

# Sauvegarde du résultat
with open("resultats_adn.txt", "w") as f:
    f.write(f"Coupable probable : {coupable}\n")
    f.write(f"Scores de similarité : {scores}\n")
```


