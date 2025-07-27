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

### Exercice 4 : Distance parcourue

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

> **RAPPEL**: Semaine prochaine c'est le **premier examen** (20%)

1. Lire la matière sur [Décider avec if, elif, else](../semaine4/)
2. Faire les [exercices se trouvant à la fin de la leçon 4](../semaine4/#exercices-à-faire-avant-le-cours)