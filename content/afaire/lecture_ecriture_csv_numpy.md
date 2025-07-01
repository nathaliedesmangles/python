+++
title = "L’écriture et la lecture de données (csv)"
weight = 7
+++


---

# Programmation scientifique en Python — Leçon : Fichiers, Tableaux et Visualisation

## 1. Lire et écrire des fichiers de données (.csv)

Les fichiers `.csv` (Comma-Separated Values) permettent de stocker des tableaux de données.

### Écrire un fichier `.csv`

```python
with open("donnees.csv", "w") as f:
    f.write("Nom,Âge\n")
    f.write("Alice,20\n")
    f.write("Bob,22\n")
```

### Lire un fichier `.csv`

```python
with open("donnees.csv", "r") as f:
    contenu = f.read()
    print(contenu)
```

### Pour des données **numériques**, on peut utiliser `numpy.savetxt()` et `numpy.loadtxt()` :

```python
import numpy as np

# Sauvegarder un tableau
tableau = np.array([[1, 2], [3, 4]])
np.savetxt("tableau.csv", tableau, delimiter=",")

# Charger un tableau
donnees = np.loadtxt("tableau.csv", delimiter=",")
print(donnees)
```


## 2. Tableaux numériques avec **NumPy**

NumPy est une bibliothèque spécialisée pour manipuler efficacement des tableaux.

### Création d’un tableau :

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])
```

### Quelques fonctions utiles :

```python
np.zeros((2, 3))   # tableau 2x3 rempli de 0
np.ones((3, 2))    # tableau 3x2 rempli de 1
np.arange(0, 10, 2) # [0 2 4 6 8]
```


## 3. Opérations sur les tableaux NumPy

Les opérations sont **automatiques** et **élément par élément**.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a * b)   # [4 10 18]
print(a ** 2)  # [1 4 9]
```

Les opérations fonctionnent aussi sur des matrices :

```python
mat = np.array([[1, 2], [3, 4]])
print(mat.T)  # transposée
```

---

## 4. Fonctions statistiques utiles

```python
data = np.array([1, 2, 3, 4, 5])

print(np.sum(data))   # 15
print(np.mean(data))  # 3.0
print(np.std(data))   # 1.41
```


## 5. Graphiques de base avec Matplotlib

```python
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 4, 9])

plt.plot(x, y)        # Tracer y en fonction de x
plt.title("Graphique simple")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
```

Autres types de graphiques :

```python
plt.scatter(x, y)   # Nuage de points
plt.bar(x, y)       # Diagramme à barres
```


## 6. Les instructions conditionnelles


## Résumé des outils par thème

| Thème                   | Fonctions / Notions clés                                |
| ----------------------- | ------------------------------------------------------- |
| Fichiers .csv           | `open()`, `write()`, `read()`, `loadtxt()`, `savetxt()` |
| Tableaux                | `np.array()`, `np.zeros()`, `np.ones()`                 |
| Opérations sur tableaux | `+`, `*`, `.T`                                          |
| Statistiques            | `np.sum()`, `np.mean()`, `np.std()`                     |
| Graphiques              | `plt.plot()`, `plt.scatter()`, `plt.show()`             |
| Conditions              | `if`, `elif`, `else`                                    |

---

Souhaitez-vous que je transforme cette leçon en fichier `.ipynb` (Jupyter Notebook) avec exemples exécutables et sections bien structurées ?
