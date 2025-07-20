+++
pre = "<b>5.</b>"
title = " Décider avec if-elif-else et les opérateurs"
weight = 206
+++


### Partie 1 – Opérateurs de comparaison

```python
# 1.1

a = 10
b = 7

print(a > b)     # True
print(a == 7)    # False

# 1.2

# Résultats :

5 != 3     # True
8 <= 8     # True
4 > 10     # False
3 == 3     # True

```

---

### Partie 2 – Opérateurs logiques

```python
# 2.1

(5 > 2) and (7 < 10)     # True and True = True
(3 != 3) or (6 >= 6)     # False or True = True
not (2 < 5)              # not True = False

# 2.2

# Cette condition est vraie si : temperature > 30 ET humidite < 50
```

---

### Partie 3 – Lire et corriger des conditions

```python
# 3.1

temp = 10
if temp > 25:
    print("Il fait chaud.")
elif temp > 15:
    print("Il fait confortable.")
else:
    print("Il fait frais.")  # → affichera ceci

# 3.2

# Erreur : il manque les deux-points à la fin du if

# Correction :

if vitesse > 80:
     print("Trop vite !")
```

---


### Partie 4 – Écrire ses propres conditions

```python
# 4.1

ph = 6.4

if ph < 7:
    print("Solution acide")
elif ph == 7:
    print("Solution neutre")
else:
    print("Solution basique")

# 4.2

temperature = 110
pression = 1.6

if temperature > 100 and pression > 1.5:
    print("Attention, danger")
```