+++
pre = "6."
title = " Listes, chaines et visualisation des données"
weight = 306
draft = false
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


# 1. Extraction et nettoyage

temperatures = []  # liste imbriquée

for ligne in donnees:
     trio = ligne.split(",")
     trio_float = [float(valeur.strip()) for valeur in trio]
     temperatures.append(trio_float)

print("Liste des températures (liste imbriquée) :")
print(temperatures)

# 2. Calculs sur les données

# Moyenne par jour
moyennes_journalières = []

for jour in temperatures:
     moyenne = sum(jour) / len(jour)
     moyennes_journalières.append(moyenne)

print("Températures moyennes par jour :")
print(moyennes_journalières)


# Température maximale et jour
toutes_valeurs = [temp for jour in temperatures for temp in jour]
temp_max = max(toutes_valeurs)
index_max = toutes_valeurs.index(temp_max)
jour_max = index_max // 3 + 1

print(f"Température maximale : {temp_max}°C (Jour {jour_max})")

# Moyenne globale
moyenne_generale = sum(toutes_valeurs) / len(toutes_valeurs)
print(f"Température moyenne de la semaine : {moyenne_generale:.2f}°C")

# 3. Visualisation avec matplotlib

jours = list(range(1, 8))

plt.plot(jours, moyennes_journalières, marker='o', color='blue', label="Moyenne quotidienne")
plt.title("Températures moyennes par jour")
plt.xlabel("Jour")
plt.ylabel("Température (°C)")
plt.grid()
plt.legend()
plt.savefig("graphique_temperature.png")
plt.show()


# 4. Exploration des chaînes de caractères (températures de midi)

nb_midi_sup_18 = 0

for ligne in donnees:
     valeurs = ligne.split(",")
     midi = float(valeurs[1].strip())

     if midi > 18:
         nb_midi_sup_18 += 1

print(f"Nombre de jours où la température de midi a dépassé 18°C : {nb_midi_sup_18}")
```

---

### Résultat attendu (valeurs approximatives à cause des arrondis) :


```
Liste des températures (liste imbriquée) :
[[12.3, 16.8, 14.0], [11.5, 18.2, 15.4], ..., [11.7, 17.8, 15.0]]

Températures moyennes par jour :
[14.37, 15.03, 14.43, 16.13, 17.6, 15.93, 14.83]

Température maximale : 20.2°C (Jour 5)

Température moyenne de la semaine : 15.47°C

Nombre de jours où la température de midi a dépassé 18°C : 2
```

