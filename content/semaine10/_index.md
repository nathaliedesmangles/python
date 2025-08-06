+++
chapter = true
pre = "10."
title = " Évaluation #2 (30%)"
weight = 110
draft = false
+++


## Informations

⦁ **Date**:			Semaine #10 (Voir le calendrier)  
⦁ **Matière**: 		        Semaines 6 à 9 inclusivement  
⦁ **Documentation permise**: 	1 feuille recto-verso (manuscrite ou imprimée)  
⦁ **Format**:			À confirmer

<!--
## Exercice 6 – Motif avec nombres décroissants par ligne

* Affiche les nombres dans l’ordre décroissant sur chaque ligne.
* Utilise deux boucles `for` imbriquées.
* Ne pas utiliser de chaînes préfabriquées (ex: `"321"`).

**Affichage attendu :**
```
321
21
1
```

## Exercice 7 – Triangle aligné à droite avec nombres croissants

* Utilise les fonctions `print()` et la multiplication de chaînes (`" " * n`).
* Aligne le motif à droite.
* Ne pas utiliser de fonctions avancées comme `rjust()`.


**Affichage attendu :**
```
&nbsp; 1
&nbsp;12
123

```


## Exercice 8 – Triangle inversé avec décalage à gauche

* Utilise deux boucles imbriquées et des espaces (`" "`) pour le décalage.
* Le triangle doit se décaler d’une position à droite à chaque ligne.

**Affichage attendu :**
```
123
&nbsp;12
&nbsp; 1
```


=== SOLUTION===

## Exercice 6: Nombres décroissants sur chaque ligne

**Affichage :**
```

321
21
1
```

**Code :**
```python

for i in range(3, 0, -1):
&nbsp;   for j in range(i, 0, -1):
&nbsp;       print(j, end="")
&nbsp;   print()
```

## Exercice 7: Triangle inversé aligné à droite

**Affichage :**
```
&nbsp; 1
&nbsp;12
123
```

**Code :**
```python
n = 3

for i in range(1, n + 1):
&nbsp;   print(" " * (n - i) + "".join(str(j) for j in range(1, i + 1)))
```


## Exercice 8: Triangle inversé avec espace et décalage

**Affichage :**
```
123
&nbsp;12
&nbsp; 1
```
```python
n = 3

for i in range(n, 0, -1):
&nbsp;   print(" " * (n - i) + "".join(str(j) for j in range(1, i + 1)))
```
-->