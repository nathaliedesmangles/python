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

[Fichier utilisé pour la démonstration](./demo_nympy_reg.ipynb)

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
v = np.array(liste)
print(v)  # Résultat : [2 4 6]
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
u = np.ones(4)
print(u)  # Résultat : [1. 1. 1. 1.]
```

**5. Avec `np.zeros(n)`** → créer un tableau de `n` zéros.

```python
z = np.zeros(3)
print(z)  # Résultat : [0. 0. 0.]
```


## Fonctions mathématiques

**1. Racine carrée : `np.sqrt()`**

```python
x = np.array([4, 9, 16])
print(np.sqrt(x))  # Résultat : [2. 3. 4.]
```

**2. Racine cubique : `np.cbrt()`**

```python
x = np.array([27, 64, 216])
print(np.cbrt(x))        # Résultat : array([3., 4., 6.])
```

**3. Exponentielle : `np.exp()`**

```python
x = np.array([0, 1, 2])
print(np.exp(x))  	# Résultat : [1. 2.71828183 7.3890561]
```

**4. Logarithme naturel : `np.log()`**

```python
x = np.array([1, np.e, np.e**2])
print(np.log(x))  	# Résultat : [ 0. 1. 2.]
```

**5. Logarithme base 2 : `np.log2()`**

```python
x = np.array([1, 2, 4, 8])
print(np.log2(arr))	# Résultat : [ 0.  1.  2.  3. ]
```


**6. Logarithme base 10 : `np.log10()`**
```python
x = np.array([1, 10, 100, 0.1])
print(np.log10(x))	# Résultat : [ 0.   1.   2.  -1. ]
```

## Fonctions statistiques

**1. Somme : `np.sum()`**

```python
data = np.array([3, 7, 2, 9])
print(np.sum(data))    # → 21
```

**2. Produit : `np.prod()`**
```python
data = np.array([3, 7, 2, 9])
print(np.prod(data))  # → 378
```

**3. Valeur max/min : `np.max()` / `np.min()`**

```python
data = np.array([3, 7, 2, 9])
print(np.max(data))  # 9
print(np.min(data))  # 2
```

**4. Moyenne : `np.mean()`**

```python
notes = np.array([80, 90, 100])
print(np.mean(notes))  # 90.0
```

**5. Médiane : `np.median()`**
```python
x = np.array([1, 2, 3, 4])
print(np.median(x))	# → 2.5
```

**6. Variance : `np.var()`**

```python
np.var(x)    # → 1.25
```

**7. Écart-type : `np.std()`**

```python
np.std(x)    # → 1.118...
```

## Fonctions trigonométriques

## 6. Trigonométrie

```python
# Sinus
np.sin(np.pi/2)   # → 1.0

# Cosinus
np.cos(0)         # → 1.0

# Tangente
np.tan(np.pi/4)   # → 1.0

# Sinus inverse
np.arcsin(1)      # → 1.5707... (≈ π/2)

# Cosinus inverse
np.arccos(0)      # → 1.5707...

# Tangente inverse
np.arctan(1)      # → 0.7853... (≈ π/4)

# Arctangente avec quadrant correct
np.arctan2(1,1)   # → 0.7853... (≈ π/4)

# Conversion degrés → radians
np.deg2rad(180)   # → 3.14159...

# Conversion radians → degrés
np.rad2deg(np.pi) # → 180.0
```


**2. Sinus et cosinus : `np.sin()` et `np.cos()`**

```python
angles = np.array([0, np.pi/2, np.pi])
print(np.sin(angles))  # Résultat : [0. 1. 0.]
print(np.cos(angles))  # Résultat : [1. 0. -1.]
```



**7. Différences consécutives : `np.diff()`**

```python
x = np.array([0, 5, 15])
print(np.diff(x))  # [5 10]
```

> Utile en physique : vitesse ≈ variation de position / variation de temps.

---

## Opérations vectorisées

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
---

## Régression linéaire avec NumPy (`np.polyfit()`)

```python
t = np.array([0, 1, 2, 3])
x = np.array([0, 2, 4.1, 6.2])
a, b = np.polyfit(t, x, 
````


1.

print("Pente =", a, "Ordonnée =", b)

# Résultat attendu : Pente ≈ 2.05, Ordonnée ≈ 0.02

````

```python
# Exemple complet
t = np.array([0, 1, 2, 3, 4])
x = np.array([0, 2.1, 4.2, 6.1, 8.2])
a, b = np.polyfit(t, x, 1)
print("Pente (vitesse) =", a)
print("Ordonnée à l'origine =", b)
````

> La **pente** correspond à la vitesse moyenne.

---

## Tracer une droite de régression

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([2.1, 4.2, 6.1, 8.0])

# Droite de régression
a, b = np.polyfit(x, y, 1)
y_reg = a * x + b

plt.plot(x, y, "o", label="Données")
plt.plot(x, y_reg, "-", label=f"y = {a:.2f}x + {b:.2f}")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

---

# Atelier : Effet de la lumière sur la croissance des plantes

| Condition   | Plante 1 | Plante 2 | Plante 3 | Plante 4 | Plante 5 |
| ----------- | -------- | -------- | -------- | -------- | -------- |
| Naturelle   | 12.5     | 13.1     | 12.9     | 13.0     | 12.8     |
| LED blanche | 11.2     | 11.6     | np.nan   | 11.5     | 11.3     |
| LED rouge   | 10.4     | 10.1     | 10.2     | np.nan   | np.nan   |

1. Créez un tableau 2D `numpy.array()` avec ces données.
2. Calculez la **moyenne** et l’**écart-type** pour chaque condition avec `np.nanmean()` et `np.nanstd()`.
3. Identifiez la condition avec la plus grande croissance moyenne.
4. Représentez les moyennes avec un **diagramme en barres** et **barres d’erreur** correspondant aux écarts-types.

---

## À faire avant le prochain cours

1. Lire la prochaine leçon : [9. Lecture et écriture de fichiers de données](../semaine9/)
2. Faire les exercices de la [prochaine leçon](../semaine9/#exercices)
