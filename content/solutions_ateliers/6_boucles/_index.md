+++
pre = "<b>6.</b>"
title = " Répéter avec FOR et WHILE"
weight = 306
draft = false
+++


## Exercice 1 – Table de multiplication

### Solution de base (avec boucle `for`)

```python
# Demande à l'usager un nombre entre 1 et 12
n = int(input("Entrez un nombre entre 1 et 12 : "))

# Vérifie que le nombre est valide

if 1 <= n <= 12:
   for i in range(1, 13):
       print(f"{i} x {n} = {i * n}")
else:
   print("Le nombre doit être entre 1 et 12.")
```

### **Variante 1** : ordre croissant ou décroissant

```python
n = int(input("Entrez un nombre entre 1 et 12 : "))

if 1 <= n <= 12:
   ordre = input("Voulez-vous l’ordre croissant (c) ou décroissant (d) ? ")
   if ordre.lower() == 'c':
       for i in range(1, 13):
           print(f"{i} x {n} = {i * n}")
   elif ordre.lower() == 'd':
       for i in range(12, 0, -1):
           print(f"{i} x {n} = {i * n}")
   else:
       print("Choix non reconnu.")
else:
   print("Le nombre doit être entre 1 et 12.")
```



## Exercice #2 – Motif croissant simple



**Affichage attendu :**

```

1

12

123

```



```python

for i in range(1, 4):       # i va de 1 à 3 inclusivement

   for j in range(1, i + 1):  # j va de 1 jusqu'à i

       print(j, end="")     # afficher j sans aller à la ligne

   print()                  # aller à la ligne après chaque ligne

```





## Exercice #3 - Motif croissant inversé (triangle renversé)



**Affichage attendu :**

```

123

12

1

```



```python

for i in range(3, 0, -1):     # i va de 3 à 1 (inclus) en décrémentant

   for j in range(1, i + 1): # j va de 1 à i

       print(j, end="")      # afficher j sans retour à la ligne

   print()                   # retour à la ligne après chaque ligne



```





## Exercice 4: Triangle inversé symétrique avec des étoiles `*`



**Affichage :**

```

*****

 ***

  *

```



```python

n = 3

for i in range(n, 0, -1):

   etoiles = "*" * (2 * i - 1)

   espaces = " " * (n - i)

   print(espaces + etoiles)

```







