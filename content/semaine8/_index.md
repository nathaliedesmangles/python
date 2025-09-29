+++
chapter = true
pre = "8."
title = " Tableaux numpy et droite de régression"
weight = 108
draft = true
+++


## Objectifs

* Créer des **tableaux de données** à une ou deux dimensions.
* Calculer des **moyennes** et **écarts types**.
* Gérer des données **expérimentales incomplètes** (`np.nan`).
* Comparer des résultats entre éléments ou conditions.
* Filtrer des données selon des conditions.
* Tracer un graphique à barres muni d'une barre d'erreur avec `matplotlib`.
* Tracer une droite de régression et interpréter la pente, l’ordonnée à l’origine et le coefficient de détermination R².
* Établir une relation entre deux données.

Comprendre ce qu’est NumPy et pourquoi il est utile en sciences.
Apprendre à créer et manipuler des tableaux NumPy.
Utiliser NumPy pour traiter des données physiques et faire des calculs rapides.
Appliquer NumPy à des situations concrètes en mécanique (cinématique, énergie, forces).

---

{{% notice style="accent" title="Apprendre par la pratique" %}}
- **Faites les exercices** en vous aidant des notes de cours ci-dessous.
- Certains seront fait en classe à titre de démonstration.
- Les solutions seront disponibles à la fin de la semaine prochaine.
{{% /notice %}}

# Exercices

## Fichier de départ à utiliser

1. Cliquez sur le lien pour télécharger le fichier.
[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_numpy.ipynb)
2. Enregistrez le fichier dans votre dossier **exercices** de la semaine en cours.
3. Ouvrez **Visual Studio Code**.
4. Dans VS Code, recherchez et ouvrez le fichier `exercices_numpy.ipynb`
5. Assurez-vous que le noyau Python (`Kernel`) soit sélectionné.
6. Vous pouvez commencer à faire les exercices.


## Exercice 1 : Chute libre

Un objet est lâché sans vitesse initiale d’une hauteur $h = 20 \, m$.
La position est donnée par :

$$
y(t) = h - \frac{1}{2} g t^2
$$

avec $g = 9.8 \, m/s^2$.

Écris un programme qui :

1. Crée un tableau `t` de 0 à 2 secondes (21 valeurs).
2. Calcule la position `y`.
3. Affiche les 5 premières valeurs.


## Exercice 2 : Mouvement rectiligne uniforme

Une voiture roule à $v = 15 \, m/s$.
La position est donnée par :

$$
x(t) = v \cdot t
$$

Écris un programme qui :

1. Crée un tableau de temps entre 0 et 10 s (par pas de 0.5).
2. Calcule la position.
3. Affiche la dernière valeur (la position après 10 s).


## Exercice 3 : Énergie cinétique

La formule est :

$$
E_c = \frac{1}{2} m v^2
$$

Un objet de masse $m = 2.0 \, kg$ accélère de 0 à 20 m/s.

Écris un programme qui :

1. Crée un tableau de vitesses de 0 à 20 m/s (pas de 2).
2. Calcule l’énergie cinétique correspondante.
3. Affiche les résultats.


## Exercice 4 : Oscillations harmoniques

La position d’un oscillateur est donnée par :

$$
x(t) = A \cos(\omega t)
$$

avec $A = 0.1 \, m$, $\omega = 2 \pi \, rad/s$.

Écris un programme qui :

1. Crée un tableau `t` de 0 à 2 s (101 valeurs).
2. Calcule la position `x(t)`.
3. Affiche la valeur maximale et minimale de la position. 


---

# Cours

## Pourquoi NumPy ?

* En sciences, nous travaillons souvent avec des données numériques : mesures expérimentales, vecteurs, séries temporelles, etc.
* En Python de base, on peut utiliser des listes, mais elles sont limitées pour les calculs scientifiques.
* La **bibliothèque NumPy** (*Numerical Python*) permet de manipuler efficacement des tableaux numériques (***arrays***).

## Importer la bibliothèque

Avant de d’utiliser les fonctionnalités de NumPy, on doit importer la bibliothèque :

```python
import numpy as np
```
Ici, `np` est un **alias** utilisé par convention.


## Créer des tableaux (arrays)

### À partir d’une liste Python

```python
import numpy as np

v = np.array([2, 4, 6, 8])
print(v)
```

**Résultat** :
```
[2 4 6 8]
```

### Générer rapidement des tableaux numériques

* `np.arange(début, fin, pas)` → nombres régulièrement espacés.
* `np.linspace(début, fin, n)` → n valeurs également réparties.
* `np.zeros(n)` → n zéros.
* `np.ones(n)` → n uns.

Exemples :

```python
x = np.linspace(0, 10, 6)
print(x)
```

**Résultat** :
```
[ 0.  2.  4.  6.  8. 10.]
```
***AJOUTER EXEMPLES AUTRES FN***

## Opérations vectorisées

Avec NumPy, les **opérations s’appliquent à tout le tableau** (pas besoin de boucles `for`).

```python
x = np.array([0, 1, 2, 3])
y = x**2   # chaque élément est mis au carré
print(y)
```

**Résultat** :
```
[0 1 4 9]
```

### Opérations arithmétiques élémentaires

Avec
`a = np.array([1, 2, 3, 4])` et  
`b = np.array([10, 20, 30, 40])`


| Opération      | Exemple avec NumPy | Description                      | Résultat (vectorisé)    |
| -------------- | ------------------ | -------------------------------- | ----------------------- |
| Addition       | `a + b`            | addition élément par élément     | [11 22 33 44]           |
| Soustraction   | `a - b`            | soustraction élément par élément | [-9 -18 -27 -36]        |
| Multiplication | `a * b`            | produit élément par élément      | [10 40 90 160]          |
| Division       | `a / b`            | division élément par élément     | [0.1 0.1 0.1 0.1]       |
| Puissance      | `a ** 2`           | élève chaque élément au carré    | [1 4 9 16]              |
| Racine carrée  | `np.sqrt(a)`       | racine carrée de chaque élément  | [1. 1.41421356 1.73205081 2.] |
| Valeur absolue | `np.abs(a)`        | valeur absolue de chaque élément | [9 18 27 36]            |


## Fonctions mathématiques

NumPy propose beaucoup de fonctions

### 1. Fonctions statistiques

Avec `a = np.array([1, 2, 3, 4])`

| Fonction   | Exemple        | Résultat
| ---------- | -------------- | ----------------- |
| Moyenne    | `np.mean(a)`   | 2.5               |
| Médiane    | `np.median(a)` | 2.5               |
| Somme      | `np.sum(a)`    | 10                |
| Produit    | `np.prod(a)`   | 24                |
| Variance   | `np.var(a)`    | 1.25              |
| Écart-type | `np.std(a)`    | 1.118033988749895 |
| Minimum    | `np.min(a)`    | 1                 |
| Maximum    | `np.max(a)`    | 4                 |


### 2. Fonctions logarithmiques et trigonométriques

Avec ` = np.array([1, 2, 3, 4])`

| Fonction           | Exemple          | Résultat                    |
| ------------------ | ---------------- | --------------------------- |
| Arrondi            | `np.round(a, 2)` | arrondit à 2 décimales      |
| Plafond            | `np.ceil(a)`     | arrondi supérieur           |
| Plancher           | `np.floor(a)`    | arrondi inférieur           |
| Exponentielle      | `np.exp(a)`      | \$e^x\$ élément par élément |
| Logarithme naturel | `np.log(a)`      | \$\ln(x)\$                  |
| Logarithme base 2  | `np.log2(a)`     | \$\log\_{2}(x)\$           |
| Logarithme base 10 | `np.log10(a)`    | \$\log\_{10}(x)\$           |

| **Exponentielles et logarithmes** | `np.exp(x)`         | Exponentielle e^x                      | `np.exp(1) → 2.718…`           |
|                                   | `np.expm1(x)`       | e^x - 1 (utile pour petites valeurs)   | `np.expm1(1e-5) → 1.000005e-5` |
|                                   | `np.log1p(x)`       | ln(1+x)                                | `np.log1p(1e-5) → 0.00001`     |

 | `np.log(np.e) → 1`             |
 | `np.log2(8) → 3`               |
| `np.log10(1000) → 3`           |


Exemple :
```python
angles = np.linspace(0, np.pi, 4)
print(np.sin(angles))
```

**Principales Fonctions trigonométriques**

| Fonction                    | Exemple         | Résultat                     |
| --------------------------- | --------------- | ---------------------------- |
| Sinus                       | `np.sin(a)`     | sinus élément par élément    |
| Cosinus                     | `np.cos(a)`     | cosinus élément par élément  |
| Tangente                    | `np.tan(a)`     | tangente élément par élément |
| Arcsin                      | `np.arcsin(a)`  | sinus inverse                |
| Arccos                      | `np.arccos(a)`  | cosinus inverse              |
| Arctan                      | `np.arctan(a)`  | tangente inverse             |
| Conversion degrés → radians | `np.deg2rad(a)` | transforme ° en rad          |
| Conversion radians → degrés | `np.rad2deg(a)` | transforme rad en °          |

### Constantes et autres fonctions utiles

| Catégorie                         | Fonction            | Description                            | Exemple                        |
| --------------------------------- | ------------------- | -------------------------------------- | ------------------------------ |
| **Constantes**                    | `np.pi`             | Valeur de π                            | `np.pi → 3.14159…`             |
|                                   | `np.e`              | Base du logarithme naturel             | `np.e → 2.71828…`              |
|                                   | `np.arctan2(y, x)`  | Arctangente de y/x en quadrant correct | `np.arctan2(1,1) → π/4`        |
| **Racines et valeurs absolues**   | `np.sqrt(x)`        | Racine carrée                          | `np.sqrt(9) → 3`               |
|                                   | `np.cbrt(x)`        | Racine cubique                         | `np.cbrt(27) → 3`              |
|                                   | `np.abs(x)`         | Valeur absolue                         | `np.abs(-5) → 5`               |
|                                   | `np.fabs(x)`        | Valeur absolue flottante               | `np.fabs(-5.2) → 5.2`          |
| **Arrondi et troncature**         | `np.round(x, n)`    | Arrondi à n décimales                  | `np.round(3.14159,2) → 3.14`   |
|                                   | `np.floor(x)`       | Arrondi inférieur                      | `np.floor(3.7) → 3`            |
|                                   | `np.ceil(x)`        | Arrondi supérieur                      | `np.ceil(3.2) → 4`             |
|                                   | `np.trunc(x)`       | Tronque la partie décimale             | `np.trunc(3.7) → 3`            |

{{% notice style="blue" title="Principales fonctions mathématiques de NumPy" groupid="notice-toggle" expanded="false" %}}
{{% /notice %}}





























<!--

### Quelques exemples

#### 1. Calculer le sinus d'un angle en radian

```python
import numpy as np

# Definition de l'angle en radians
angle = np.pi / 2  # 90 degrés en radians

# Calcul du sinus
sinus = np.sin(angle)

# Afficher le résultat
print("Sinus de 90 degrés (π/2 radians):", sinus)
```

#### 2. Calculer la moyenne des données avec np.mean()

```python
sol = np.array([32.0, 35.5, 37.2])
moy = np.mean(sol)
print(f"Moyenne : {moy:.2f} g/100mL")
```

#### 3. Calculer l’écart type des données avec np.std()

```python
sol = np.array([32.0, 35.5, 37.2])
ecart = np.std(sol)
print(f"Écart type : {ecart:.2f}")
```

## Opérations vectorielles (rapides et simples)

Avec NumPy, on peut faire des **opérations sur tout un tableau en une seule ligne** (sans utiliser de boucle).

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
```

### 1. Addition élément par élément

```python
x + y    # [5 7 9]
```

### 2. Soustraction élément par élément

```python
y - x    # [3 3 3]
```

### 3. Multiplication par un scalaire

```python
x * 10   # [10 20 30]
```

### 4. Division par un scalaire

```python
y / 2    # [2.  2.5 3. ]
```
-->

## Ignorer des valeurs manquantes (`np.nan`)

Parfois, une mesure a été oubliée ou mal prise. On utilise `np.nan` pour représenter une valeur manquante :

```python
sol = np.array([32.0, np.nan, 37.2])
moy = np.nanmean(sol)
print(f"Moyenne (sans valeur manquante) : {moy:.2f} g/100mL")
```

* La fonction `np.nanmean()` calcule **la moyenne des éléments en ignorant les valeurs `NaN`** (`Not a Number`), qui représentent généralement des données manquantes ou invalides.

{{% notice style="cyan" title="Notez" %}}
Sans `nanmean`, la fonction `np.mean(sol)` retournerait `nan` car une seule valeur `nan` dans la liste contamine le résultat.
{{% /notice %}}

## Filtrage de données

1. **Créer un tableau et afficher uniquement certaines valeurs selon une condition**

```python
tableau = np.array([2, 5, 7, 1, 8, 3])
masque = tableau > 5	# Masquage : valeurs supérieures à 5
print(f"Masque booléen : {masque}")

valeurs_filtrees = tableau[masque]
print(f"Valeurs supérieures à 5 : {valeurs_filtrees}")
```
**Résultat attendu :**
```
Masque booléen : [False False  True False  True False]
Valeurs supérieures à 5 : [7 8]
```

**Explication** :
* `masque = tableau > 5` : crée une liste de booléen, `True` lorsque la valeur de `tableau` est > 5, `False` sinon.
* `tableau[masque]` : ne garde que les valeurs dans `tableau` qui sont > 5.

2. **Comptage conditionnel avec `np.sum`**

Compter combien de valeurs respectent un seuil donné.

```python
tableau = np.array([3, 7, 4, 6, 2, 9, 5])
seuil = 5

nb_valeurs = np.sum(tableau > seuil)	# Comptage des valeurs > 5
print(f"Nombre de valeurs supérieures à {seuil} : {nb_valeurs}")
```

**Résultat attendu** :
```
Nombre de valeurs supérieures à 5 : 3
```

**Explication** :
* `tableau > seuil` : conserve les valeurs dans `tableau` qui sont > 5.
* `np.sum(tableau > seuil)` : compte le nombre de valeurs dans `tableau` qui sont > 5.


3. **Filtre avec `np.where()`**

* `numpy.where(condition, valeur_si_vrai, valeur_si_faux)` permet de créer un tableau (ou une colonne dans un DataFrame) en fonction d’une condition logique.

   * **condition** → un test qui renvoie `True` ou `False` (par exemple : `df["Note"] >= 60`)
   * **valeur_si_vrai** → ce qui sera écrit quand la condition est vraie (`"Réussi"`)
   * **valeur_si_faux** → ce qui sera écrit quand la condition est fausse (`"Échoué"`)

Exemple :

```python
df["Tendance"] = np.where(df["Note"] >= 60, "Réussi", "Échoué")
```

**Explication**:

Pour chaque ligne :

   * si la note est >= 60 → `"Réussi"`
   * sinon → `"Échoué"`.

C’est une méthode très rapide car `numpy` applique l’opération directement sur toute la colonne, sans boucle explicite.

---


## Tracer des graphiques à barres et avec barres d'erreur

### Importer la bibliothèque

```python
import matplotlib.pyplot as plt
```

### Graphique à barres

**Exemple de base :**

```python
noms = ["A", "B", "C"]
valeurs = [4, 7, 5]

plt.bar(noms, valeurs)
plt.title("Résultats")
plt.xticks(rotation=0)
plt.legend(["Score"])
plt.show()
```
![graphique à barres](./graphique_barres.png?width=40vw)

| Fonction        | Rôle                                |
| --------------- | ----------------------------------- |
| `plt.bar(x, y)` | Crée des barres                     |
| `plt.xticks()`  | Contrôle les étiquettes sur l’axe x |


### Graphique avec barres d’erreur

La fonction `plt.errorbar()` permet de tracer des barres d'erreur autour des points d'une courbe, et ici la liste `erreurs = [0.5, 0.3, 0.6]` indique **l'incertitude verticale** (±) associée à chaque point.

**Exemple :**
```python
x = [1, 2, 3]
y = [10, 12, 9]
erreurs = [0.5, 0.3, 0.6]

plt.errorbar(x, y, yerr=erreurs, fmt="o", label="Mesures")
plt.title("Mesures avec incertitude")
plt.legend()
plt.grid(True)
plt.show()
```

![graphique à barres d'erreur](./graphique_barres_erreurs.png?width=40vw)

| Argument  | Signification                    |
| --------- | -------------------------------- |
| `yerr`    | barres d’erreur verticales       |
| `xerr`    | (optionnel) erreurs horizontales |
| `fmt="o"` | style des points                 |


## Tracer une droite de régression

**Rappel** : L'équation d'une droite est `y = a·x + b`

Voici comment obtenir les données de la droite :

* `a, b = np.polyfit(x, y, 1)` : On calcule la droite qui s'ajuste le mieux aux points (régression linéaire) et on récupère sa pente (`a`) et son ordonnée à l'origine (`b`).
* `y_reg = a * x + b` : On utilise la pente et l'ordonnée pour calculer les valeurs de la droite.
* `plt.plot(x, y, "o", label="Données")` : On trace les points de données sous forme de cercles.
* `plt.plot(x, y_reg, "-", label=f"y = {a:.2f}x + {b:.2f}")` : On trace la droite de régression et on affiche son équation.


```python
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([2.1, 4.2, 6.1, 8.0])

# Droite de régression : y = a·x + b

a, b = np.polyfit(x, y, 1)
y_reg = a * x + b

plt.plot(x, y, "o", label="Données")
plt.plot(x, y_reg, "-", label=f"y = {a:.2f}x + {b:.2f}")
plt.legend()
plt.grid(True)
plt.tight_layout()	# Ajuste l'espacement pour éviter le chevauchement
plt.show()
```
![graphique droite de régression](./graphique_regression.png?width=40vw)


---

# Atelier

1. Téléchargez le fichier de départ : [Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/atelier_numpy_regression.ipynb)
2. Déplacez-le dans votre dossier prévu pour **l'atelier de la semaine 7**.
3. Ouvrez votre dossier de travail `programmation-sciences` **à partir de Visual Studio Code**.
   * Vous devriez voir votre structure de dossiers et vos fichiers (.ipynb).


## Exercice : Effet de la lumière sur la croissance des plantes

Une équipe de recherche a étudié l’influence de différents types de lumière sur la croissance de jeunes plantes. Après **10 jours**, la **hauteur (en cm)** de **5 plantes** a été mesurée dans chacune des **trois conditions lumineuses** suivantes :

* **Lumière naturelle**
* **Lumière LED blanche**
* **Lumière LED rouge**

Certaines mesures sont manquantes (notées `np.nan`), car une ou deux plantes n’ont pas survécu. Voici les données brutes :

| Condition   | Plante 1 | Plante 2 | Plante 3 | Plante 4 | Plante 5 |
| ----------- | -------- | -------- | -------- | -------- | -------- |
| Naturelle   | 12.5     | 13.1     | 12.9     | 13.0     | 12.8     |
| LED blanche | 11.2     | 11.6     | np.nan   | 11.5     | 11.3     |
| LED rouge   | 10.4     | 10.1     | 10.2     | np.nan   | np.nan   |


1. **Représentation des données**
   * Crée un tableau 2D avec `numpy.array()` contenant les mesures ci-dessus.
   * Stocke les noms des conditions dans une liste `conditions = ["Naturelle", "LED blanche", "LED rouge"]`.

2. **Analyse statistique**
   * Calcule la **moyenne** et l’**écart-type** de la hauteur des plantes pour chaque condition.
   * Utilise `np.nanmean()` et `np.nanstd()` pour **ignorer les valeurs manquantes** (`np.nan`).

3. **Comparaison entre conditions**
   * Détermine la condition qui présente la croissance moyenne la plus élevée.
   * Affiche un résumé clair, par exemple :
     ```
     Moyenne (Naturelle) = 12.86 cm, écart-type = 0.22 cm
     Moyenne (LED blanche) = ...
     Moyenne (LED rouge) = ...
     Condition avec la plus grande croissance moyenne : Naturelle
     ```

4. **Visualisation graphique**
   * Représente les moyennes avec un **diagramme en barres** (`plt.bar`).
   * Ajoute les **barres d’erreur** correspondant aux écarts-types.
   * Mets les noms des conditions en abscisse avec `plt.xticks()`.
   * Ajoute un titre et un label pour l’axe des ordonnées (hauteur moyenne en cm).

![Graphique](./graphique_croissance_lumiere.png?width=45vw)


---

## À faire avant le prochain cours

1. Lire la prochaine leçon : [9. Lecture et écriture de fichiers de données](../semaine9/)
2. Faire les exercices de la [prochaine leçon](../semaine9/#exercices)