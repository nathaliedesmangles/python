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
![Erreur de nom](../fonctions_perso/erreur_name.png?width=35vw)

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

[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_entrees_fn_debug.ipynb)

## Exercice 1 : La loi d'Ohm

Un technicien de laboratoire vous demande d'écrire un programme Python pour calculer la tension (U) en volts selon la loi d’Ohm. Il voudrait pouvoir entrer la valeur de la résistance (en ohms) et la valeur du courant (en ampères), puis obtenir la tension.

```math
Loi d’Ohm : $ U = R × I $
```
Écrire un programme qui : 
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

Écrire un programme qui :
* Demande à l'utilisateur d'entrer le nom d’un élément chimique.
* Affiche un message disant "L’élément choisi est \[nom]"

**Exemple d'affichage attendu (élément oxygène)** :
```python
Entrer le nom d'un élément chimique : oxygène
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

> **RAPPEL**: Le **troisième et dernier examen** (20%) et prévu à la **semaine 15**.

1. Lire la description du [Projet final](../semaine12/)
2. Prendre connaissance de la [Grille de correction](../semaine12/grille/)
3. S'approprier des [Notions à savoir pour réussir le projet](../semaine12/competences_reussite/)


<!--
## Exercices à faire avant le cours


[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_graphes_barres_reg.ipynb)





### Exercice 1 – Sulfate de cuivre



1. Températures : `[0, 10, 20, 30, 40, 50]`

2. Solubilité (g/100g eau) : `[23, 27, 32, 37, 44, 51]`

3. Calcule la régression linéaire.

4. Affiche les résultats et une conclusion scientifique.





### Exercice 2 – Comparaison de deux sels



1. Sel A :



   * Température : `[0, 20, 40, 60]`

   * Solubilité : `[15, 21, 30, 38]`



2. Sel B :



   * Température : `[0, 20, 40, 60]`

   * Solubilité : `[30, 32, 33, 33.5]`



3. Pour chaque sel :



   * Effectue la régression

   * Affiche pente, intercept, R²

   * Déduis quel sel est le plus influencé par la température





### Exercice 3 – Prévision



1. Utilise les données de l’exemple principal

2. Calcule la solubilité prévue à 60 °C avec la formule :



```python
valeur_predite = resultat.slope * 60 + resultat.intercept
print(f"Solubilité prévue à 60 °C : {valeur_predite:.2f} g/100g d’eau")
```



### Exercice 1 – Graphique à barres



**Énoncé :**

Affiche un graphique à barres pour les éléments `"Fer"`, `"Cuivre"`, `"Zinc"` avec les valeurs `[12, 7, 5]`.



**Solution :**



```python
elements = ["Fer", "Cuivre", "Zinc"]
quantites = [12, 7, 5]

plt.bar(elements, quantites)
plt.title("Concentration des métaux")
plt.legend(["mg/L"])
plt.show()
```





### Exercice 2 – Barres d’erreur



**Énoncé :**

Pour `x = [1, 2, 3]`, `y = [5.1, 5.0, 5.2]`, `yerr = [0.1, 0.2, 0.15]`, trace les points avec barres d’erreur.



**Solution :**



```python
x = [1, 2, 3]
y = [5.1, 5.0, 5.2]

yerr = [0.1, 0.2, 0.15]

plt.errorbar(x, y, yerr=yerr, fmt="o", label="Mesures")
plt.title("Tension mesurée")
plt.legend()
plt.grid(True)
plt.show()
```





### Exercice 3 – Droite de régression



**Énoncé :**

Pour `x = [0, 1, 2, 3]`, `y = [1, 2.1, 3.9, 6.0]`, trace les points et la droite de régression, avec son équation dans la légende.



**Solution :**



```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3])
y = np.array([1, 2.1, 3.9, 6.0])

a, b = np.polyfit(x, y, 1)

plt.plot(x, y, "o", label="Points")
plt.plot(x, a*x + b, "-", label=f"y = {a:.2f}x + {b:.2f}")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
```

-->