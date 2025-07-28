+++
chapter = true
pre = "<b>3.</b>"
title = " Algorithme et débogage"
weight = 103
+++

## Objectifs 

À la fin de la leçon, vous devrez être en mesure de :

* Écrire des algorithmes simples et les traduire en Python.
* Comprendre les messages d'erreurs et à apprendre à déboguer un programme.

---

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


## Trouver facilement les sources des erreurs dans nos programmes (débogage)

**Déboguer**, c’est trouver les causes des erreurs dans le cod, afin de les corriger rapidement.

### Types d’erreurs fréquentes

* **Erreur de syntaxe** : La syntaxe de Python n'est pas respectée. Ex.: `print("Bonjour'`
* **Erreur d’exécution** : Le mauvais type de données est utilisé. Ex.: `valeur = int("abc")`
* **Erreur de logique** : Les instructions ne correspondent pas à la logique imposée par le problème. Ex.: `aire = longueur + largeur`
 

### Quelques habitudes à avoir pour déboguer

* Lire le message d’erreur affiché
* Ajouter des ***print()*** pour suivre les valeurs.
* Corriger les erreurs dans l'**ordre de leur apparition**, car 1 erreur, peut soit en cacher ou être la cause d'autres erreurs.
* Tester **une ligne à la fois**.
* Se poser la question : "Est-ce que le résultat est correct ?".
* Vérifier les types des données avec *type()*.


### Exemple de code présentant des erreurs

**Énoncé du problème**

Ce programme est censé calculer le temps nécessaire pour qu’un objet tombe d’une certaine hauteur `h` en chute libre (sans frottement), en utilisant la formule :

```math
$$
t = \sqrt{\frac{2h}{g}}
$$
où $g = 9.8 \, m/s^2$ est l’accélération gravitationnelle.
```
> Malheureusement, le programme contient des erreurs. Utilisez des `print()` pour comprendre ce qui ne fonctionne pas, puis corrigez le code.

**Code à déboguer**
```python
import math

def temps_chute(hauteur):
g = "9.8"
    t = math.sqrt(2 * hauteur / g)
    return t

h = input("Entrez la hauteur de chute en mètres: ")

temps = temps_chute(h)

print("Le temps de chute est {temps} secondes.")
```

{{% notice style="magenta" title="Correction attendue" groupid="notice-toggle" expanded="false" %}}
**Erreurs intégrées** :
1. Erreur d'indentation : définition de `g` n'est dans le corps de la fonction.
2. `g = "9.8"` : valeur gravitationnelle en chaîne de caractères → provoquera une erreur de type.
3. `input()` retourne une chaîne → doit être convertie en `float()`.
4. Il manque `f` dans le `print()` final.
5. Le type de la variable `hauteur` dans `temps_chute()` est incorrect (chaîne).
```python
import math

def temps_chute(hauteur):
    g = 9.8

    # Vérification du type de g
    print(type(g))

    t = math.sqrt(2 * hauteur / g)

    # vérification de la valeur de t
    print(f"Temps de chute calculé: {t}")

    return t 

h = float(input("Entrez la hauteur de chute en mètres: "))

# vérification de la valeur de h
print(f"Hauteur entrée: {h}")

temps = temps_chute(h)

print("Le temps de chute est {temps} secondes.")
```
{{% /notice %}}

{{% notice style="blue" title="À retenir" groupid="notice-toggle" expanded="false" %}}
* **Avant de coder**: 
    * Comprendre le problème afin d'identifier les variables ou constantes et les formules.
    * Écrire en phrases simples, les étapes principales du programme (l'algorithme).
* Utiliser la fonction `print()` pour suivre l'exécution d'un programme et identifier les bogues.
* Toujours *"challenger"* les résultats obtenus, à l'aide de différentes valeurs: "Est-ce que ça a du sens scientifiquement ?"
{{% /notice %}}

---

## Exercices à faire avant le cours

### Exercice 1 – Temps de demi-vie radioactive

Un isotope radioactif se désintègre avec le temps. Sa masse diminue de moitié à chaque période de demi-vie.
Un échantillon de 100 g d’un isotope a une demi-vie de 5 ans. On souhaite connaître la masse restante après un certain nombre d’années.

1. Écris un algorithme permettant de :

   * Demander à l’utilisateur combien d’années se sont écoulées.
   * Calculer le nombre de périodes de demi-vie.
   * Calculer la masse restante à partir de la formule :

     $$
     \text{masse} = \text{masse initiale} \times \left(\frac{1}{2}\right)^{\text{nb\_periodes}}
     $$
   * Afficher le résultat.

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

2. Traduis ton algorithme en Python.


### Exercice 3 : Trouvez les erreurs et corrigez les

> Ce programme est censé calculer la surface d’un cône droit à partir du rayon et de la hauteur entrés par l’utilisateur. La formule utilisée est :
```math
$$
\text{Surface} = \pi \cdot r \cdot (r + \sqrt{r^2 + h^2})
$$
```
> Toutefois, des erreurs se sont glissées dans le programme. Utilisez des instructions `print()` pour comprendre les erreurs, puis corrigez-les une à une et exécutez le code après chaque correction avant de passer à l'erreur suivante.

**Code à déboguer et corriger** :

```python
def surface_cone(rayon, hauteur):
    aire_base = math.pi * rayon ** 2
    aire_lateral = math.pi * rayon * math.sqrt(rayon**2 + hauteur)
    surface = aire_base + aire_latérale
    return surface

r = input("Entrez le rayon du cône: ")
h = input("Entrez la hauteur du cône: ")

resultat = surface_cone(r, h)

print("La surface totale du cône est de {resultat} cm²")
```

---

## À faire avant le prochain cours

1. Lire la matière sur [Décider avec if, elif, else, répéter avec `while`](../semaine4/)
2. Faire les [exercices se trouvant à la fin de la leçon 4](../semaine4/#exercices-à-faire-avant-le-cours)