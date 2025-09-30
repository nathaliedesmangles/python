+++
title = "print et end"
weight = 106.5
+++

* En Python, la fonction `print()`, ajoute par défaut un saut de ligne (`\n`) à la fin de chaque instruction. 
* Ce comportement peut être modifié grâce au paramètre `end`, qui permet de préciser **une autre chaîne de caractères** (comme un espace `" "`, une virgule `","` ou un tiret `"-"`, etc.) à afficher à la fin. 
* Cela rend possible l’affichage de plusieurs sorties sur la même ligne ou avec des séparateurs personnalisés.

**Exemples :**

* **Un espace**
```python
print("Bienvenus au cours", end=" ")
print("de programmation")
```

> Ici, au lieu de passer à la ligne après chaque `print()`, le texte sera affiché côte à côte, séparé par un espace ` `.
```
Bienvenus au cours de programmation
```

* **Une virgule**
```python
print("Bienvenus au cours", end=", ")
print("de programmation")
```

> Ici, au lieu de passer à la ligne après chaque `print()`, le texte sera affiché côte à côte, séparé par une virgule `,`.
```
Bienvenus au cours, de programmation
```

* **Une étoile**
```python
print("Bienvenus au cours", end="*")
print("de programmation")
```

> Ici, au lieu de passer à la ligne après chaque `print()`, le texte sera affiché côte à côte, séparé par une étoile `*`.
```
Bienvenus au cours*de programmation
```

