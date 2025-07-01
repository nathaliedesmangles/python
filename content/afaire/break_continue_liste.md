+++
title = "break, continue, liste et boucle"
weight = 3
+++

## Objectifs de la séance

1. Apprendre à **arrêter une boucle** selon une condition.
2. Apprendre à **créer et manipuler une liste**.
3. Apprendre à **parcourir des listes ou des chaînes de caractères avec la boucle `for`**.

---

## Partie 1 – Arrêter une boucle selon une condition

### Explication

- Une boucle `while` ou `for` continue tant qu'une condition est vraie. On peut aussi utiliser `break` pour arrêter manuellement une boucle.

### Démonstration : boucle `while`

```python
valeur = 0
while valeur < 100:
    print("Valeur actuelle :", valeur)
    if valeur == 50:
        break  		# Arrête la boucle
    valeur += 1
```

### Démonstration : boucle `for`

```python
for i in range(11):	# i prends les valeurs 0,1,2,3,4,5,6,7,8,9,10
    if i == 5:
        break		# Arrête la boucle
    print(i)    	# Affiche: 0, 1, 2, 3, 4
```

### Exercice 1

- Demander à l’utilisateur de saisir des températures (float). 
- La boucle s’arrête dès qu’on entre la valeur 0 (valeur sentinelle).

```python
# Saisie de températures
while True:		# Toujours Vrai, pratique ici, mais à éviter
    temp = float(input("Entrez une température (ou 0 pour arrêter) : "))
    if temp == 0:
        print("Arrêt de la saisie.")
        break
```

---

## Partie 2 – Créer et manipuler une liste

### Explication

- Une **liste** permet de stocker plusieurs éléments (nombres, chaînes, etc.) dans une seule variable.
- Dans une liste les éléments sont indexés à partir de 0, ce qui signifie que le premier élément d'une liste et à l'indice 0.
- Pour accéder à un élément d'une liste on utilise: `nom-de-la-liste[index]`.
  * Exemple: Pour accéder au **3e élément** d'une liste nommée `ma_liste`, on écrit: `ma_liste[2]`. `2` étant l'indice du 3e élément.

### Démonstration : création et accès

```python
fruits = ["pomme", "banane", "kiwi"]

print(fruits[0])  		# Affiche 'pomme'
fruits.append("mangue")		# Ajoute 'mangue' à la fin

print(fruits)     		# Ajoute un élément
```

### Démonstration : opérations utiles

```python
notes = [85, 90, 78, 92]

print("Nombre de notes :", len(notes))		# Affiche le nombre d'éléments dans la liste "notes"
print("Somme :", sum(notes))			# Affiche la somme des notes dans la liste
print("Moyenne :", sum(notes) / len(notes))	# Affiche la moyenne des notes dans la liste
```

- La fonction `len` donne la longueur d'une liste ou d'une chaine de caractères.

### Exercice 2

- Créer une liste de pH mesurés dans différents échantillons et calculer la moyenne. 
- Afficher un message si un pH est inférieur à 4.

---

## Partie 3 – Parcourir une liste ou une chaîne avec la boucle `for`

### Explication

- La boucle `for` permet de **parcourir** une liste ou une chaîne de caractères **élément par élément**.

### Démonstration 5 : liste

```python
vitesses = [10.2, 11.5, 9.8, 12.0]
for v in vitesses:
    print("Vitesse :", v)
```

### Démonstration : chaîne de caractères

```python
mot = "glucose"

for lettre in mot:
    print(lettre)
```

### Exercice 3

Demander de :

* Créer une liste de volumes en mL.
* Convertir chaque volume en L (1 L = 1000 mL) et afficher les conversions avec une boucle `for`.

---

## Exercices d'intégration

### Exercice 4

On a mesuré la concentration d’un soluté (en g/L) à 6 moments différents. La boucle :

* Affiche chaque concentration
* Affiche un message d’alerte si > 20 g/L
* Calcule la moyenne à la fin

### **Solution attendue (exemple guidé)**

```python
concentrations = [12.5, 18.0, 22.3, 19.5, 21.0, 15.7]
somme = 0

for c in concentrations:
    print("Concentration :", c)
    if c > 20:
        print("Attention : concentration élevée !")
    somme += c

moyenne = somme / len(concentrations)
print("Moyenne :", moyenne)
```

### Exercice 5 

* Écrire une fonction qui prend une liste de températures et retourne la température maximale et sa position
  - Exemple de nom de fonction: `temperature_max(une_liste)`
  - Exemple d'utilisation de la fonction:
  ```python
  liste = [15,34,23,12,31,8,20]
  temp_max = temperature_max(liste)
  print("La température maximum est", temp_max)
  ```

### Exercice 6

* On vous donne une séquence d’ADN représentée par une chaîne de caractères composée uniquement des lettres `A`, `T`, `C` et `G`. Par exemple :

```python
sequence = "ATGCGCATTAAGGCCGTA"
```

1. Parcourez la séquence avec une boucle `for`.
2. Comptez le nombre de bases `A`, `T`, `C` et `G`.
3. Affichez le nombre total de bases.
4. Affichez le pourcentage de **G+C** dans la séquence.


### **Indices**

* Une lettre dans une chaîne peut être parcourue avec une boucle `for`.
* Pour augmenter un compteur, on peut faire : `compteur += 1`
* Calcul du pourcentage :

```
Pourcentage de G+C = (nombre de G + nombre de C) / nombre total de bases * 100
```

---

### **Solution attendue (exemple guidé)**

```python
sequence = "ATGCGCATTAAGGCCGTA"

nb_A = 0
nb_T = 0
nb_C = 0
nb_G = 0

for base in sequence:
    if base == 'A':
        nb_A += 1
    elif base == 'T':
        nb_T += 1
    elif base == 'C':
        nb_C += 1
    elif base == 'G':
        nb_G += 1

total = len(sequence)
gc_content = ((nb_G + nb_C) / total) * 100

print("A :", nb_A)
print("T :", nb_T)
print("C :", nb_C)
print("G :", nb_G)
print("Total :", total)
print("Pourcentage de G+C :", round(gc_content, 2), "%")
```

---

### Variante possible

* Ajouter une vérification : si une base **n’est pas** A, T, C ou G, afficher un message d’erreur.
* Compter les codons (groupes de 3 bases) avec une boucle `for` allant de 0 à `len(sequence)-3` par pas de 3.




