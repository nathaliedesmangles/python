+++
chapter = true
pre = "<b>2.</b>"
title = " Introduction à Python (Variables, types de données et algorithme)"
weight = 102
+++

## Objectifs

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

* La fonction  `print()` permet d'afficher des résultats.
* On peut aussi utiliser `print()` pour ajouter un saut de ligne.

* Quand on veut afficher une phrase contenant des **valeurs numériques ou des variables**, c'est préférable d'utiliser des **f-strings** (ou **chaînes formatées**) pour aller plus vite et rendre le code plus clair.

**Exemple** :

```python
nom = "Sophie"
age = 18
print(f"{nom} a {age} ans.")
```

```plaintext
Résultat : Sophie a 18 ans.
```

* Le `f` devant les guillemets indique qu’on veut insérer des **valeurs de variables** directement dans le texte. On place les **variables** entre **accolades** `{}`.

* Mais parfois, on veut afficher **un nombre arrondi**, **aligné**, ou **avec des zéros**. C’est là qu’on utilise les **modificateurs de format** juste après la variable, entre `:` et `}`.


### Les modificateurs de format numérique

| Objectif                                | Syntaxe           | Exemple de résultat |
| --------------------------------------- | ----------------- | ------------------- |
| Afficher **2 décimales**                | `{valeur:.2f}`    | `3.14`              |
| Afficher **avec des zéros devant**      | `{valeur:06.2f}`  | `003.14`            |
| **Aligner à droite** sur 10 caractères  | `{valeur:>10.2f}` | `      3.14`        |
| **Aligner à gauche** sur 10 caractères  | `{valeur:<10.2f}` | `3.14      `        |
| **Pourcentage** avec 1 décimale         | `{valeur:.1%}`    | `314.2%`            |
| Format **scientifique** (notation exp.) | `{valeur:.2e}`    | `3.14e+00`          |


**Exemples** :

```python
montant = 134.8678
print(f"Montant : {montant:.2f} $")        # → Montant : 134.87 $
print(f"Montant : {montant:10.2f} $")      # → Montant :     134.87 $
print(f"Montant : {montant:<10.2f} $")     # → Montant : 134.87     $ 
print(f"Montant : {montant:>10.2f} $")     # → Montant :     134.87 $
print(f"Montant : {montant:^10.2f} $")     # → Montant :   134.87   $
```

**Explication** :

* `.2f` → **f** pour "float", **2** pour eux décimales
* `10.2f` → total de 10 caractères, dont 2 après la virgule
* `<`, `>`, `^` → alignement (gauche, droite, centré)


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

[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/2_intro/exercices_intro.ipynb)

## Exercice 1 : Conversion de température

Un thermomètre donne des relevés en Fahrenheit, mais vous devez les convertir en Celsius et Kelvin.

1. Utilisez une variable pour stocker une température en °C.
2. Convertissez cette température en °F et en K.
3. Affichez les trois valeurs avec des messages clairs.

**Formules** :
```math
$ °F = (°C × 9/5) + 32 $  <br> 
$ K = °C + 273.15 $
```

**Résultat attendu avec une température de 38°C** :
```
Température en Celsius : 38°C
Température en Fahrenheit : 100.4°F
Température en Kelvin : 311.15K
```
---

## Exercice 2 : Calcul de concentration molaire

Un technicien prépare une solution en dissolvant une masse donnée de soluté dans un certain volume de solvant.
Écrire un programme qui calcule la concentration molaire (mol/L) selon la formule :
```math
$ C = n / V $ où  $ n = m / M $
```

**Résultat attendu avec** :  
m = 10.0 	masse du soluté en grammes  
M = 58.5	masse molaire du soluté en g/mol (ex. NaCl)  
V = 0.25	volume de la solution en litres  

```
Concentration molaire : 0.682051282051282 mol/L
```
---

## Exercice 3 : Vitesse moyenne d’une réaction

Lors d’une expérience de cinétique chimique, on mesure la variation de la concentration d’un réactif au cours du temps.
Écrire un programme qui calcule la vitesse moyenne de disparition selon :

```math
$ v = \frac{\Delta [A]}{\Delta t} $
```

où `[A]` est la concentration du réactif.

**Résultat attendu avec**:  \[Réactif A] passe de 0.80 mol/L à 0.20 mol/L en 120 secondes.

```
Vitesse moyenne = -0.005000 mol L⁻¹ s⁻¹
```
---

## Exercice 4 : Distance parcourue

Un cycliste roule à une vitesse constante de 6,5 m/s pendant 12 minutes.

1. **Écris l’algorithme en phrases** pour calculer la distance parcourue.
2. **Implémente l’algorithme en Python**`.
3. **Affiche la distance parcourue avec une phrase complète.**

**Résultat attendu**:
```
Le cycliste a parcouru 4680.0 mètres en 12 minutes.
```
---

## À faire avant le prochain cours

1. Lire la matière sur [La saisie au clavier, fonctions et débogage](../semaine3/)
2. Faire les [exercices se trouvant à la fin de la leçon 3](../semaine3/#exercices-à-faire-avant-le-cours)

