+++
chapter = true
pre = "<b>2.</b>"
title = " Introduction à Python (Variables, types de données et algorithme)"
weight = 102
+++

## Objectifs d'apprentissage

À la fin de la leçon, vous devrez être en mesure de :

* Comprendre l'utilité des **variables** en programmation.
* Définir et utiliser des variables en Python.
* Manipuler les **types de base** en Python: `int`, `float`, `str`, `bool`.
* Afficher les résultats de manière claire et lisible.
* Comprendre le rôle d'un algorithme.
* Écrire et traduire des algorithmes simples en python.

---


## Variables et types de données de base

Une **variable** est un nom qui permet de **stocker une valeur** pour la réutiliser.

**Exemples :**

```python
age = 17
nom = "Julie"
temperature = 36.6
```

### Types de données courants

| Type    | Exemple          | Description                     |
| ------- | ---------------- | ------------------------------- |
| `int`   | `5`, `-3`        | Nombre entier                   |
| `float` | `3.14`, `-0.5`   | Nombre à virgule flottante      |
| `str`   | `"Bonjour"` ou `'Bonjour'`    | Chaîne de caractères (`string`)           |
| `bool`  | `True`, `False`  | Valeur booléenne (vrai ou faux) |

{{% notice style="cyan" title="Notez que.." %}}
Pour les données de type à virgule flottante, on utilise le point (`.`) à la place d'une virgule (`,`).
{{% /notice %}}

### Vérifier le type d’une variable

```python
age = 18
type_age = type(age)
print(type_age)  # <class 'int'>
```


## Bonnes pratiques pour nommer des variables

* Utiliser des **noms significatifs** (ex : `masse_corps`, `volume_solution`)
* Commencer par une **lettre** ou un **souligné (\_)**, jamais par un chiffre.
* Éviter les mots réservés de Python (`if`, `for`, `print`, etc.).
* Utiliser des mots séparés par des soulignés (\_).
* Utiliser des mots commençants par une lettre majuscule, sauf le premier mot (ex : `masseCorps`, `volumeSolution`).

Mauvais exemples :

```python
1age = 20       # commence par un chiffre → erreur
print = 8       # print est un mot réservé → erreur
```


## Documentation du code (les commentaires)

On écrit des **commentaires** pour expliquer le code. Python ignore tout ce qui suit `#` sur une ligne.

**Exemples :**

```python
# Calcul de l'aire d'un cercle
rayon = 3
aire = 3.14 * rayon ** 2  # formule de l’aire
```


## Opérateurs arithmétiques

| Opérateur | Signification                   | Exemple  | Résultat |
| --------- | ------------------------------- | -------- | -------- |
| `+`       | Addition                        | `3 + 2`  | `5`      |
| `-`       | Soustraction                    | `7 - 4`  | `3`      |
| `*`       | Multiplication                  | `5 * 2`  | `10`     |
| `/`       | **Division** (résultat décimal) | `6 / 2`  | `3.0`    |
| `//`      | **Division entière**            | `7 // 2` | `3`      |
| `%`       | **Modulo** (reste)              | `7 % 2`  | `1`      |
| `**`      | Puissance                       | `3 ** 2` | `9`      |

{{% notice style="cyan" title="Notez" %}}
Les differents résultats pour les trois types de division (en **gras** dans le tableau).
* [Division et division entière](http://w3.uqo.ca/adavoust/cours/expressions1.html#Division-et-division-enti%C3%A8re)   
* [Division entière et modulo](http://w3.uqo.ca/adavoust/cours/expressions1.html#Division-enti%C3%A8re-et-modulo)  
{{% /notice %}}

## Expressions et priorité des opérateurs

Une **expression** est une combinaison de variables, de nombres et d'opérateurs.

### Priorité (ordre d’exécution) des opérateurs :

1. `()` : parenthèses
2. `**` : puissance
3. `*`, `/`, `//`, `%` : multiplication et division
4. `+`, `-` : addition et soustraction

**Exemple :**

```python
resultat = 3 + 4 * 2       # donne 11, pas 14 !
resultat = (3 + 4) * 2     # donne 14 grâce aux ()
```


## Affichage des données avec *print* et les *f-string*

Quand on veut afficher une phrase contenant des **valeurs numériques ou des variables**, c'est préférable d'utiliser des **f-strings** (ou **chaînes formatées**) pour aller plus vite et rendre le code plus clair.

### Exemple

```python
nom = "Sophie"
age = 18
print(f"{nom} a {age} ans.")
```

```plaintext
Résultat : Sophie a 18 ans.
```

Le `f` devant les guillemets indique qu’on veut insérer des **valeurs de variables** directement dans le texte. On place les **variables ou calculs** entre **accolades** `{}`.

* On peut utiliser `print()` pour ajouter un saut de ligne.


## Comment décortiquer un problème scientifique en algorithme et le traduire en Python ?

**Un algorithme**, c’est une suite d’instructions claires pour résoudre un problème.

Ce processus **crucial**, est la clé pour arriver à écrire un programme sans s'arracher les cheveux. On peut le décrire en **6 étapes principales**:

1. Lire et comprendre le problème
2. Identifier les variables et constantes
3. Choisir ou écrire la formule
4. Écrire un algorithme clair
5. Traduire en code Python
6. Vérifier et tester le programme

Voyons chacune des étapes plus en détails: 

### **Étape 1 — Lire et comprendre le problème**

> **Objectif** : Identifier ce qu’on cherche, ce qu’on connaît, et le contexte scientifique.

* **Question principale** : Que doit-on calculer, prédire ou modéliser ?
* **Données** : Quelles sont les grandeurs connues ? (types ? unités ? constantes ?)
* **Formule ou loi** : Y a-t-il une relation physique, chimique ou biologique utilisable ?
* **Conditions** : Y a-t-il des limites, des cas particuliers ou des hypothèses ?


### **Étape 2 — Identifier les variables et constantes**

> **Objectif** : Repérer les quantités **variables** (entrées ou sorties) et les **constantes**.

* **Variables d’entrée** : Grandeurs connues fournies par le problème ou l’utilisateur du programme.
* **Variable de sortie** : Ce que l’on veut calculer (la réponse).
* **Constantes** : Valeurs fixes (ex. : constante des gaz, g, densité de l’eau, etc.).


### **Étape 3 — Choisir ou écrire la formule**

> **Objectif** : Traduire la relation scientifique en équation.

* Identifier la loi scientifique utilisée (ex. : Boyle, loi des gaz, loi de la gravité, etc.)
* Réorganiser si nécessaire pour isoler la variable à calculer.


### **Étape 4 — Écrire un algorithme clair**

> **Objectif** : Décrire les étapes logiques **avant** de coder.

* Définir ou lire les données (entrées)
* Calculer la sortie (résultat) avec la formule
* Afficher la réponse


### **Étape 5 — Traduire en code Python**

> **Objectif** : Écrire du code propre et commenté.


### **Étape 6 — Vérifier et tester**

> **Objectif** : Valider que le résultat est cohérent (scientifiquement et informatiquement).

* Est-ce que l’unité du résultat est correcte ?
* Est-ce que la valeur semble logique (ex. : une pression double si le volume diminue de moitié) ?
* Tester avec d’autres valeurs pour confirmer.

---

> **Exemple 1** : Un gaz occupe un volume de 4,0 L à une pression de 100 kPa. Quelle sera la pression si le volume diminue à 2,0 L (à température constante) ?

**Étape 1**: Comprendre le problème
   * On doit calculer la pression finale (P2) d'un gaz lorsque son volume final (V2) diminue de moitié.
   * On connait les volumes initial (V1) et final (V2), la pression initiale (P1).
   * On doit donc trouver la pression finale à l'aide de la Loi de Boyle (`P1 x V1 = P2 x V2`)

**Étape 2**: Identifier les variables et constantes
   * Variables d’entrée : `V1 = 4.0`, `P1 = 100`, `V2 = 2.0`
   * Variable de sortie : `P2`
   * Constantes : aucune ici
   * Type : float (car ce sont des mesures continues)

**Étape 3**: Écrire la formule
```math
Loi de Boyle : 
   $P_1 \cdot V_1 = P_2 \cdot V_2$ &nbsp Donc $P_2 = \frac{P_1 \cdot V_1}{V_2}$
```

**Étape 4**: Écrire un algorithme clair  
    **Format 1**: algorithme en phrases simples et claires  
   ```plaintxt
    * Définir les deux volumes V1 et V2 (initial et final) et la pression initiale P1.
    * Calculer la pression finale à l'aide de la formule P2 = (P1 * V1) / V2.
    * Afficher la pression finale P2.
   ```
Ou
   **Format 2**: algorithme en pseudo-code
   ```plaintxt
   Début
     Lire V1, P1, V2
     Calculer P2 = (P1 * V1) / V2
     Afficher P2
   Fin
   ```

**Étape 5**: Traduire en Python
```python
# Données d'entrée (float = nombre à virgule)
V1 = 4.0  # Volume initial en litres
P1 = 100.0  # Pression initiale en kPa
V2 = 2.0  # Volume final en litres

# Calcul (loi de Boyle)
P2 = (P1 * V1) / V2

# Affichage du résultat
print("La pression finale est de {P2} kPa")
```

**Étape 6**: Vérifier et tester

* **Test 1 — Volume initial = Volume final**

```python
V1 = 2.0
P1 = 100
V2 = 2.0
P2 = (P1 * V1) / V2 = (100 * 2.0) / 2.0 = 100.0
```

**Résultat :** `P2 = 100.0 kPa`
**Interprétation :** Si le volume ne change pas, la pression reste la même.

* **Test 2 — Volume final diminué de 4 à 1 L**

```python
V1 = 4.0
P1 = 100
V2 = 1.0
P2 = (100 * 4.0) / 1.0 = 400.0
```

**Résultat :** `P2 = 400.0 kPa`
**Interprétation :** Si on divise le volume par 4, la pression est **multipliée par 4**.

* **Test 3 — Pression initiale réduite à 50 kPa**

```python
V1 = 4.0
P1 = 50
V2 = 2.0
P2 = (50 * 4.0) / 2.0 = 100.0
```

**Résultat :** `P2 = 100.0 kPa`
**Interprétation :** Une pression initiale plus faible donne une pression finale plus faible, toutes choses égales par ailleurs.

**Conclusion**

Ces tests montrent que :

* La **pression est inversement proportionnelle au volume** : si le volume diminue, la pression augmente, et inversement.
* Le calcul respecte la **loi de Boyle** à température constante.
* Les résultats sont **cohérents avec l’intuition physique**.

> **Exemple 2 à faire à la maison** : Calculer la force gravitationnelle entre deux masses.


{{% notice style="blue" title="À retenir..." groupid="notice-toggle" expanded="false" %}}
* Une variable garde une **valeur**.
* On utilise les **bonnes pratiques** pour nommer nos variables.
* Les **commentaires** servent à documenter le code.
* Les **opérateurs arithmétiques** permettent de faire des calculs.
* Comme en mathématiques, l’ordre des opérations est **important** en Python.
* `print()` permet d'afficher une réponse, seule ou avec du texte.
* De préférence, utiliser des `f-string`.
   * Le `f` vient **juste avant** les guillemets.
   * On peut insérer n'importe quelle **variable** ou **expression** dans `{}`.
* **Avant de coder**: 
   * Comprendre le problème afin d'identifier les variables ou constantes et les formules
   * Toujours *"challenger"* les résultats obtenus, à l'aide de différentes valeurs: "Est-ce que ça a du sens scientifiquement ?"
{{% /notice %}}

---

## Exercices à faire avant le cours

{{% notice style="magenta" title="Organisation des fichiers recommandée..." groupid="notice-toggle" expanded="false"%}}
Pour chaque exercice, créez un nouveau notebook (par ex.: `exercice1.ipynb`, `exercice2.ipynb`,..., `exercice4.ipynb`) dans un **sous-dossier `exercices`** dans le dossier de la **semaine2**.
![Dossier exercices](./dossier-exercices.png?width=25vw)
{{% /notice %}}


### Exercice 1 - Calcul de probabilité

On choisit un point au hasard dans ce rectangle. Calcule la probabilité que ce point se situe dans la région grise, c’est-à-dire en dehors des cercles.
![](./probabilite.png?width=30vw)


* Un rectangle contenant **6 cercles isométriques** (même taille),
* Ils sont organisés en **2 rangées** de **3 cercles**,
* La **hauteur du rectangle est 10 cm**, ce qui correspond à **deux diamètres** de cercles (1 par rangée).

a) Identifier les variables, les constantes et les formules nécessaires
b) Écrire l'algorithme
c) Traduire l'algorithme en Python

### Résultat attendu:

```
Probabilité qu’un point tombe dans la région grise : 0.2119 (soit 21.19 %)
```

### Exercice #2 - Expérience en chimie

Un bécher contient 400 mL de solution. La solution s’évapore à raison de 25 mL/min.
La situation est linéaire : on commence à 400 mL, et on perd 25 mL chaque minute.
Donc la fonction est :
```math
$$
q(t) = 400 - 25t
$$
```
où :
* $t$ est le temps en minutes,
* $q(t)$ est la quantité de solution restante (en mL) après $t$ minutes.

On souhaite trouver la quantité de solution qu'il restera après 10 min 15 s

a) Définir les variables, constantes et formules
b) Écrire l'algorithme
c) Traduire l'algorithme en Python

**Résultat attendu** :

```
Après 10.25 minutes, il reste 143.75 mL de solution.
```

---

quel est le temps écoulé en minutes ?
> 15 secondes = 0.25 minutes
> Donc $t = 10.25$

### Code Python :

```python
# a) Fonction q(t)
def q(t):
    return 400 - 25 * t

# b) Temps écoulé en minutes
temps_minutes = 10 + 15 / 60  # 10 min 15 s = 10.25 min

# Calcul de la quantité restante
quantité_restante = q(temps_minutes)

# Affichage clair
print(f"Après {temps_minutes} minutes, il reste {quantité_restante} mL de solution.")
```

## Exercice #3 - Calcul d'intérêts simple et composé

* Vous avez deux placements avec **le même montant initial** (qu'on peut appeler `montant`).
   * **Premier placement** : intérêt **annuel simple** de **3,2 %** pendant **10 ans**.
   * **Deuxième placement** : intérêt **composé** à **1,6 % tous les 6 mois**, donc **2 fois par an**, pendant **10 ans**.

a) On cherche **l’écart en % entre les deux montants finaux** au bout de 10 ans.  
b) En déduire quel est le meilleur placement sur 10 ans.

**Hypothèse** : Comme le montant initial est le **même**, on peut le fixer à 100 \$ pour faciliter le calcul de l’écart en **pourcentage** à la fin.

**Résultat attendu** (approximatif) :

```
Valeur avec intérêt simple : 132.00 $
Valeur avec intérêt composé : 134.87 $
Écart relatif : 2.17 %
```

---

## À faire avant le prochain cours

1. Lire la matière sur [La saisie au clavier, fonctions et débogage](../semaine3/)
2. Faire les [exercices se trouvant à la fin de la leçon 3](../semaine3/#exercices-à-faire-avant-le-cours)

