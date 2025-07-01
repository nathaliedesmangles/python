+++
chapter = true
pre = "<b>Semaine 6.</b>"
title = "Fonctions simples et paramètres"
weight = 60
+++


## Objectifs de la leçon

À la fin de cette leçon, vous devrez être capable de :

* Expliquer le rôle des fonctions dans un programme
* Définir une fonction avec ou sans paramètres
* Appeler une fonction dans un script
* Réutiliser une fonction pour éviter la répétition de code
* Comprendre la portée des variables (locale vs globale)

---


Écrire des programmes clairs et efficaces demande de bien structurer son code. Les **fonctions** permettent de regrouper des blocs d’instructions qu’on peut exécuter plusieurs fois à différents endroits du programme. Elles rendent le code plus **lisible**, **réutilisable** et **facile à tester**.

## Définir une fonction

Une fonction se définit avec le mot-clé `def`, suivi du nom de la fonction, de parenthèses et de deux-points.

```python
def bonjour():
    print("Bonjour!")
```

Pour exécuter (appeler) cette fonction :

```python
bonjour()
```

## Paramètres d’une fonction

On peut rendre une fonction plus souple en lui donnant des **paramètres** : des valeurs qu’on lui transmet au moment de l’appel.

```python
def saluer(nom):
    print(f"Bonjour, {nom}!")
```

Appel de la fonction :

```python
saluer("Marie")
saluer("Paul")
```

On peut aussi passer plusieurs paramètres :

```python
def calculer_tension(resistance, courant):
    tension = resistance * courant
    print(f"La tension est de {tension} V")
```

Appel :

```python
calculer_tension(10, 2)
```

## Valeurs de retour (`return`)

Une fonction peut **retourner** un résultat au lieu de seulement afficher quelque chose.

```python
def calculer_tension(resistance, courant):
    return resistance * courant

u = calculer_tension(10, 2)
print(f"Tension : {u} V")
```

Cela permet de réutiliser le résultat dans un autre calcul ou de le manipuler.

## Portée des variables

Les variables créées **à l’intérieur d’une fonction** sont locales à cette fonction. Ce qui signifie que seule la fonction peut utiliser la variable.

```python
def exemple():
    x = 5
    print(x)

exemple()
# print(x)  # Provoque une erreur : x n’existe pas ici
```

Cela permet d’éviter que des variables se mélangent entre différentes parties du programme.

## Résumé des bonnes pratiques

* Donner des **noms clairs** aux fonctions
* Une fonction doit faire **une seule chose**
* Éviter de trop dépendre de variables globales (variables à l'extérieur de la fonction
* Écrire un petit **commentaire au-dessus** de chaque fonction

## Mise en pratique (aperçu)

Vous allez créer des fonctions pour modéliser des phénomènes simples (loi d’Ohm, formule de l’aire, conversion d’unités) et vous devrez les réutiliser dans un script principal.


