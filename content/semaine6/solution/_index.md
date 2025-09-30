+++
title = "Atelier - Version pas à pas (solution)"
weight = 106.2
+++



### 1. **Les données**

```python
# Données des températures
temperatures = [
    [15, 16, 14, 14, 17, 18, 19],  # Ville A
    [22, 23, 21, 20, 24, 25, 26],  # Ville B
    [5, 7, 6, 6, 8, 9, 7],         # Ville C
    [10, 11, 12, 10, 13, 14, 15]   # Ville D
]

villes = ["Ville A", "Ville B", "Ville C", "Ville D"]
jours = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]
```


### 2. **Afficher les températures**

```python
for i in range(len(villes)):
    print(villes[i], ":", end=" ")
    for t in temperatures[i]:
        print(t," ")	# les températures séparées par un espace
    print()  # retour à la ligne
```

**Résultat attendu :**
```
Ville A : 15 16 14 14 17 18 19 
Ville B : 22 23 21 20 24 25 26 
Ville C : 5 7 6 6 8 9 7 
Ville D : 10 11 12 10 13 14 15 
```


### 3. **Trouver les valeurs extrêmes (min et max)**

**Étape 3a. Ville A seulement**

```python
print("La température maximale de Ville A est", max(temperatures[0]), "C")
print("La température minimale de Ville A est", min(temperatures[0]), "C")
```

**Étape 3b. Répéter pour Ville B et Ville C**

```python
print("La température maximale de Ville B est", max(temperatures[1]), "C")
print("La température minimale de Ville B est", min(temperatures[1]), "C")

print("La température maximale de Ville C est", max(temperatures[2]), "C")
print("La température minimale de Ville C est", min(temperatures[2]), "C")
```

**Étape 3c. Généraliser avec une boucle**

```python
for i in range(len(villes)):
    maxi = max(temperatures[i])
    mini = min(temperatures[i])
    print("La température maximale de", villes[i], "est", maxi, "C")
    print("La température minimale de", villes[i], "est", mini, "C")
```

---

### 4. **Classer les températures**

**Étape 4a. Tester avec une seule valeur**

```python
T = 15
if T < 10:
    print(T, "=> Froide")
elif T <= 20:
    print(T, "=> Douce")
else:
    print(T, "=> Chaud")
```

**Étape 4b. Tester avec plusieurs valeurs**

```python
for T in [7, 15, 23]:
    if T < 10:
        print(T, "=> Froide")
    elif T <= 20:
        print(T, "=> Douce")
    else:
        print(T, "=> Chaud")
```

**Étape 4c. Appliquer à une seule ville (Ville A)**

```python
print("Classification pour Ville A :")
for T in temperatures[0]:
    if T < 10:
        print(T, "=> Froide")
    elif T <= 20:
        print(T, "=> Douce")
    else:
        print(T, "=> Chaud")
```

**Étape 4d. Généraliser à toutes les villes**

```python
for i in range(len(villes)):
    print("Classification pour", villes[i], ":")
    for T in temperatures[i]:
        if T < 10:
            print(T, "=> Froide")
        elif T <= 20:
            print(T, "=> Douce")
        else:
            print(T, "=> Chaud")
    print()  # saut de ligne entre les villes
```


### 5. **Tracer un graphique avec matplotlib**

```python
import matplotlib.pyplot as plt

for i in range(len(villes)):
    plt.plot(jours, temperatures[i], label=villes[i])

plt.title("Températures hebdomadaires")
plt.xlabel("Jour")
plt.ylabel("Température (C)")
plt.grid(True)
plt.legend()
plt.savefig("temperatures.png")
plt.show()
```

