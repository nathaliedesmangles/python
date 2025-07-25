+++
pre = "<b>7.</b>"
title = " Listes, chaines et graphiques de base"
weight = 307
+++

```python
import matplotlib.pyplot as plt

# Données brutes sous forme de chaînes
donnees = [
    "12.3, 16.8, 14.0",  # jour 1 : matin, midi, soir
    "11.5, 18.2, 15.4",
    "10.8, 17.6, 14.9",
    "13.0, 19.1, 16.3",
    "14.1, 20.2, 18.5",
    "12.9, 18.7, 16.2",
    "11.7, 17.8, 15.0"
]


# 1. Transformation des chaînes en listes de 3 nombres flottants
temperatures = []
for ligne in donnees:
    morceaux = ligne.split(",")
    valeurs = [float(x.strip()) for x in morceaux]
    temperatures.append(valeurs)

print("Liste des températures (liste imbriquée) :")
print(temperatures)
```
```
Liste des températures (liste imbriquée) :
[[12.3, 16.8, 14.0], [11.5, 18.2, 15.4], [10.8, 17.6, 14.9], [13.0, 19.1, 16.3], [14.1, 20.2, 18.5], [12.9, 18.7, 16.2], [11.7, 17.8, 15.0]]
```

```python
# 2. Calculs sur les données

# Moyenne de chaque jour
moyennes_journalières = []
for jour in temperatures:
    moyenne = sum(jour) / 3
    moyennes_journalières.append(moyenne)

print("Températures moyennes par jour :")
print(moyennes_journalières)

# Température maximale
valeurs_toutes = []
for jour in temperatures:
    for t in jour:
        valeurs_toutes.append(t)

temp_max = max(valeurs_toutes)
jour_max = valeurs_toutes.index(temp_max) // 3 + 1

print(f"Température maximale : {temp_max}°C (Jour {jour_max})")

# Moyenne générale
moyenne_globale = sum(valeurs_toutes) / len(valeurs_toutes)
print(f"Température moyenne de la semaine : {moyenne_globale:.2f}°C")
```

```
Températures moyennes par jour :
[14.366666666666667, 15.033333333333333, 14.433333333333335, 16.133333333333336, 17.599999999999998, 15.933333333333332, 14.833333333333334]
Température maximale : 20.2°C (Jour 5)
Température moyenne de la semaine : 15.48°C
```

```python
# 3. Visualisation avec matplotlib

import matplotlib.pyplot as plt

jours = [1, 2, 3, 4, 5, 6, 7]

plt.plot(jours, moyennes_journalières, marker='o', color='blue', label='Moyenne journalière')
plt.title("Températures moyennes par jour")
plt.xlabel("Jour")
plt.ylabel("Température (°C)")
plt.grid()
plt.legend()
plt.savefig("graphique_temperature.png")
plt.show()
```

![Atelier 7](./graphique_temperature.png?width=40vw)

```python
# 4. Exploration des chaînes de caractères (températures de midi)

# Recompte des jours où la température de midi dépasse 18°C
nb_midi_haut = 0

for ligne in donnees:
    morceaux = ligne.split(",")
    midi = float(morceaux[1].strip())
    if midi > 18:
        nb_midi_haut += 1

print(f"Nombre de jours où la température de midi a dépassé 18°C : {nb_midi_haut}")
```
```
Nombre de jours où la température de midi a dépassé 18°C : 4
```