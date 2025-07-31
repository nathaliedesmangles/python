+++
chapter = true
pre = "3."
title = " Structures conditionnelles et algorithmes simples"
weight = 103
+++

## Objectifs 

* Identifier et utiliser correctement les opérateurs de comparaison et logiques pour évaluer des conditions simples en Python.
* Appliquer les structures conditionnelles (`if`, `elif`, `else`) à des contextes scientifiques simples.
* Écrire des algorithmes simples et les traduire en Python.

---

## Les opérateurs de comparaison

Ces opérateurs permettent de comparer des valeurs. Le résultat est **toujours un booléen** : `True` (vrai) ou `False` (faux).

| Opérateur | Signification        | Exemple  | Résultat |
| --------- | -------------------- | -------- | -------- |
| `==`      | égal à               | `5 == 5` | `True`   |
| `!=`      | différent de         | `3 != 4` | `True`   |
| `<`       | plus petit que       | `2 < 5`  | `True`   |
| `<=`      | plus petit ou égal à | `5 <= 5` | `True`   |
| `>`       | plus grand que       | `7 > 4`  | `True`   |
| `>=`      | plus grand ou égal à | `6 >= 9` | `False`  |

> Dans une cellule de Code, testez les exemples du tableau.


## Les opérateurs logiques

Ils permettent de **combiner plusieurs conditions**.

| Opérateur | Signification            | Exemple               | Résultat |
| --------- | ------------------------ | --------------------- | -------- |
| `and`     | et (toutes vraies)       | `(4 < 5) and (6 > 3)` | `True`   |
| `or`      | ou (au moins une vraie)  | `(4 < 5) or (6 < 3)`  | `True`   |
| `not`     | négation                 | `not (4 < 5)`         | `False`  |

> Dans une cellule de Code, testez les exemples du tableau.

## Les structures conditionnelles

Elles permettent **d’exécuter un bloc de code seulement si une condition est vraie**.

### L'instruction *if*

> Pour exécuter du code **si une condition est vraie**.

```python
if condition:
    # Bloc de code exécuté si la condition est vraie
```

**Exemple :**

```python
age = 20
if age >= 18:
    print("Majeur")
```


### L'instruction *if*-*else*

> Pour exécuter du code **si une condition est fausse**.

```python
if condition:
    # Si la condition est vraie
else:
    # Sinon (condition fausse)
```

**Exemple :**

```python
age = 16
if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```


### L'instruction *if*-*elif*-*else*

> Pour tester **plusieurs cas différents** et exécuter du code différent selon le cas.

{{% notice style="accent" title="Important" %}}
* **Si la condition du `if` est fausse**, un seul `elif` sera exécuté.  
* **Si et seulement si toutes les conditions** (`if` et tous les `elif`) **sont fausses**, le `else` sera traité.
{{% /notice %}}

```python
if condition1:
    # Si condition1 est vraie
elif condition2:
    # Sinon, si condition2 est vraie
elif condition3:
    # Sinon, si condition3 est vraie
else:
    # Sinon (aucune condition vraie)
```

**Exemple :**

```python
note = 85

if note >= 90:
    print("Excellent")
elif note >= 75:
    print("Très bien")
elif note >= 60:
    print("Passable")
else:
    print("Échec")
```

{{% notice style="accent" title="Important" %}}
* **Les deux-points (`:`)** sont obligatoires à la fin des lignes `if`, `elif` et `else`.
* **L'indentation** est essentielle : elle délimite le bloc de code à exécuter.
{{% /notice %}}

> Dans des cellules de Code dans VS Code, testez les exemples des instructions `if`, `elif` et `else`.


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

{{% notice style="blue" title="À retenir" groupid="notice-toggle" expanded="false" %}}
* Les **opérateurs de comparaison** comparent des valeurs.
* Les **opérateurs logiques** combinent plusieurs conditions.
* Les **structures conditionnelles** permettent de **réagir à des critères** dans un programme.
* **Les deux-points (`:`)** sont obligatoires à la fin des lignes `if`, `elif` et `else`.
* **L'indentation** (souvent 4 espaces) est essentielle : elle délimite le bloc de code à exécuter.
* Il peut y avoir **autant de `elif` que nécessaire**, mais **un seul `if` et au plus un seul `else`**.
	* `if` vérifie si une condition est vraie, **si et seulement si c'est le cas**, les instructions en dessous seront exécutées.
	* `elif` permet de vérifier une autre condition, **si et seulement si la condition du `if` est fausse ET celle du `elif` est vraie**, les instructions en dessous et décalées seront exécutées.
	* `else` permet de prévoir des instructions à effectuer, **si et seulement si aucune des conditions précédentes n'est vraie**.

* **Avant de coder**: 
    * Comprendre le problème afin d'identifier les variables ou constantes et les formules.
    * Écrire en phrases simples, les étapes principales du programme (l'algorithme).
{{% /notice %}}

---

## Exercices

### Exercice 1 – Temps de demi-vie radioactive

Un isotope radioactif se désintègre avec le temps. Sa masse diminue de moitié à chaque période de demi-vie.
Un échantillon de 100 g d’un isotope a une demi-vie de 5 ans. On souhaite connaître la masse restante après un certain nombre d’années.

1. Écris un algorithme permettant de :

   * Demander à l’utilisateur le nombre d’années écoulées.
   * Calculer le nombre de périodes de demi-vie.
   * Calculer la masse restante :
     $$
     \text{masse} = \text{masse initiale} \times \left(\frac{1}{2}\right)^{\text{nb\_periodes}}
     $$
   * Si la masse est inférieure à 1 g, afficher un message d’avertissement, sinon, afficher la masse restante normalement.

2. Traduis ton algorithme en Python.


### Exercice 2 – Taux de croissance d’une population bactérienne

Une colonie de bactéries double toutes les 3 heures si les conditions sont optimales.
Une boîte de Pétri contient 500 bactéries. On souhaite estimer la taille de la population après un certain nombre d’heures.

1. Écris un algorithme pour :

   * Demander à l’utilisateur le nombre d’heures écoulées.
   * Calculer le nombre de périodes de croissance (périodes de 3 heures).
   * Calculer la population après cette durée avec la formule :
     $$
     \text{population} = \text{population initiale} \times 2^{\text{nb\_periodes}}
     $$
   * Afficher la population estimée.
   * Si la population dépasse 1 000 000 bactéries, afficher un message d’alerte sur la croissance excessive, sinon afficher la population normalement

2. Traduis ton algorithme en Python.



### Exercice 3 – Température critique d’un liquide

Un liquide ne doit pas dépasser **80 °C** pour rester stable.
Demander à l’utilisateur la température actuelle du liquide et **afficher un message** selon les cas :

* Si la température est **inférieure à 80**, afficher : « Température sécuritaire. »
* Si elle est **exactement 80**, afficher : « Limite atteinte. »
* Si elle est **supérieure à 80**, afficher : « Attention : température critique ! »


### Exercice 4 – Classification du pH d’une solution

En chimie, le **pH** permet de savoir si une solution est acide, neutre ou basique.
Demander à l’utilisateur le **pH** d’une solution (entre 0 et 14), puis afficher :

* « Solution acide » si `pH < 7`
* « Solution neutre » si `pH == 7`
* « Solution basique » si `pH > 7`
* « Valeur de pH invalide » si le pH est en dehors de l’intervalle `[0, 14]`


### Exercice 5 – Autorisation d’une réaction chimique

Une réaction chimique ne peut avoir lieu **que si** la température est **entre 25 °C et 45 °C inclusivement**, **et** si le **pH est entre 6 et 8 inclusivement**.

Demander à l’utilisateur la température et le pH, puis afficher :

* « Réaction possible. » si les deux conditions sont remplies,
* « Conditions non compatibles. » sinon.


---

## Atelier 3

### Exercice 1

L’état physique de l’eau dépend de la température et de la pression. À **pression atmosphérique normale (1 atm)** :

* L’eau gèle à 0 °C et bout à 100 °C.
* En **altitude**, la pression est plus faible, donc l’eau bout à une température plus basse.
* En **autocuiseur**, la pression est plus élevée, donc l’eau bout à une température plus élevée.

On suppose ici un modèle très simple :

| Pression (atm) | Température d’ébullition (°C) |
| -------------- | ----------------------------- |
| 0.5            | 81                            |
| 1.0            | 100                           |
| 1.5            | 112                           |
| 2.0            | 120                           |

Le point de congélation demeure à 0 °C peu importe la pression.

Écris un programme Python qui :

1. Demande à l’utilisateur d’entrer :

   * La **température de l’eau en °C**
   * La **pression en atm** (choix parmi 0.5, 1.0, 1.5, 2.0)

2. Détermine et affiche l’**état physique de l’eau** : `"solide"`, `"liquide"` ou `"gaz"`.


### Exemples de fonctionnements attendus

```text
Température (°C) : 50
Pression (atm) : 1.0
État de l’eau : liquide
```

```text
Température (°C) : 101
Pression (atm) : 1.0
État de l’eau : gaz
```

```text
Température (°C) : -5
Pression (atm) : 2.0
État de l’eau : solide
```

### Pistes / rappels

* Utiliser des conditions imbriquées ou combinées (`if ... and ...`, `elif`).
* Pour simplifier, vous pouvez faire un `if` sur la pression pour définir le point d’ébullition.
* Utilisez des variables pour stocker les seuils.

### Exemple d’exécution

```
Température de l'eau en °C : 105
Pression en atm (0.5, 1.0, 1.5 ou 2.0) : 1.5
sÉtat de l’eau : liquide
L’eau est liquide à cette température et pression.
```

### Version améliorée

* Gérer des cas d’erreurs (ex. : pression invalide)
* Afficher une petite phrase plus descriptive selon l’état :
* *"L’eau est sous forme de vapeur."* ou *"L’eau est liquide à cette température et pression."*

{{% notice style="magenta" title="Gérer des cas d'erreur: Utiliser la valeur None" groupid="notice-toggle" expanded="false" %}}

### Qu’est-ce que `None` en Python ?

* `None` est une **valeur spéciale** en Python.
* Elle représente **l'absence de valeur** ou **"rien"**.

### Pourquoi utiliser `None` ?

* Pour **vérifier si une variable est encore vide**.
* Pour **initialiser une variable** sans lui donner de valeur tout de suite.
* Pour **indiquer qu’une fonction ne retourne rien**.

---

### Exemple 1 – Vérifier si une variable est vide

```python
reponse = None

if reponse is None:
    print("Aucune réponse reçue.")
```

> Attention : on teste `None` avec `is` et non `==` dans les bonnes pratiques Python :

```python
if variable is None:
   

### Exemple 2 – Variable vide au départ

```python
resultat = None  # on ne connaît pas encore le résultat

# plus tard...
resultat = 42
```

### Exemple 3 – Fonction sans return

```python
def afficher_message():
    print("Bonjour!")

x = afficher_message()
print(x)  # Affiche : None (car la fonction ne retourne rien)
```
{{% /notice %}}

---

## À faire avant le prochain cours

1. Lire la prochaine leçon : [4. Boucles et algorithmes simples](../semaine4/)
2. Faire les exercices de la [prochaine leçon :](../semaine4/#exercices)