+++
chapter = true
pre = "7."
title = " Tableaux numpy et droite de régression"
weight = 107
draft = false
+++


## Objectifs

* Créer des **tableaux de données** à une ou deux dimensions.
* Calculer des **moyennes** et **écarts types**.
* Gérer des données **expérimentales incomplètes** (`np.nan`).
* Comparer des résultats entre éléments ou conditions.
* Filtrer des données selon des conditions.
* Tracer un graphique à barres muni d'une barre d'erreur avec `matplotlib`.
* Tracer une droite de régression et interpréter la pente, l’ordonnée à l’origine et le coefficient de détermination R²
* Établir une relation entre deux données

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
4. Dans VS Code, recherchez et ouvrez le fichier `exercices_boucles.ipynb`
5. Assurez-vous que le noyau Python (`Kernel`) soit sélectionné.
6. Vous pouvez commencer à faire les exercices.


## Exercice 1 – Solubilité d’un sel

On a mesuré la solubilité (en g/100 mL) d’un sel à différentes températures. Les données sont stockées dans un tableau NumPy :

```python
import numpy as np
sol = np.array([32.0, 35.5, np.nan, 37.2, 39.0])
```

1. **Afficher le tableau** `sol` pour visualiser les valeurs de solubilité (remarque : une valeur est manquante et représentée par `np.nan`).
2. **Calculer la moyenne des solubilités** en ignorant la valeur manquante.

   * Cherche dans NumPy une fonction qui calcule la moyenne en excluant les `NaN`.
3. **Calculer l’écart type** des valeurs (toujours en ignorant `NaN`).

   * Arrondis le résultat à **2 décimales** avec `round()`.
   * Affiche ton résultat sous la forme : `Écart type : valeur`.

**Exemple de sortie attendue** :
```
Solubilités : [32.  35.5  nan 37.2 39. ]
Moyenne sans NaN : 35.925
Écart type : 2.58
```


## Exercice 2 – Températures journalières

Un thermomètre a enregistré la température **3 fois par jour (matin, après-midi, soir)** pendant **7 jours consécutifs**.
Ces données sont stockées dans un tableau NumPy à deux dimensions :

```python
temperatures = np.array([
    [12.1, 17.3, 14.2],  # Jour 1
    [11.8, 16.9, 13.9],  # Jour 2
    [13.0, 18.1, 15.0],  # Jour 3
    [12.5, 17.5, 14.7],  # Jour 4
    [np.nan, 16.0, 14.0],# Jour 5 (valeur manquante le matin)
    [13.2, 18.0, 15.2],  # Jour 6
    [12.0, 17.0, 14.5]   # Jour 7
])
```

1. **Structure du tableau**
   * Quelle est la *forme* (`shape`) de ce tableau ?
   * Combien y a-t-il de lignes et de colonnes ? Que représentent-elles ?

2. **Moyenne par jour**
   * Calcule la **température moyenne quotidienne** pour chaque jour.
     *(Indice : tu peux utiliser `np.mean(..., axis=1)`)*

3. **Moyenne du matin**
   * Calcule la **température moyenne du matin** (1ʳᵉ colonne du tableau).
   * **Attention** : il y a une donnée manquante (`np.nan`). Comment peux-tu l’ignorer dans ton calcul ?
     *(Indice : utilise `np.nanmean(...)` sur la colonne du matin)*


**Résultats attendus** :
```
Forme : (7, 3)
Moyennes journalières : [14.53333333 14.2        15.36666667 14.9        15.         15.46666667
 14.5       ]
Moyenne du matin : 12.433333333333332
```


## Exercice 3 – Analyse d’ADN

On a mesuré l’intensité de **5 fragments d’ADN** (valeurs arbitraires) pour **deux échantillons**. Ces intensités sont stockées dans des tableaux NumPy :

```python
import numpy as np

ech1 = np.array([3.2, 2.8, 4.1, 3.9, 2.5])
ech2 = np.array([2.9, 3.0, 4.2, 4.0, 2.7])
```

1. **Profil combiné** : additionne directement les deux tableaux `ech1` et `ech2` pour obtenir un nouveau tableau qui représente la somme des intensités fragment par fragment.
   * **Indice** : tu peux utiliser l’opérateur `+` avec des tableaux NumPy.  

2. **Différences entre échantillons** : calcule la différence `ech1 - ech2`.  
   * **Indice** : fais attention à l’ordre, car `ech1 - ech2` n’est pas la même chose que `ech2 - ech1`.

3. **Statistiques** :
   * Calcule la **moyenne** de chaque échantillon (`np.mean`).
   * Calcule l’**écart type** de chaque échantillon (`np.std`).
   * Arrondis les résultats à **2 décimales** (`round(..., 2)`).

**Résultats attendus** :
```
Profil combiné : [6.1 5.8 8.3 7.9 5.2]
Différence : [ 0.3 -0.2 -0.1 -0.1 -0.2]
Moyenne éch1 : 3.3
Écart type éch1 : 0.62
Moyenne éch2 : 3.36
Écart type éch2 : 0.62
```



## Exercice 4 – Pression en fonction de la hauteur dans un cylindre

On mesure la pression (en kPa) à différentes hauteurs (en cm) dans un cylindre rempli d’air :

```python
import numpy as np

hauteur = np.linspace(0, 50, 6)  # [0, 10, 20, 30, 40, 50]
pression = np.array([101.3, 100.0, 98.7, 97.5, 96.2, 95.0])
```

1. **Affichage des données**
   * Affiche le tableau des hauteurs en cm.
   * Affiche le tableau des pressions en kPa.

2. **Variation de pression**
   * Calcule la différence de pression entre deux hauteurs consécutives (chaque 10 cm).
   * Affiche le tableau des variations obtenues.

3. **Moyenne de la pression**
   * Calcule la moyenne des valeurs de pression.
   * Affiche-la avec **2 chiffres après la virgule**.

4. **Graphique avec régression linéaire**
   * Trace un nuage de points (`plt.scatter()`) représentant la pression en fonction de la hauteur.
   * Ajoute la droite de régression linéaire sur le même graphique.
   * Mets un titre et des étiquettes aux axes (`plt.xlabel`, `plt.ylabel`).

**Exemple attendu (partiel)** :
```
Hauteur (cm) : [ 0. 10. 20. 30. 40. 50.]
Pression (kPa) : [101.3 100.   98.7  97.5  96.2  95. ]
Variation de pression par 10 cm : [-1.3 -1.3 -1.2 -1.3 -1.2]
Moyenne de pression : 98.12 kPa
```
![Graphique nuage et regression](./graphique_pression_regression.png?width=35vw)



## Exercice 5 – Croissance d’une plante (modélisation simplifiée)

On veut modéliser la croissance d’une plante.
Sans engrais, sa taille **augmente de 2 cm par jour**, en partant d’une taille initiale de **5 cm**.

1. **Créer un tableau NumPy** qui contient la taille de la plante chaque jour pendant 10 jours (jour 0 à jour 9).   
   **Indice** : utilise `np.arange()` ou construis le tableau à partir d’une liste.
2. **Afficher ce tableau** pour vérifier qu’il correspond à la croissance sans engrais.
3. **Créer un deuxième tableau** où tu ajoutes **+1 cm** à chaque valeur du premier tableau (effet de l’engrais).
4. **Calculer la moyenne** des tailles de la plante :
   * une fois **sans engrais**,
   * une fois **avec engrais**.  
     **Indice** : utilise la fonction `np.mean()`.

**Résultats attendus** :
```
Taille sans engrais : [ 5  7  9 11 13 15 17 19 21 23]
Taille avec engrais : [ 6  8 10 12 14 16 18 20 22 24]
Moyenne sans engrais : 14.0 cm
Moyenne avec engrais : 15.0 cm
```


---

# Cours

## Importer la bibliothèque

```python
import numpy as np
```

## Créer des tableaux de données (`array`)

### Tableau 1D via un liste et np.array()

```python
sol = np.array([32.0, 35.5, 37.2])
print(f"Solubilités mesurées : {sol}")
```

### Tableau 2D via une liste de listes et np.array()

* Un **tableau numpy** multidimentionnel c'est un **tableau numpy** qui contient **une liste de listes**.

```python
matrice = np.array([[1, 2], [3, 4]])
print(matrice.shape)     # Affiche les dimensions (2 lignes, 2 colonnes)
```

## Créer des tableaux remplis d’une même valeur

### Rempli de 0

* `np.zeros(forme)`: créer un tableau rempli uniquement de `0`
* `forme` = dimensions du tableau (ex. `(2,3)` → 2 lignes, 3 colonnes).

**Exemple** :
```python
tab_zeros = np.zeros((2, 3))  # Crée un tableau de 2 lignes et 3 colonnes rempli de 0
```

### Rempli de 1

* `np.ones(forme)` : créer un tableau rempli uniquement de `1`.
* `forme` = dimensions du tableau (ex. `(3,2)` → 3 lignes, 2 colonnes).

**Exemple** :
```python
tab_uns = np.ones((3, 2))  # Crée un tableau de 3 lignes et 2 colonnes rempli de 1
```

### Rempli d'une autre valeur

* `np.full(forme, valeur)` : créer un tableau rempli avec une **valeur choisie**.
* `forme` = dimensions du tableau (ex. `4` → 1D avec 4 éléments).
* `valeur` = nombre à répéter (ex. `0.5`).

**Exemple** :
```python
tab_demi = np.full(4, 0.5)  # Crée un tableau [0.5, 0.5, 0.5, 0.5]
```

### Rempli de valeurs espacées régulièrement (utile pour les graphiques)

* `np.linspace(debut, fin, nb)` : créer un tableau de `nb` valeurs **réparties régulièrement** entre `debut` et `fin` (inclus).
  * `debut` = première valeur.
  * `fin` = dernière valeur.
  * `nb` = nombre total de valeurs.

```python
tab_esp = np.linspace(0, 10, 5)  # Crée un tableau : [ 0.  2.5  5.  7.5 10. ]
```


## Fonctions statistiques

### Calculer la moyenne des données

```python
sol = np.array([32.0, 35.5, 37.2])
moy = np.mean(sol)
print(f"Moyenne : {moy:.2f} g/100mL")
```


### Calculer l’écart type des données

```python
sol = np.array([32.0, 35.5, 37.2])
ecart = np.std(sol)
print(f"Écart type : {ecart:.2f}")
```

## Opérations vectorielles (rapides et simples)

L’intérêt principal de NumPy : on peut faire des **opérations sur tout un tableau en une seule ligne**.

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
```

### Addition élément par élément

```python
x + y    # [5 7 9]
```

### Soustraction élément par élément

```python
y - x    # [3 3 3]
```

### Multiplication par un scalaire

```python
x * 10   # [10 20 30]
```

### Division par un scalaire

```python
y / 2    # [2.  2.5 3. ]
```

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

1. Créer un tableau et afficher uniquement certaines valeurs selon une condition

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

2. Comptage conditionnel avec `np.sum`

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

---

{{% notice style="blue" title="À retenir" groupid="notice-toggle" expanded="false" %}}
* `import numpy as np` pour utiliser NumPy.
* `np.array()` crée un tableau de données.
* `np.zeros()`, `np.ones()`, `np.full()` créent des tableaux remplis.
* `np.linspace()` génère des valeurs espacées régulièrement.
* `np.mean()` calcule la moyenne.
* `np.std()` calcule l’écart type.
* `np.nanmean()` ignore les données manquantes.
* Les opérations (`+`, `-`, `*`, `/`) s’appliquent à tout le tableau.
{{% /notice %}}


## Tracer un graphique à barres avec barre d'erreurs

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

La fonction `plt.errorbar()` permet de tracer des barres d'erreur autour des points d'une courbe, et ici la liste `erreurs = [0.5, 0.3, 0.6]` indique l'incertitude verticale (±) associée à chaque point.

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

* `a, b = np.polyfit(x, y, 1)` : On calcule la droite qui s'ajuste le mieux aux points (régression linéaire) et on récupère sa pente (`a`) et son intercept (`b`).
* `y_reg = a * x + b` : On utilise la pente et l'intercept pour calculer les valeurs de la droite.
* `plt.plot(x, y, "o", label="Données")` : On trace les points de données sous forme de cercles.
* `plt.plot(x, y_reg, "-", label=f"y = {a:.2f}x + {b:.2f}")` : On trace la droite de régression et on affiche son équation.

### Exemple

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
plt.tight_layout()
plt.show()
```
![graphique droite de régression](./graphique_regression.png?width=40vw)

## Affichage propre

| Fonction             | Effet                                            |
| -------------------- | ------------------------------------------------ |
| `plt.tight_layout()` | Ajuste l'espacement pour éviter le chevauchement 



## Résumé

| Tâche                | Fonction                           |
| -------------------- | ---------------------------------- |
| Graphique à barres   | `plt.bar()`                        |
| Barres d’erreur      | `plt.errorbar()`                   |
| Droite de régression | `np.polyfit()`, `plt.plot()`       |
| Affichage final      | `plt.show()`, `plt.tight_layout()` |

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

### Aide

* `numpy.array()` pour créer le tableau.
* `np.nanmean()` et `np.nanstd()` pour les calculs.
* `np.arange(len(conditions))` pour créer les positions des barres.
* `plt.bar()` et `plt.errorbar()` (ou l’argument `yerr`) pour tracer les moyennes avec barres d’erreur.
* `plt.xticks()` pour afficher correctement les noms des conditions.



---

## À faire avant le prochain cours

1. Lire la prochaine leçon : [8. Dictionnaires](../semaine8/)
2. Faire les exercices de la [prochaine leçon :](../semaine8/#exercices)