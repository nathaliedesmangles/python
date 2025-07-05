+++
title = "exercices préparatoires progressifs"
weight = 112
+++

Parfait ! Voici une **série d’exercices préparatoires progressifs**, organisés par bloc de compétences, pour bien préparer tes étudiant·es au projet ADN.

---

## 🔁 Bloc A – Programmation de base en Python

### 🧪 Exercice A1 — Comparaison de deux séquences

```python
# Complète la fonction pour comparer deux séquences de même longueur.
# Un caractère "?" agit comme un joker qui compte toujours comme une correspondance.

def comparer(seq1, seq2):
    correspondance = 0
    for a, b in zip(seq1, seq2):
        if a == b or a == "?" or b == "?":
            correspondance += 1
    return correspondance / len(seq1) * 100

# Exemple
print(comparer("A?CGT", "AGCGT"))  # Devrait afficher 100.0
```

---

## 📊 Bloc B – Pandas : tableaux et moyennes

### 🧪 Exercice B1 — Créer et analyser un tableau

```python
import pandas as pd

donnees = {
    "Nom": ["Suspect A", "Suspect B", "Suspect C"],
    "Locus_1": [90, 70, 80],
    "Locus_2": [85, 75, 60],
    "Locus_3": [88, 72, 65]
}

df = pd.DataFrame(donnees)

# 1. Ajoute une colonne moyenne
# 2. Trie le tableau par la colonne moyenne, du plus haut au plus bas
```

---

## 📈 Bloc C – Visualisation avec Matplotlib

### 🧪 Exercice C1 — Diagramme à barres

```python
import matplotlib.pyplot as plt

noms = ["A", "B", "C"]
scores = [87, 75, 68]

plt.bar(noms, scores)
plt.title("Score moyen par suspect")
plt.xlabel("Suspects")
plt.ylabel("Pourcentage de correspondance")
plt.show()
```

### 🧪 Exercice C2 — Ajout de barres d’erreur

```python
import numpy as np

incertitudes = [5, 6, 4]

plt.errorbar(noms, scores, yerr=incertitudes, fmt="o", capsize=5)
plt.title("Score moyen avec barres d’erreur")
plt.grid(True)
plt.show()
```

---

## 📐 Bloc D – Régression linéaire avec SciPy

### 🧪 Exercice D1 — Régression entre deux loci

```python
from scipy.stats import linregress

locus1 = [90, 70, 80]
locus2 = [85, 75, 60]

slope, intercept, r, p, std_err = linregress(locus1, locus2)
print(f"Pente : {slope:.2f}, Intercept : {intercept:.2f}, R² = {r**2:.3f}, erreur = {std_err:.2f}")
```

### 🧪 Exercice D2 — Tracer la régression

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array(locus1)
y = np.array(locus2)

plt.plot(x, y, "o", label="Données")
plt.plot(x, slope*x + intercept, "r-", label="Régression")
plt.xlabel("Locus 1")
plt.ylabel("Locus 2")
plt.legend()
plt.title("Régression linéaire entre loci")
plt.grid(True)
plt.show()
```

---

Souhaites-tu :

* 📁 Que je rassemble tous ces exercices dans un **notebook `.ipynb` prêt à remettre** ?
* 📝 Une **fiche d’instructions pour les élèves** avec des zones à compléter ?
* 🧠 Des **exercices de réflexion ou quiz** sur les erreurs fréquentes ?
