+++
title = "Bonnes pratiques, documentation, débogage"
weight = 2
+++


## Objectifs

* Adopter des pratiques de codage claires et lisibles
* Comprendre l’utilité des commentaires et de la documentation
* Apprendre des méthodes simples pour détecter et corriger des erreurs
* Se préparer à lire et améliorer du code existant

---

## Pourquoi adopter de bonnes pratiques?

Un programme **fonctionnel** n’est pas forcément un programme **lisible** ou **facile à maintenir**. Les bonnes pratiques rendent le code :

* Plus facile à comprendre pour soi-même et pour les autres
* Plus simple à déboguer
* Moins susceptible de contenir des erreurs


## Quelques bonnes pratiques essentielles

**a. Clarté des noms de variables**  
Utilisez des noms qui ont du sens :

```python
r = 10       # Mauvais  
resistance = 10  # Meilleur
```

**b. Indentation et structure du code**  
Python utilise l’indentation pour organiser le code. Ne mélangez jamais des espaces et des tabulations.

```python
if x > 0:
    print("Positif")
else:
    print("Négatif ou nul")
```

**c. Simplicité**  
Un bon code est simple. Évitez les constructions compliquées si une version plus directe existe.

**d. Séparer les étapes**  
Clarifiez le processus en séparant les étapes : entrées, calculs, affichage.


## Comment bien commenter un programme?

Les commentaires doivent expliquer **le pourquoi**, pas le comment (que l’on peut souvent lire dans le code).

**Exemple utile :**

```python
# Conversion de la masse en grammes vers kilogrammes
masse_kg = masse_g / 1000
```

**Commentaires inutiles :**

```python
masse = 3  # On met 3 dans masse
```

**À retenir :**

* Ne commentez pas l’évidence
* Mettez un commentaire en haut du programme pour résumer son objectif
* Utilisez des blocs de commentaires pour expliquer des parties complexes


## Erreurs fréquentes et débogage

**a. Erreurs de syntaxe**  
- Oubli d’un deux-points. 
- Parenthèse mal fermée. 
- Indentation incorrecte.

Python indique souvent la ligne (ou juste après) où l’erreur se produit.

**b. Erreurs de type**  
- Essayer de multiplier une chaîne de caractères par un nombre flottant :

```python
"3" * 2.5  # Erreur
```

**c. Erreur de conversion avec `input()`**  
Le retour de `input()` est toujours une chaîne (`str`) même si l’utilisateur entre un nombre. 
- Oublier de convertir entraîne des erreurs lors des calculs.
Exemple :

```python
x = input("Entrer un nombre : ")
print(x * 2)  # Répète la chaîne deux fois au lieu de doubler le nombre
```

**Correction :**

```python
x = float(input("Entrer un nombre : "))
print(x * 2)
```

**d. Erreurs de logique**  
- Le programme fonctionne mais donne un résultat faux (ex. : division au mauvais endroit, mauvaise formule).


## Astuces pour déboguer

* Lire les messages d’erreur lentement, ligne par ligne
* Ajouter des `print()` pour afficher les valeurs intermédiaires
* Tester avec des valeurs simples
* Isoler les parties du programme pour tester séparément

---

### Exercice proposé

Mettre en pratique ces notions en **corrigeant un script scientifique erroné** (voir activité de la **semaine 2**).

