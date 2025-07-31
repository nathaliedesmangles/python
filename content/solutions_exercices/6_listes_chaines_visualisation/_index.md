+++
pre = "6."
title = " Listes, chaines et visualisation des données"
weight = 206
+++


### **Listes**

#### Exercice 1

```python
animaux = ["chat", "chien", "lapin", "perroquet", "tigre"]

for animal in animaux:
      print(f"Voici un/une {animal}")
```

---

#### Exercice 2

```python
grille = [
           [1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16],
           [17, 18, 19, 20]
]

for ligne in grille:
    for chiffre in ligne:
        print(chiffre)
```

---

#### Exercice 3

```python
noms = []

for i in range(3):
    nom = input(f"Entrez le nom {i+1} : ")
    noms.append(nom)

print("Ordre alphabétique croissant :")

for nom in sorted(noms):
    print(nom)

print("Ordre alphabétique décroissant :")

for nom in sorted(noms, reverse=True):
    print(nom)
```

---

#### Exercice 4

```python
suspects = [
             ["A", "T", "C", "G"],
             ["G", "A", "T", "G"],
             ["A", "T", "T", "G"]
]


print(suspects[0][1])  # 2e base de la 1re séquence → T
print(suspects[2][-1])  # dernière base de la 3e séquence → G
```

---


### **Chaînes de caractères**

#### Exercice 5

```python
mots = ["chlorophylle", "atome", "protéine"]

nb_lettres = []

for mot in mots:
    nb_lettres.append(len(mot))

print(nb_lettres)  # [12, 5, 8]
```

---

#### Exercice 6

```python
adn = "ATGCT"
arn = adn.lower().replace("t", "u")
print(arn)  # augcu
```

---


### **Graphiques avec matplotlib**

#### Exercice 7

```python
import matplotlib.pyplot as plt

heures = [0, 4, 8, 12, 16, 20, 24]
temperatures = [-5, -2, 3, 7, 6, 1, -2]

plt.plot(heures, temperatures)
plt.title("Température en fonction de l’heure")
plt.xlabel("Heure (h)")
plt.ylabel("Température (°C)")
plt.grid()
plt.show()
```

---

#### Exercice 8

```python
import matplotlib.pyplot as plt

temp = [10, 20, 30, 40, 50]
attendu = [2.1, 3.8, 5.6, 7.3, 9.0]
mesure =  [2.0, 3.9, 5.2, 7.5, 8.8]

plt.plot(temp, attendu, "ok-", label="Valeurs attendues")  # o = rond, k = noir, - = ligne
plt.bar(temp, mesure, color="blue", alpha=0.5, label="Valeurs mesurées")

plt.title("Comparaison des concentrations")
plt.xlabel("Température (°C)")
plt.ylabel("Concentration")
plt.grid()
plt.legend()
plt.show()
```