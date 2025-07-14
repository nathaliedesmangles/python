+++
pre = "3."
title = " Entrées/Sorties, algorithme et débogage"
weight = 203

draft = false
+++





\## Exercice #1



\### Cellule Markdown – Algorithme



```markdown
#### Algorithme – Calcul de la force gravitationnelle

1. Demander à l’utilisateur d’entrer le nom de l’objet (chaîne de caractères).
2. Demander à l’utilisateur d’entrer la masse de l’objet (nombre décimal, en kg).
3. Définir la constante d’accélération gravitationnelle (9,8 m/s²).
4. Calculer la force en utilisant la formule : `force = masse \* accélération`
5. Afficher la force avec une phrase claire, incluant le nom de l’objet et l’unité en N (Newton).
```



\### Cellule Code



```python
# Demande du nom de l'objet (chaîne de caractères)
nom\_objet = input("Entrez le nom de l'objet : ")

# Demande de la masse (nombre décimal)
masse = float(input("Entrez la masse de l'objet en kg : "))

# Déclaration de la constante d'accélération gravitationnelle (en m/s²)
ACCELERATION\_GRAVITATIONNELLE = 9.8  # constante en majuscules

# Calcul de la force
force = masse \* ACCELERATION\_GRAVITATIONNELLE

# Affichage du résultat
print(f"La force de {nom\_objet} de {masse:.1f} est de {force:.2f} N.")
```



\## Résultats des tests



\### Test 1



\*\*Entrée\*\* :



\* nom\_objet = "balle"

\* masse = 2.5



\*\*Sortie attendue\*\* :



```
La force de la balle de 2.5 Kg est de 24.50 N.
```



\### Test 2



\*\*Entrée\*\* :



\* nom\_objet = "voiture"

\* masse = 1000.0



\*\*Sortie attendue\*\* :



```
La force de la voiture de 1000.0 Kg est de 9800.00 N.
```



\## Exercice #2





\## Exercice #3





\## Exercice #4



