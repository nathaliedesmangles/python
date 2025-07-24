+++
title = "Évaluation formative"
weight = 108.3
draft = true
+++

Parfait. Voici un **examen formatif** structuré exactement comme l’examen sommatif, pour que vos étudiant·es puissent s’y préparer efficacement. Il couvre les **mêmes compétences**, avec des énoncés **différents** mais comparables en complexité.

---

# 🧪 Examen formatif – Programmation Python

**Durée suggérée : 2h – VS Code + 1 feuille de notes autorisée**

---

## 🌬️ Question 1 – Conditions et météo (20 pts)

On veut interpréter un indice de qualité de l’air (IQA) selon les valeurs suivantes :

| IQA     | Interprétation         |
| ------- | ---------------------- |
| < 50    | Bon                    |
| 50–100  | Modéré                 |
| 101–150 | Mauvais pour sensibles |
| > 150   | Mauvais pour tous      |

**Écris un programme qui :**

* Demande un IQA à l’utilisateur (`int`)
* Affiche l’interprétation à l’aide d’une structure `if / elif / else`.

---

## 🧬 Question 2 – Boucle while : reproduction bactérienne (25 pts)

Une colonie de bactéries double toutes les heures. Écrire un programme qui :

1. demande une population initiale (ex. 100),
2. affiche pour chaque heure :

   * l’heure
   * la population
3. s’arrête dès que la population atteint ou dépasse 10 000.

Utilise une **boucle `while`** avec compteur d’heures.

---

## 🧫 Question 3 – Chaînes et protéines (20 pts)

Un laboratoire reçoit la chaîne d’un peptide représentée par des lettres (acides aminés) :

```python
peptide = "AGWTVAGTWVAG"
```

1. Convertis la chaîne en liste.
2. Compte le nombre d’occurrences de **chaque lettre unique** (tu peux utiliser `.count()`).
3. Affiche les résultats comme suit (ordre non important) :

```
A: 3
G: 3
W: 2
T: 1
V: 2
```

---

## 🧪 Question 4 – Moyennes de résultats expérimentaux (20 pts)

Résultats de plusieurs séries d’essais :

```python
resultats = [[8, 14, 16], [19, 12, 17], [11, 10, 12]]
```

1. Affiche la moyenne de chaque série.
2. Affiche la **plus petite valeur** parmi tous les résultats.
3. Remplace toutes les valeurs supérieures à 15 par `"Haut"`.

---

## 📈 Question 5 – Graphique de pH selon le volume de base (15 pts)

Lors d’un titrage, on mesure le pH à différents volumes de base ajoutée :

```python
volumes = [0, 5, 10, 15, 20, 25, 30, 35]
pH =      [2.5, 3.0, 3.8, 4.5, 6.8, 9.2, 11.0, 12.5]
```

1. Trace un graphique ligne entre les volumes (x) et le pH (y).
2. Ajoute un titre, un nom aux axes et une grille.
3. Sauvegarde sous le nom `courbe_titrage.png`.

---

## 📋 Barème suggéré

| Compétence               | Points  |
| ------------------------ | ------- |
| Conditions (IQA)         | 20      |
| Boucle `while`           | 25      |
| Chaînes/listes (peptide) | 20      |
| Listes imbriquées        | 20      |
| Graphique matplotlib     | 15      |
| **Total**                | **100** |

