+++
chapter = true
pre = "8."
title = " Tableaux NumPy et droite de régression"
weight = 108
draft = false
+++


## Objectifs

* Comprendre ce qu’est NumPy et pourquoi il est utile en sciences.
* Apprendre à créer et manipuler des tableaux NumPy.
* Utiliser NumPy pour traiter des données scientifiques et faire des calculs rapides.
* Modéliser une relation entre deux données à l'aide d'une droite de régression linéaire.

## Fichier .ipynb pour la démo en classe

[Fichier utilisé pour la démonstration](./blocnotes/demo_numpy_reg.ipynb)

---

{{% notice style="accent" title="Apprendre par la pratique" %}}
- Faites les exercices en vous aidant des notes de cours ci-dessous.  
- Certains seront faits en classe à titre de démonstration.  
- Les solutions seront disponibles à la fin de la semaine prochaine.
{{% /notice %}}

---

## Fichier de départ à utiliser

1. Cliquez sur le lien pour télécharger le fichier : [Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_numpy.ipynb)  
2. Enregistrez-le dans votre dossier **exercices** de la semaine en cours.  
3. Ouvrez **Visual Studio Code**.  
4. Recherchez et ouvrez le fichier `exercices_numpy.ipynb`.  
5. Assurez-vous que le noyau Python (`Kernel`) soit sélectionné.  
6. Vous pouvez commencer les exercices.

---

# Exercices

### Exercice 1 : Chute libre verticale et régression linéaire

Un objet est lâché d’une hauteur **h = 20 m** sans vitesse initiale.  
La formule de la position est :
```math
$$ y(t) = h - \frac{1}{2} g t^2 $$
```
avec $ g = 9.8 m/s^2 $

1. Importez NumPy et Matplotlib.  
2. Définissez les constantes `g` et `h`.  
3. Créez un tableau `t` de 0 à 2 secondes avec 21 valeurs (`np.linspace(0, 2, 21)`).  
4. Calculez la position `y` avec la formule ci-dessus.  
5. Affichez les **5 premières valeurs** de `y` (`y[:5]`).  
6. Tracez le graphique de la position (`plt.plot(t, y)`).  
7. Ajoutez une **droite de régression linéaire** sur la portion `0.5 ≤ t ≤ 1.5` :  
	* masque = (t >= 0.5) & (t <= 1.5)
	* coef = np.polyfit(t[masque], y[masque], 1)
	* droite = np.polyval(coef, t)
	* plt.plot(t, droite)

**Résultats** :
```
5 premières valeurs de y : [20.    19.951 19.804 19.559 19.216]
```
![Graphique 1](./graphe_exo1.png?width=35vw)

### Exercice 2 : Mouvement rectiligne uniforme et régression linéaire

Une voiture roule à vitesse constante **v = 15 m/s**. Sa position est donnée par :

$$
x(t) = v \cdot t
$$

1. Définissez la vitesse constante (`v = 15`).  
2. Créez un tableau `t` allant de 0 à 10 s avec un pas de 0.5 (`np.arange(0, 10.5, 0.5)`).  
3. Calculez la position `x`.  
4. Affichez la **dernière valeur** (`x[-1]`).  
5. Tracez la position en fonction du temps.  
6. Ajoutez une **droite de régression linéaire** pour vérifier la relation proportionnelle.

**Résultats** :
```
Dernière position : 150.0
```
![Graphique 2](./graphe_exo2.png?width=35vw)

### Exercice 3 : Énergie cinétique et barres d’erreur

La formule de l'énergie cinétique est :

$$
E_c = \frac{1}{2} m v^2
$$

Un objet de masse **m = 2.0 kg** accélère de 0 à 20 m/s.

1. Créez un tableau `v` de 0 à 20 avec un pas de 2 (`np.arange`).  
2. Calculez `Ec`.  
3. Affichez les énergies calculées.  
4. Vérifiez la valeur maximale avec `np.max(Ec)`.  
5. Affichez les **3 dernières valeurs** et la **sous-plage 2–8 m/s**.  
6. Tracez un **graphique à barres** avec **barres d’erreur** (±5%).  
	* erreurs = 0.05 * Ec
	* plt.bar(v, Ec, yerr=erreurs)

**Résultats** :
```
Énergies : [  0.   4.  16.  36.  64. 100. 144. 196. 256. 324. 400.]
Max : 400.0
Trois dernières : [256. 324. 400.]
Vitesses 2–8 : [2 4 6 8]
Énergies : [ 4. 16. 36. 64.]
```
![Graphique 3](./graphe_exo3.png?width=35vw)

### Exercice 4 : Oscillations harmoniques

La position d’un oscillateur est donnée par :

$$
x(t) = A \cos(\omega t)
$$

avec $A = 0.1 \, m$ et $\omega = 2 \pi \, rad/s$

1. Créez un tableau `t` de 0 à 2 s avec 101 valeurs (`np.linspace`).  
2. Calculez `x`.  
3. Trouvez les valeurs extrêmes (`np.max`, `np.min`).  
4. Tracez le graphique de l’oscillation.

**Résultats** :
```
Max : 0.1
Min : -0.1
```
![Graphique 4](./graphe_exo4.png?width=35vw)

---

# Cours

*NumPy* est une bibliothèque Python pour manipuler des données numériques sous forme de **tableaux (arrays)**. Elle permet de faire des **calculs rapides** sur plusieurs valeurs.

## Création de tableaux

**1. Avec `np.array()`** → créer un tableau à partir d’une liste.

```python
import numpy as np
liste = [2, 4, 6]
t = np.array(liste)
print(t)  # Résultat : [2 4 6]
```

**2. Avec `np.arange()`** → créer des valeurs espacées régulièrement.

```python
t = np.arange(0, 5, 1)  # de 0 à 4 inclus
print(t)  # Résultat : [0 1 2 3 4]
```

**3. Avec `np.linspace()`** → créer un nombre fixe de valeurs entre deux bornes.

```python
t = np.linspace(0, 10, 5)
print(t)  # Résultat : [0.  2.5  5.  7.5 10.]
```

**4. Avec `np.ones(n)`** → créer un tableau de `n` uns.

```python
t = np.ones(4)
print(t)  # Résultat : [1. 1. 1. 1.]
```

**5. Avec `np.zeros(n)`** → créer un tableau de `n` zéros.

```python
t = np.zeros(3)
print(t)  # Résultat : [0. 0. 0.]
```


## Fonctions mathématiques

**1. Racine carrée : `np.sqrt()`**

```python
t = np.array([4, 9, 16])
print(np.sqrt(t))  # Résultat : [2. 3. 4.]
```

**2. Racine cubique : `np.cbrt()`**

```python
t = np.array([27, 64, 216])
print(np.cbrt(t))        # Résultat : array([3., 4., 6.])
```

**3. Exponentielle : `np.exp()`**

```python
t = np.array([0, 1, 2])
print(np.exp(t))  	# Résultat : [1. 2.71828183 7.3890561]
```

**4. Logarithme naturel : `np.log()`**

```python
t = np.array([1, np.e, np.e**2])
print(np.log(t))  	# Résultat : [ 0. 1. 2.]
```

**5. Logarithme base 2 : `np.log2()`**

```python
t = np.array([1, 2, 4, 8])
print(np.log2(t))	# Résultat : [ 0.  1.  2.  3. ]
```


**6. Logarithme base 10 : `np.log10()`**

```python
t = np.array([1, 10, 100, 0.1])
print(np.log10(t))	# Résultat : [ 0.   1.   2.  -1. ]
```

## Fonctions statistiques

**1. Somme : `np.sum()`**

```python
t = np.array([3, 7, 2, 9])
print(np.sum(t))    # 3 + 7 + 2 + 9 → 21
```

**2. Produit : `np.prod()`**

```python
t = np.array([3, 7, 2, 9])
print(np.prod(t))  # 3 * 7 * 2 * 9 → 378
```

**3. Valeur max/min : `np.max()` / `np.min()`**

```python
t = np.array([3, 7, 2, 9])
print(np.max(t))  # 9
print(np.min(t))  # 2
```

**4. Moyenne : `np.mean()`**

```python
t = np.array([80, 90, 100])
print(np.mean(t))  # (80 + 90 + 100)/3 → 90.0
```

**5. Médiane : `np.median()`**

```python
t = np.array([1, 2, 3, 4])
print(np.median(t))	# (4 + 1)/2 → 2.5
```

**6. Variance : `np.var()`**

```python
t = np.array([1, 2, 3, 4])
print(np.var(t))    	# somme des carrés des écarts à la moyenne → 1.25
```

**7. Écart-type : `np.std()`**

```python
t = np.array([1, 2, 3, 4])
print(np.std(t))    	# racine carrée de la variance → 1.118...
```

## Fonctions trigonométriques

**1. Sinus, cosinus et tangente : `np.sin()`, `np.cos()` et `tan()`**

```python
angles = np.array([0, np.pi/2, np.pi])
print(np.sin(angles))  # Résultat : [0. 1. 0.]
print(np.cos(angles))  # Résultat : [1. 0. -1.]
print(np.tan(angles))	# Résultat : [ 0.00000000e+00  1.63312394e+16 -1.22464680e-16]
```


**2. Sinus, cosinus et tangente inverses : `np.arcsin()`, `np.arccos()` et `np.arctan()`**

```python
t = np.array([1, -1, 0.1])	
print(np.arcsin(t))	# Résultat : [ 1.57079633 -1.57079633  0.10016742]
print(np.arccos(t))	# Résultat : [0.         3.14159265 1.47062891]
print(np.arctan(t))	# Résultat : [ 0.78539816 -0.78539816  0.09966865]
```

**3. Conversion degrés → radians : `np.deg2rad()`**

```python
t = np.array([90, 180, 270, 360])
print(np.deg2rad(t))	# Résultat : [1.57079633 3.14159265 4.71238898 6.28318531]
```

**4. Conversion radians → degrés : `np.rad2deg()`**

```python
t = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
print(np.rad2deg(t))	# Résultat : [ 90. 180. 270. 360.]
```


## Différences consécutives : `np.diff()`

```python
t = np.array([0, 5, 15])
print(np.diff(t))  # [5 10]
```

> Utile en physique : vitesse ≈ variation de position / variation de temps.


## Opérations vectorisées

* Lorsque vous effectuez une **opération arithmétique** (comme l'addition, la soustraction, la multiplication) entre **deux tableaux NumPy de même forme**, l'opération s'applique **automatiquement** à chaque paire d'éléments correspondants. 

**Exemple** :
```python
t = np.array([0, 1, 2])
x = 3 * t**2  # applique la formule à chaque valeur
print(x)  # Résultat : [0 3 12]
```

### Opérations arithmétiques

```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# Addition élément par élément
a + b    # → [11 22 33 44]

# Soustraction élément par élément
a - b    # → [-9 -18 -27 -36]

# Multiplication élément par élément
a * b    # → [10 40 90 160]

# Division élément par élément
a / b    # → [0.1 0.1 0.1 0.1]

# Puissance élément par élément
a ** 2   # → [ 1  4  9 16]

# Valeur absolue
np.abs([-3, -5])   # → [3 5]
```


## Régression linéaire avec NumPy (`np.polyfit()`)

###  Pourquoi parler de régression linéaire ?

En sciences, on mesure souvent **deux grandeurs liées entre elles**, par exemple :

* la température et la solubilité d’un sel,
* le temps et la distance parcourue,
* la concentration et l’absorbance d’une solution.

On veut savoir **s’il existe une relation linéaire** entre ces grandeurs, c’est-à-dire une **droite** du type :

$$
y = a x + b
$$

où :

* **x** = variable indépendante (qu’on choisit ou mesure, comme le temps)
* **y** = variable dépendante (qui dépend de x, comme la distance)
* **a** = pente de la droite
* **b** = ordonnée à l’origine (valeur de y quand x = 0)


### Trouver la droite de régression avec NumPy

La fonction la plus simple à utiliser est **`numpy.polyfit()`**.
Elle ajuste une droite (ou un polynôme) aux points expérimentaux.

```python
import numpy as np

# Données expérimentales
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0.1, 1.2, 2.0, 2.9, 4.1, 5.0])

# Calcul de la droite de régression (degré 1 = droite)
a, b = np.polyfit(x, y, 1)

print("Pente a =", round(a,2))
print("Ordonnée à l’origine b =", round(b,2))
```

**Résultat**  :
```
Pente a = 0.97
Ordonnée à l’origine b = 0.11
```

La droite obtenue est donc :
$
y = 0.97x + 0.11
$


### Tracer la droite et les points expérimentaux

On peut visualiser le tout avec **Matplotlib** :

```python
import matplotlib.pyplot as plt

# Calcul des valeurs prédites par la droite
y_pred = a * x + b

# Tracé d'un nuage de points et la droite
plt.scatter(x, y, color='blue', label='Données expérimentales')
plt.plot(x, y_pred, color='red', label='Droite de régression')

plt.xlabel("x (variable indépendante)")
plt.ylabel("y (variable dépendante)")
plt.title("Régression linéaire avec NumPy")
plt.legend()
plt.show()
```

![Graphe régression](./graphe_reg.png?width=35vw)

**Interprétation :**

* Les points bleus représentent vos données mesurées.
* La ligne rouge montre la tendance générale (le modèle linéaire).


### Évaluer la qualité de la régression

Pour savoir si la droite correspond bien aux données, on peut calculer le **coefficient de corrélation R²**.
Plus R² est proche de **1**, meilleure est la correspondance.

```python
# Calcul de R²
y_moy = np.mean(y)
ss_tot = np.sum((y - y_moy)**2)
ss_res = np.sum((y - y_pred)**2)
r2 = 1 - (ss_res / ss_tot)

print("Coefficient de détermination R² =", round(r2,3))
```

```
Coefficient de détermination R² = 0.997
```

### Résumé

| Étape | Fonction NumPy            | Rôle                                       |
| ----- | ------------------------- | ------------------------------------------ |
| 1     | `np.polyfit(x, y, 1)`     | Trouver la pente et l’ordonnée à l’origine |
| 2     | `y_pred = a*x + b`                 | Calculer les valeurs prédites              |
| 3     | `np.mean()` et `np.sum()` | Calculer R²                                |
| 4     | `plt.plot(x,y_pred)`       | Tracer les données et la droite            |


---

# Atelier

1. Téléchargez les fichiers de départ (.ipynb):
[Bloc-notes de départ](./blocnotes/atelier_numpy_regression.ipynb)
2. Déplacez-le dans votre dossier prévu pour de la semaine en cours.
3. Ouvrez votre dossier de travail programmation-sciences à partir de Visual Studio Code.
	* Vous devriez voir votre structure de dossiers et vos fichiers (.ipynb).

## Exercice 1 : Effet de la lumière sur la croissance des plantes

| Condition   | Plante 1 | Plante 2 | Plante 3 | Plante 4 | Plante 5 |
| ----------- | -------- | -------- | -------- | -------- | -------- |
| Naturelle   | 12.5     | 13.1     | 12.9     | 13.0     | 12.8     |
| LED blanche | 11.2     | 11.6     | np.nan   | 11.5     | 11.3     |
| LED rouge   | 10.4     | 10.1     | 10.2     | np.nan   | np.nan   |

1. Créez un tableau 2D `numpy.array()` avec ces données.
2. Calculez la **moyenne** et l’**écart-type** pour chaque condition avec `np.nanmean()` et `np.nanstd()`.
3. Identifiez la condition avec la plus grande croissance moyenne.
4. Représentez les moyennes avec un **diagramme en barres** et **barres d’erreur** correspondant aux écarts-types.

**Résultats** :
```
Moyenne (Naturelle) = 12.86 cm, écart-type = 0.21 cm  
Moyenne (LED blanche) = 11.40 cm, écart-type = 0.16 cm  
Moyenne (LED rouge) = 10.23 cm, écart-type = 0.12 cm  
Condition avec la plus grande croissance moyenne : Naturelle
```
![Graphique1](./graphique_croissance_lumiere.png?width=35vw)

## Exercice 2 : distance parcourue par un chariot en fonction du temps

On mesure la distance parcourue par un chariot en fonction du temps.

| Temps (s) | Distance (m) |
| --------: | -----------: |
|         0 |            0 |
|         1 |          0.9 |
|         2 |          1.8 |
|         3 |          2.9 |
|         4 |          4.1 |

1. Saisir ces données dans deux tableaux NumPy.
2. Calculer la droite de régression ( y = ax + b ).
3. Tracer le graphique (points + droite).
4. Calculer R².
5. Interpréter la pente : que représente-t-elle physiquement ?

*Indice :* La pente correspond à la **vitesse moyenne** du chariot.

**Résultat** :
```
Pente a = 1.02 m/s
Ordonnée à l’origine b = -0.01 m
Coefficient de détermination R² = 0.999
```
![Graphique2](./graphique_distance_chariot.png?width=35vw)

---

## À faire avant le prochain cours

1. Lire la prochaine leçon : [9. Lecture et écriture de fichiers de données](../semaine9/)
2. Faire les exercices de la [prochaine leçon](../semaine9/#exercices)
