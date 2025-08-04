+++
chapter = true
pre = "11."
title = " Fonctions personnalisées"
weight = 111
draft = false
+++

## Objectifs

* Définir vos propres fonctions avec `def` (paramètres, `return`, portée locale)
* Documenter les fonctions personnalisées (`docstring`)

---

## Création de fonction avec `def`
 
> Une fonction peut:
   > 1. Afficher un résultat (ex: `print()`)
   > 2. Retourner un résultat (ex: `input()`)


### Comment créer et utiliser une fonction ?

1. On utilise le mot clé `def`.
2. Suivi du nom de la fonction.
3. Suivi de parenthèses `()`.
4. Suivi de deux-points `:`.
5. Les instructions de la fonction sont sur les lignes d'en dessous, décalées. Ce décalage, permet à Python de reconnaitre le code qui appartient à la fonction et qui sera exécuté lors de son utilisation. 
L'absence de ce décalage (**indentation**) provoque l'erreur ***IndentationError***.

```python
IndentationError: expected an indented block after function definition on line X
```

{{% notice style="accent" title="Important" %}}
* Les règles de **nomenclature des variables**, s'appliquent aussi aux noms de fonctions.
* Entre les parenthèses, on peut indiquer des **paramètres ou pas**, mais les **parenthèses sont obligatoires**.
{{% /notice %}}

#### Syntaxes générales

**Une fonction qui affiche le résultat** :
```python
def nom_fonction(param1, param2): # <--- Les deux-points 
    instructions
    print(résultat) # <--- La fonction se termine ici
```

**Exemple** :

```python
# Définition de la fonction
def aire_rectangle(longueur, largeur):
    aire = longueur * largeur
    print(f"L'aire du rectangle de longueur {longueur} et de largeur {largeur} est {aire} cm^2") 
```

> Cette fonction reçoit deux valeurs (longueur et largeur du rectangle), calcule l’aire du rectangle et **affiche** l'aire.

**Une fonction qui retourne le résultat** :

```python
def nom_fonction(param1, param2):
    instructions
    return résultat # <---- La fonction se termine ici
```

**Exemple** :

```python
# Définition de la fonction
def aire_rectangle(longueur, largeur):
    aire = longueur * largeur
    return aire  
```

> Cette fonction reçoit deux valeurs (longueur et largeur du rectangle), calcule l’aire du rectangle et la **retourne**.

#### Le mot-clé `return`

* Il **renvoie un résultat** à l’endroit où la fonction a été utilisée (appelée).
* Dès que `return` est exécuté, la fonction **s’arrête**.


#### Appeler (utiliser) une fonction

**Utilisation de la fonction `aire_rectangle()` qui **affiche** l'aire**

```python
# Appel de la fonction
aire_rectangle(5, 2)
```
> Les valeurs utilisées entre les parenthèses seront utilisées par la fonction.
> Ici, 5 est la valeur pour la longueur et 2 celle de la largeur.

**Utilisation de la fonction `aire_rectangle()` qui **retourne** l'aire**

```python
surface = aire_rectangle(5, 2) # Appel de la fonction
print(f"L'aire du rectangle est : {surface}")
```
> Notez la différence: Ici, **il faut stocker le résultat de la fonction dans une variable**.

On aurait aussi pu faire:
```python
print(f"L'aire du rectangle est : {aire_rectangle(5, 2)}") # Appel de la fonction
```


### La portée locale des variables

Les **variables créées **à l'intérieur** d'une fonction** (ex: `aire`) **n’existent que dans la fonction**.

**Exemple** :

```python
def test():
    x = 10  <---- On peut utiliser x qu'à l'intérieur de la fonction.
    return x <---- Après cette ligne, x n'existe plus. 

print(test())  # OK, affiche 10
print(x)       # Erreur : x n'existe pas ici
```
![Erreur de nom](./erreur_name.png?width=35vw)

## Documenter ses fonctions (*docstrings*)

Les ***docstrings*** sont des chaînes de caractères utilisées pour documenter les fonctions. Elles sont placées juste après la définition de la fonction.

**Format standard**
```python
def nom_fonction(param):
    """
    Description de la fonction.

    Paramètres:
    - param (type): Description.

    Retour:
    - type: Description.
    """
```

**Exemple** :
```python
def addition(a, b):
    """
    Calcule la somme de deux nombres.

    Paramètres:
    a (int, float): Le premier nombre.
    b (int, float): Le deuxième nombre.

    Retour:
    int, float: La somme des deux nombres.
    """
    return a + b
```


{{% notice style="cyan" title="À retenir" groupid="notice-toggle" expanded="false" %}}
* `def` : sert à définir une fonction 
* ***nom_fonction(paramètres)*** : Les paramètres sont les variables représentant les données dont la fonction a besoin pour obtenir le résultat.                   
* `return` : Permet à la fonction de retourner un résultat (`resultat = fonction()` ou <br> `print(fonction())`)
* **Portée locale** : Signifie que les variables dans une fonction n’existent qu’à l’intérieur de .elle-ci|
* Pour **utiliser une fonction** prédéfinie ou personnalisé, il faut écrire sont nom, les parenthèses et les paramètres si elle en a.
{{% /notice %}}

---

### Exercices

{{% notice style="magenta" title="Appel de fonction" groupid="notice-toggle" expanded="false" %}}
Pour les exercices #2 à #5, utilisez (appelez) la fonction crée.
{{% /notice %}}

[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_fonctions.ipynb)

## Exercice 1 : La loi d'Ohm

Un technicien de laboratoire vous demande d'écrire un programme Python pour calculer la tension (U) en volts selon la loi d’Ohm. Il voudrait pouvoir entrer la valeur de la résistance (en ohms) et la valeur du courant (en ampères), puis obtenir la tension.

```math
Loi d’Ohm : $ U = R × I $
```
Le technicien souhaiterait pouvoir réutiliser le programme plus facilement et dans d'autres situations. Pour ce faire, il vous demande d'écrire une fonction qui : 

1. Demande à l'utilisateur d'entrer la valeur de la résistance (en ohms).
2. Demande à l'utilisateur d'entrer la valeur du courant (en ampères).
3. Calcule et affiche la tension à l'aide d'une phrase.

**NB** : Ajoutez des explications en commentaire dans le code.

**Résultat attendu** :
```
Entrer la résistance en ohms : 10
Entrer le courant en ampères : 2
La tension est de 20.0 V
```

### Exercice 2 : Élément chimique

Écrire une fonction `element_chm(elt)` qui :
* Prend en paramètre le nom d’un élément chimique.
* Affiche un message disant "L’élément choisi est [nom]"

**Exemple d'affichage attendu (élément oxygène)** :
```python
L’élément choisi est : oxygène
```

### Exercice 3 : Convertir Celsius en Kelvin

Crée une fonction nommée `convertir_C_en_K` qui :
* prend une température en °C en paramètre
* retourne la température en Kelvin (formule : K = C + 273.15)

**Exemple d'affichage attendu (30°C)** :
```python
Une température de 30°C équivaut à 303.15 K.
```

### Exercice 4 : Calculer une énergie cinétique

Créez une fonction `energie_cinetique(m, v)` qui calcule et retourne la valeur de l'énergie cinétique d'un objet en joules:

```math
$E_c = \frac{1}{2} \cdot m \cdot v^2$
```
où
* m  : La masse de l'objet en kilogrammes.
* v  : La vitesse de l'objet en mètres par seconde.

**Exemple d'affichage attendu avec `masse=2.0 kg` et `vitesse=3.0 m/s`** :
```python
L'énergie cinétique de l'objet est de 9.0 joules.
```

### Exercice 5 : Aire d'un cercle

Écrire une fonction `aire_cercle()` qui :
* Demande à l'utilisateur d'entrer le rayon du cercle (en cm).
* Calcule l'aire du cercle (utilisez le **module math** pour PI et le rayon².)
* Affiche l'aire du cercle, arrondie à 2 décimales (utilisez la fonction `round`).

**Exemple d'affichage attendu (rayon de 5 cm)** :
```python
Aire du cercle de rayon 5 cm : 78.54 cm²
```

### Exercice 6 : Vérifier la portée locale

Crée une fonction `tester_variable()` qui crée une variable `prenom = "votre prénom` et l’affiche dans la fonction avec un `print`.
Essaye ensuite d’afficher la valeur de `prenom` **à l’extérieur de la fonction**.

**Exemple d'affichage attendu** :
```python
NameError                                 Traceback (most recent call last)
Cell In[16], line 6
      3     print(f"Dans la fonction tu t'appelles : {prenom}")
      5 tester_variable()
----> 6 print(f"À l'exterieur de la fonction tu t'appelles : {prenom}") 

NameError: name 'prenom' is not defined
```

---

## Atelier

[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/atelier_fonctions_perso.ipynb)


## Exercice – Calcul de dilution (C₁V₁ = C₂V₂)

En laboratoire, vous devez préparer une solution diluée à partir d'une solution mère plus concentrée. Vous connaissez la formule de dilution :

```
C₁ × V₁ = C₂ × V₂
```

Où :

* `C₁` : concentration de la solution mère (mol/L)
* `V₁` : volume de la solution mère à prélever (L)
* `C₂` : concentration finale souhaitée (mol/L)
* `V₂` : volume final de la solution diluée (L)

---

Écrire un programme Python structuré en **plusieurs fonctions** qui permet de :

1. **Lire** les données nécessaires à la dilution (`C1`, `C2`, `V2`) — sans retourner de valeur.
2. **Calculer et retourner** le volume `V1` de solution mère à prélever (formule : `V1 = (C2 × V2) / C1`).
3. **Afficher** une phrase qui résume le calcul avec les valeurs fournies.

---

### Consignes

1. Crée une fonction `lire_donnees()` **sans paramètres** qui demande à l’utilisateur :

   * la concentration `C1` de la solution mère (en mol/L),
   * la concentration `C2` de la solution finale (en mol/L),
   * le volume final `V2` (en L),
     et **retourne ces 3 valeurs**.

2. Crée une fonction `calculer_v1(C1, C2, V2)` qui :

   * prend en **paramètres** les trois valeurs,
   * **retourne** le volume `V1` à prélever (en L).

3. Crée une fonction `afficher_resultat(V1)` qui **affiche** une phrase expliquant le volume de solution mère à utiliser, avec **deux décimales**.

4. Teste le tout dans un petit programme principal.


### Exemple d'exécution attendue

```
--- Programme de dilution ---
Concentration de la solution mère (mol/L) : 2.0
Concentration finale souhaitée (mol/L) : 0.5
Volume final de la solution (L) : 1.0
Il faut prélever 0.25 L de solution mère pour préparer la solution diluée.
```

---

> **RAPPEL**: Le **troisième et dernier examen** (20%) et prévu à la **semaine 15**.

1. Lire la description du [Projet final](../semaine12/)
2. Prendre connaissance de la [Grille de correction](../semaine12/grille/)
3. S'approprier des [Notions à savoir pour réussir le projet](../semaine12/competences_reussite/)
