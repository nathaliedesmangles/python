+++
pre = "<b>6.</b>"
title = " Répéter avec FOR et WHILE"
weight = 206
+++


## Exercice 1

a. Afficher les nombres de 1 à 10

* Boucle recommandée : `for`
* Pourquoi ? Le nombre d’itérations est connu d’avance.

```python
for i in range(1, 11):
   print(i)
```

b. Compter jusqu’à 100 par bonds de 10

* Boucle recommandée : `for`
* Pourquoi ? La progression est régulière et le nombre d’itérations est connu.

```python
for i in range(0, 101, 10):
   print(i)
```

c. Simuler la chute d’un objet de 100 m (baisse de 10 m/s)

* Boucle recommandée : `while`
* Pourquoi ? On s’arrête quand l’objet atteint le sol, condition dépendante d’un calcul.

```python
hauteur = 100
vitesse = 10

while hauteur > 0:
   print(f"Hauteur : {hauteur} m")
   hauteur -= vitesse
```

d. Lire une température jusqu’à ce qu’elle soit < 0 (entrée utilisateur)

* Boucle recommandée : `while`
* Pourquoi ? On ne sait pas combien d’entrées seront nécessaires.

```python
temp = float(input("Entrez une température : "))

while temp >= 0:
   temp = float(input("Entrez une température : "))
```

e. Menu interactif : prénom ou quitter

* Boucle recommandée : `while` avec `break`
* Pourquoi ? Boucle indéterminée qui dépend du choix de l’utilisateur.

```python
while True:
   print("1 - Entrez votre prénom")
   print("2 - Quitter le programme")
   choix = input("Entrez votre choix : ")

   if choix == "1":
      prenom = input("Quel est votre prénom ? ")
      print(f"Bonjour {prenom} !")

   elif choix == "2":
      print("Programme terminé.")
      break
   else:
      print("Choix invalide.")
```

## Exercice 3

But : afficher les numéros des échantillons de 1 à 10

```python
for i in range(1, 11):
   print(f"Échantillon {i}")
```

* Affiche :
   ```
   Échantillon 1
   Échantillon 2
   ...
   Échantillon 10
   ```