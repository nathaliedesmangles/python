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
* Visualiser graphiquement l’incertitude ou la variabilité des mesures à l'aide de barres d'erreur.
* Modéliser une relation entre deux données à l'aide d'une droite de régression linéaire.

## Fichiers .ipynb pour la démo en classe

[**Bloc-note 1**](https://python-a25.netlify.app/blocnotes/demo_numpy_creation_fonctions.ipynb)  
{{% notice style="cyan" title="Sujets couverts..." groupid="notice-toggle" expanded="false" %}}
* Création de tableaux (`np.array`, `np.arange`, `np.linspace`, `np.ones`, `np.zeros`)
* Fonctions mathématiques (`np.sqrt`, `np.cbrt`, `np.exp`, `np.log`, `np.log2`, `np.log10`)
* Fonctions statistiques (`np.sum`, `np.prod`, `np.max`, `np.min`, `np.mean`, `np.median`, `np.var`, `np.std`)
* Fonctions trigonométriques (`np.sin`, `np.cos`, `np.tan`, `np.arcsin`, `np.arccos`, `np.arctan`, `np.deg2rad`, `np.rad2deg`)
* Différences consécutives (`np.diff`)
* Opérations vectorisées et arithmétiques élément par élément
{{% /notice %}}

[**Bloc-note 2**](https://python-a25.netlify.app/blocnotes/demo_numpy_operations_nan.ipynb)  
{{% notice style="cyan" title="Sujets couverts..." groupid="notice-toggle" expanded="false" %}}
* Ignorer des valeurs manquantes (`np.nan`, `np.nanmean`, `np.nansum`, etc.)
* Découpage et slicing simple (`[début:fin]`, `[début:fin:pas]`, `[:]`).
* Récapitulatif des syntaxes de slicing et indexation pour 1D et 2D.
* Exercices simples sur NaN et slicing.
{{% /notice %}}

[**Bloc-note 3**](https://python-a25.netlify.app/blocnotes/demo_numpy_filtrage_graphiques.ipynb)  
{{% notice style="cyan" title="Sujets couverts..." groupid="notice-toggle" expanded="false" %}}
* Filtrage de données avec conditions (`tableau[condition]`, `np.sum(condition)`)
* Filtrage avec `np.where()`
* Graphiques avec barres d’erreur (`plt.errorbar`)
* Régression linéaire (`np.polyfit`) et coefficient de détermination `R²`
* Exercices pour manipuler filtres, graphiques et régression
{{% /notice %}}

---

{{% notice style="accent" title="Apprendre par la pratique" %}}
- Faites les exercices en vous aidant des notes de cours ci-dessous.  
- Certains seront faits en classe à titre de démonstration.  
- Les solutions seront disponibles à la fin de la semaine prochaine.
{{% /notice %}}

---

## Fichier de départ à utiliser

1. Cliquez sur le lien pour télécharger le fichier : [Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_numpy_reg.ipynb)  
2. Enregistrez-le dans votre dossier **exercices** de la semaine en cours.  
3. Ouvrez **Visual Studio Code**.  
4. Recherchez et ouvrez le fichier `exercices_numpy_reg.ipynb`.  
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
	* pente, origine = np.polyfit(t[masque], y[masque], 1)
	* droite = pente * t + origine
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
<!--
**3. Exponentielle : `np.exp()`**

```python
t = np.array([0, 1, 2])
print(np.exp(t))  	# Résultat : [1. 2.71828183 7.3890561]
```
-->
**3. Logarithme naturel : `np.log()`**

```python
t = np.array([1, np.e, np.e**2])
print(np.log(t))  	# Résultat : [ 0. 1. 2.]
```

**4. Logarithme base 2 : `np.log2()`**

```python
t = np.array([1, 2, 4, 8])
print(np.log2(t))	# Résultat : [ 0.  1.  2.  3. ]
```


**5. Logarithme base 10 : `np.log10()`**

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

## Ignorer des valeurs manquantes dans les données (`np.nan`)

Parfois, une mesure a été oubliée ou mal prise. On utilise `np.nan` pour représenter une valeur manquante.

* La fonction `np.nanmean()` calcule **la moyenne des éléments en ignorant les valeurs `NaN`** (`Not a Number`), qui représentent généralement des données manquantes ou invalides.
* L'option axis permet de spécifier l'axe sur lequel se fait la moyenne:
	* axix = 0 -> la colonne (vertical)
	* axix = 1 -> la rangée (horizontal)

```python
sol = np.array([32.0, np.nan, 37.2])
moy = np.nanmean(sol)
print(f"Moyenne (sans valeur manquante) : {moy:.2f} g/100mL")
````

{{% notice style="cyan" title="Sachez que..." %}}
*  Sans `nanmean`, la fonction `np.mean(sol)` retournerait `nan` car une seule valeur `nan` dans la liste contamine le résultat.
* il existe d'autres fonctions statistiques qui ne tiennent pas compte des valeurs manquantes, par exemple: `np.nansum()`, `np.nanmedian()`, `np.nanstd()`, etc.
{{% /notice %}}


## Découpage et filtrage de données dans un tableau NumPy

Lorsqu’on travaille avec des tableaux NumPy, on utilise les **crochets `[]`** pour accéder à certaines valeurs ou parties du tableau.
C’est ce qu’on appelle l’**indexation** et le **slicing (tranches)**.

### Découpage (`slicing`)

Soit le tableau `t = np.array([10, 20, 30, 40, 50])`

#### 1. Tranches `[début:fin]`

* `t[début:fin]` retourne les éléments du tableau **de l’indice `début` inclus** jusqu’à **`fin` exclu**.
* Cela permet d’extraire une **portion du tableau**.

```python
print(t[1:4])  # éléments d'indice 1, 2 et 3
```
Résultat :
```
[20 30 40]
```

#### 2. Tranches avec pas `[début:fin:pas]`

On peut aussi spécifier un **pas** (bond).

* `t[début:fin:pas]` retourne un élément sur `pas`.

Exemple :

```python
print(t[0:5:2])  # un élément sur deux
```

Résultat :
```
[10 30 50]
```


#### 3. Omettre les bornes

* `t[:fin]` → du début jusqu’à `fin-1`.
* `t[début:]` → de `début` jusqu’à la fin.
* `t[:]` → tout le tableau (copie).

Exemple :

```python
print(t[:3])   # [10 20 30]
print(t[2:])   # [30 40 50]
print(t[:])    # [10 20 30 40 50]
```


## Récapitulatif

| Syntaxe       | Description                                                                                         |
| ------------- | --------------------------------------------------------------------------------------------------- |
| `a[i]`        | Accède à l’élément à l’index `i` (comme en Python, le premier élément est à l’index `0`).           |
| `a[i:j]`      | Sélectionne les éléments de l’index `i` inclus jusqu’à `j` exclus.                                  |
| `a[i:j:k]`    | Sélectionne les éléments de l’index `i` jusqu’à `j` exclus, en sautant de `k` en `k`.               |
| `a[:j]`       | Sélectionne les éléments du début jusqu’à `j` exclus.                                               |
| `a[i:]`       | Sélectionne les éléments de l’index `i` jusqu’à la fin.                                             |
| `a[:]`        | Sélectionne tous les éléments du tableau.                                                           |
| `a[-1]`       | Accède au **dernier élément**.                                                                      |
| `a[-k:]`      | Sélectionne les `k` derniers éléments.                                                              |
| `a[:, i]`     | Sélectionne la **colonne `i`** dans un tableau 2D.                                                  |
| `a[i, :]`     | Sélectionne la **ligne `i`** dans un tableau 2D.                                                    |
| `a[m:n, p:q]` | Sélectionne une **sous-matrice** allant des lignes `m` à `n` (exclu) et colonnes `p` à `q` (exclu). |


### Filtrage

#### 1. Accéder à uniquement certaines valeurs d'un tableau, selon une condition

```python
tableau = np.array([2, 5, 7, 1, 8, 3])
masque = tableau > 5  # Masquage : valeurs supérieures à 5
print(f"Masque booléen : {masque}")

valeurs_filtrees = tableau[masque]
print(f"Valeurs supérieures à 5 : {valeurs_filtrees}")
```

**Résultat attendu :**
Masque booléen : `[False False True False True False]`
Valeurs supérieures à 5 : `[7 8]`

**Explication :**

* `masque = tableau > 5` : crée une liste de booléens, `True` lorsque la valeur de `tableau` est > 5, `False` sinon.
* `tableau[masque]` : ne garde que les valeurs dans `tableau` qui sont > 5.


#### 2. Comptage conditionnel avec `np.sum`

Compter combien de valeurs respectent un seuil donné.

```python
tableau = np.array([3, 7, 4, 6, 2, 9, 5])
seuil = 5
nb_valeurs = np.sum(tableau > seuil)  # Comptage des valeurs > 5
print(f"Nombre de valeurs supérieures à {seuil} : {nb_valeurs}")
```

**Résultat attendu :**
Nombre de valeurs supérieures à 5 : 3

**Explication :**

* `tableau > seuil` : crée un masque booléen des valeurs > 5.
* `np.sum(tableau > seuil)` : compte le nombre de valeurs `True` dans le masque.


### 3. Filtre avec `np.where()`

`numpy.where(condition, valeur_si_vrai, valeur_si_faux)` permet de créer un **nouveau tableau** selon une condition logique appliquée à un autre tableau.

Un groupe d’étudiants a obtenu les notes suivantes :

```python
import numpy as np

notes = np.array([45, 78, 59, 92, 61, 33])
```

On veut créer un tableau indiquant **"Réussi"** ou **"Échoué"** selon la note (seuil : 60 %).

```python
resultat = np.where(notes >= 60, "Réussi", "Échoué")
print(resultat)
```

**Sortie :**
```
['Échoué' 'Réussi' 'Échoué' 'Réussi' 'Réussi' 'Échoué']
```


** Explication** :
* `notes >= 60` crée un **tableau booléen** :
  ```
  [False, True, False, True, True, False]
  ```
* `np.where()` choisit `"Réussi"` si la condition est `True`, sinon `"Échoué"`.


#### Variante : Classer les performances

```python
niveau = np.where(notes >= 85, "Excellent",
          np.where(notes >= 60, "Réussi", "Échoué"))
print(niveau)
```

**Résultat :**
```
['Échoué' 'Réussi' 'Échoué' 'Excellent' 'Réussi' 'Échoué']
```


## Graphique avec barres d’erreur 

Les **barres d’erreur** servent à montrer **l’incertitude** des mesures.
Elles indiquent à quel point les données sont précises.

```python
# Données simulées : moyenne et incertitude
x = np.array([1, 2, 3, 4, 5])               # numéros d’échantillons
y = np.array([2.1, 2.5, 3.0, 2.7, 3.2])     # valeurs mesurées
erreur = np.array([0.2, 0.3, 0.15, 0.25, 0.2])  # incertitudes

# Tracé
plt.errorbar(x, y, yerr=erreur, fmt='o', capsize=5, color='royalblue', ecolor='black')
plt.xlabel("Échantillon")
plt.ylabel("Valeur mesurée")
plt.title("Graphique avec barres d’erreur")
plt.grid(True)
plt.show()
```

![graphique avec barres d'erreur](./graphe_barres_err.png?width=35vw)

### Explications 

* **`plt.errorbar()`** → La fonction permettant de spécifier les longueurs/largeurs des barres d'erreur.
* **`yerr=erreur`** → indique la longueur des barres d’erreur verticales.
* Si on veut des barres d'erreur horizontales: **`xerr=erreur`** → indique la longueur des barres d’erreur horizontales.
* **`fmt='o'`** → forme des points (ici des cercles).
* **`capsize=5`** → ajoute un petit “chapeau” au bout des barres.
* **`ecolor='black'`** → couleur des barres d’erreur.

**NB**: `plt.xticks(x, tetxte)` # pour afficher du texte au lieu des valeurs, sur l'axe x

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

Pour savoir si la droite correspond bien aux données, on peut calculer le **coefficient de détermination R²**.
Plus R² est proche de **1**, meilleure est la correspondance.
$$
  0 \le R^2 \le 1
$$

  * ( R² = 1 ) → le modèle explique **toute** la variation de ( y )
  * ( R² = 0 ) → le modèle **n’explique rien**

**Formule du coefficient R²** : 
$$
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

Où :  
$y_{i}\$ sont les valeurs expérimentales observées  
$\hat{y}_i\$ sont les valeurs prédites par le modèle  
$\bar{y}$  est la moyenne des valeurs observées  
${\sum (y_i - \hat{y}_i)^2}$ est la somme des carrés des résidus  
${\sum (y_i - \bar{y})^2}$  est la somme totale des carrés

**Avec Python** : 

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
[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/atelier_numpy_regression.ipynb)
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
