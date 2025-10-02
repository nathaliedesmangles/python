+++
chapter = true
pre = "8."
title = " Tableaux NumPy et droite de régression"
weight = 108
draft = true
+++


## Objectifs

* Comprendre ce qu’est NumPy et pourquoi il est utile en sciences.
* Apprendre à créer et manipuler des tableaux NumPy.
* Utiliser NumPy pour traiter des données physiques et faire des calculs rapides.
* Appliquer NumPy à des situations concrètes en mécanique (cinématique, énergie, forces).
* Modéliser une relation entre deux données à l'aide d'une droite de régression linéaire.


---

{{% notice style="accent" title="Apprendre par la pratique" %}}
- **Faites les exercices** en vous aidant des notes de cours ci-dessous.
- Certains seront fait en classe à titre de démonstration.
- Les solutions seront disponibles à la fin de la semaine prochaine.
{{% /notice %}}


## Fichier de départ à utiliser

1. Cliquez sur le lien pour télécharger le fichier.
[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_numpy.ipynb)
2. Enregistrez le fichier dans votre dossier **exercices** de la semaine en cours.
3. Ouvrez **Visual Studio Code**.
4. Dans VS Code, recherchez et ouvrez le fichier `exercices_numpy.ipynb`
5. Assurez-vous que le noyau Python (`Kernel`) soit sélectionné.
6. Vous pouvez commencer à faire les exercices.


---

# Exercices 

## Exercice 1 : Chute libre verticale

Un objet est lâché d’une hauteur ( h = 20 , m ) sans vitesse initiale.   
La formule de la position est :
```math
$$ y(t) = h - \frac{1}{2} g t^2	$$ 
```
où 
```math
$ g = 9.8 m/s^2 $
```

1. **Importer NumPy** avec l’instruction `import numpy as np`.
2. Créer un tableau `t` allant de 0 à 2 secondes, avec 21 valeurs également espacées (`np.linspace`).
3. Calculer la position `y` avec la formule ci-dessus.
4. Afficher les **5 premières valeurs de `y`** avec `print(y[:5])`.


## Exercice 2 : Mouvement rectiligne uniforme

Une voiture roule à vitesse constante (v = 15 , m/s). Sa position est donnée par :
```math
$$
x(t) = v \cdot t
$$
```


1. Crée un tableau `t` allant de 0 à 10 secondes avec un pas de 0.5 (`np.arange`).
2. Calcule la position `x` pour chaque valeur de `t`.
3. Affiche la **dernière valeur de `x`** pour connaître la position au bout de 10 s.


## Exercice 3 : Énergie cinétique

La formule de l’énergie cinétique est :
```math
$$
E_c = \frac{1}{2} m v^2
$$
```
Un objet de masse (m = 2.0 , kg) accélère de 0 à 20 m/s.

1. Crée un tableau `v` des vitesses de 0 à 20 m/s avec un pas de 2 (`np.arange`).
2. Applique la formule pour calculer `Ec`.
3. Affiche le tableau des énergies cinétiques obtenues.
4. Vérifie la valeur maximale avec `np.max(Ec)`.


## Exercice 4 : Oscillations harmoniques

La position d’un oscillateur est donnée par :
```math
$$
x(t) = A \cos(\omega t)
$$
```
avec
```math 
A = 0.1 m et 
$\omega = 2 \pi rad/s $
```


1. Crée un tableau `t` de 0 à 2 secondes avec 101 valeurs (`np.linspace`).
2. Calcule la position `x` en appliquant la formule.
3. Utilise `np.max(x)` et `np.min(x)` pour trouver les extrêmes de l’oscillation.
4. Vérifie que les résultats correspondent bien à (A) et (-A).

---

# Cours

*NumPy* est une bibliothèque Python conçue pour manipuler des données numériques sous forme de **tableaux (arrays)**. Elle est particulièrement utile pour appliquer rapidement des **formules** sur plusieurs valeurs.


## Création de tableaux 

**1. Avec `np.array()`**

* `np.array([valeurs])` → créer un tableau à partir d’une liste.

```python
import numpy as np
liste = [2, 4, 6]

v = np.array(liste)
print(v) 	# Résultat : [2 4 6]
```

**2. Avec `np.arange()`**

* `np.arange(debut, fin, pas)` → créer des valeurs espacées régulièrement.

```python
t = np.arange(0, 5, 1)  # de 0 à 4 inclus
print(t)	# Résultat : [0 1 2 3 4]
```


**3. Avec `np.linspace()`**

* `np.linspace(debut, fin, nombre)` → créer un nombre fixe de valeurs entre deux bornes.

```python
t = np.linspace(0, 10, 5)
print(t) # Résultat : [ 0.  2.5  5.  7.5 10. ]
```

**4. Avec `np.ones(n)`**

* `np.ones(n)` → créer un tableau NumPy de `n` **1**

```python
u = np.ones(4)
print(u)	# Résultat : [1. 1. 1. 1.]
```


**5. Avec `np.zeros()`**

* `np.zeros(n)` → créer un tableau NumPy de `n` **0**

```python
z = np.zeros(3)
print(z)	# Résultat : [0. 0. 0.]
```

## Fonctions mathématiques (statistiques, trigonométriques et logarithmiques)

**1. Racine carrée de chaque élément: `np.sqrt()`**

```python
x = np.array([4, 9, 16])
print(np.sqrt(x))	# Résultat : [2. 3. 4.]
```


**2. Sinus et cosinus : `np.sin()` et `np.cos()`**

```python
angles = np.array([0, np.pi/2, np.pi])
print(np.sin(angles))  # Résultat : [0. 1. 0.]
print(np.cos(angles))  # Résultat : [ 1. 0. -1.]
```

**3. Exponentielle de chaque élément: `np.exp()`**

```python
x = np.array([0, 1, 2])
print(np.exp(x))	# Résultat : [1. 2.71828183 7.3890561 ]
```


**4. Logarithme naturel de chaque élément : `np.log()`**

```python
x = np.array([1, np.e, np.e**2])
print(np.log(x))
# Résultat : [0. 1. 2.]
```


**5. Valeurs maximale ou minimale d'un tableau NumPy :  `np.max()` et `np.min()`**

```python
data = np.array([3, 7, 2, 9])
print(np.max(data))  # Résultat : 9
print(np.min(data))  # Résultat : 2
```


**6. Moyenne des valeurs du tableau : `np.mean()`**

```python
notes = np.array([80, 90, 100])
print(np.mean(notes))	# Résultat : 90.0
```


**7. Différences entre les éléments consécutifs du tableau : `np.diff()`**

```python
x = np.array([0, 5, 15])
print(np.diff(x))	# Résultat : [ 5 10 ]
```

> Utile en physique : vitesse ≈ variation de position / variation de temps.


## Opérations vectorisées

Avec NumPy, on peut appliquer directement les **opérations mathématiques** sur un tableau **sans utiliser de boucle**.

```python
t = np.array([0, 1, 2])
x = 3 * t**2   # applique la formule à chaque valeur. Ex: 3*0^2=0; 3*1^2=3 et 3*2^2=12

print(x)	# Résultat : [ 0  3 12]
```



## Fonctions NumPy utiles en sciences

| Fonction                              | Description                                                                        |
| ------------------------------------- | ---------------------------------------------------------------------------------- |
| `np.array()`                          | Crée un tableau NumPy à partir d’une liste Python.                                 |
| `np.arange(debut, fin, pas)`          | Crée des valeurs espacées régulièrement avec un pas fixe.                          |
| `np.linspace(debut, fin, nb_valeurs)` | Crée un nombre fixé de valeurs également espacées.                                 |
| `np.ones(n)`                          | Crée un tableau rempli de 1.                                                       |
| `np.zeros(n)`                         | Crée un tableau rempli de 0.                                                       |
| `np.sqrt(x)`                          | Racine carrée de chaque élément.                                                   |
| `np.sin(x)` / `np.cos(x)`             | Valeurs trigonométriques (radians).                                                |
| `np.exp(x)`                           | Exponentielle de chaque élément.                                                   |
| `np.log(x)`                           | Logarithme naturel de chaque élément.                                              |
| `np.max(x)` / `np.min(x)`             | Valeur maximale ou minimale du tableau.                                            |
| `np.mean(x)`                          | Moyenne des valeurs.                                                               |
| `np.diff(x)`                          | Différences entre éléments consécutifs (utile pour vitesse ou dérivées).           |
| `np.polyfit(x, y, deg)`               | Ajuste un polynôme de degré `deg` (utile pour régression linéaire ou quadratique). |

| Fonction   | Exemple        | Résultat
| ---------- | -------------- | ----------------- |
| Médiane    | `np.median(a)` | 2.5               |
| Somme      | `np.sum(a)`    | 10                |
| Produit    | `np.prod(a)`   | 24                |
| Variance   | `np.var(a)`    | 1.25              |
| Écart-type | `np.std(a)`    | 1.118033988749895 |

| Opération      | Exemple avec NumPy | Description                      | Résultat (vectorisé)    |
| -------------- | ------------------ | -------------------------------- | ----------------------- |
| Addition       | `a + b`            | addition élément par élément     | [11 22 33 44]           |
| Soustraction   | `a - b`            | soustraction élément par élément | [-9 -18 -27 -36]        |
| Multiplication | `a * b`            | produit élément par élément      | [10 40 90 160]          |
| Division       | `a / b`            | division élément par élément     | [0.1 0.1 0.1 0.1]       |
| Puissance      | `a ** 2`           | élève chaque élément au carré    | [1 4 9 16]              |
| Racine carrée  | `np.sqrt(a)`       | racine carrée de chaque élément  | [1. 1.41421356 1.73205081 2.] |
| Valeur absolue | `np.abs(a)`        | valeur absolue de chaque élément | [9 18 27 36]            |

| Fonction           | Exemple          | Résultat                    |
| ------------------ | ---------------- | --------------------------- |
| Arrondi            | `np.round(a, 2)` | arrondit à 2 décimales      |
| Plafond            | `np.ceil(a)`     | arrondi supérieur           |
| Plancher           | `np.floor(a)`    | arrondi inférieur           |
| Logarithme base 2  | `np.log2(a)`     | \$\log\_{2}(x)\$           |
| Logarithme base 10 | `np.log10(a)`    | \$\log\_{10}(x)\$           |

| Fonction                    | Exemple         | Résultat                     |
| --------------------------- | --------------- | ---------------------------- |
| Tangente                    | `np.tan(a)`     | tangente élément par élément |
| Arcsin                      | `np.arcsin(a)`  | sinus inverse                |
| Arccos                      | `np.arccos(a)`  | cosinus inverse              |
| Arctan                      | `np.arctan(a)`  | tangente inverse             |
| Conversion degrés → radians | `np.deg2rad(a)` | transforme ° en rad          |
| Conversion radians → degrés | `np.rad2deg(a)` | transforme rad en °          |

| Catégorie                         | Fonction            | Description                            | Exemple                        |
| --------------------------------- | ------------------- | -------------------------------------- | ------------------------------ |
| **Constantes**                    | `np.pi`             | Valeur de π                            | `np.pi → 3.14159…`             |
|                                   | `np.e`              | Base du logarithme naturel             | `np.e → 2.71828…`              |
|                                   | `np.arctan2(y, x)`  | Arctangente de y/x en quadrant correct | `np.arctan2(1,1) → π/4`        |
|                                   | `np.cbrt(x)`        | Racine cubique                         | `np.cbrt(27) → 3`              |
|                                   | `np.abs(x)`         | Valeur absolue                         | `np.abs(-5) → 5`               |
|                                   | `np.fabs(x)`        | Valeur absolue flottante               | `np.fabs(-5.2) → 5.2`          |
|                                   | `np.trunc(x)`       | Tronque la partie décimale             | `np.trunc(3.7) → 3`            |


## Régression linéaire avec NumPy (`np.polyfit()`)

On peut ajuster une **droite** à des données expérimentales pour modéliser une relation entre deux données (exemple : loi de Newton, vitesse moyenne).


```python
t = np.array([0, 1, 2, 3])
x = np.array([0, 2, 4.1, 6.2])
a, b = np.polyfit(t, x, 1)
print("Pente =", a, "Ordonnée =", b)
# Résultat attendu : Pente ≈ 2.05 (vitesse), Ordonnée ≈ 0.02
```


```python
import numpy as np

# Données expérimentales (temps et position)
t = np.array([0, 1, 2, 3, 4])
x = np.array([0, 2.1, 4.2, 6.1, 8.2])

# Ajustement linéaire (y = a*t + b)
a, b = np.polyfit(t, x, 1)
print("Pente (vitesse) =", a)
print("Ordonnée à l'origine =", b)
```

> Ici, la **pente correspond à la vitesse moyenne**.



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