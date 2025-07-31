+++
pre = "6."
title = " Listes, chaines et visualisation des données"
weight = 306
draft = false
+++





```python

import matplotlib.pyplot as plt



\# Données brutes sous forme de chaînes

donnees = \[

&nbsp;   "12.3, 16.8, 14.0",  # jour 1 : matin, midi, soir

&nbsp;   "11.5, 18.2, 15.4",

&nbsp;   "10.8, 17.6, 14.9",

&nbsp;   "13.0, 19.1, 16.3",

&nbsp;   "14.1, 20.2, 18.5",

&nbsp;   "12.9, 18.7, 16.2",

&nbsp;   "11.7, 17.8, 15.0"

]



\# 1. Extraction et nettoyage

temperatures = \[]  # liste imbriquée

for ligne in donnees:

&nbsp;   trio = ligne.split(",")

&nbsp;   trio\_float = \[float(valeur.strip()) for valeur in trio]

&nbsp;   temperatures.append(trio\_float)



print("Liste des températures (liste imbriquée) :")

print(temperatures)



\# 2. Calculs sur les données



\# Moyenne par jour

moyennes\_journalières = \[]

for jour in temperatures:

&nbsp;   moyenne = sum(jour) / len(jour)

&nbsp;   moyennes\_journalières.append(moyenne)



print("\\nTempératures moyennes par jour :")

print(moyennes\_journalières)



\# Température maximale et jour

toutes\_valeurs = \[temp for jour in temperatures for temp in jour]

temp\_max = max(toutes\_valeurs)

index\_max = toutes\_valeurs.index(temp\_max)

jour\_max = index\_max // 3 + 1



print(f"\\nTempérature maximale : {temp\_max}°C (Jour {jour\_max})")



\# Moyenne globale

moyenne\_generale = sum(toutes\_valeurs) / len(toutes\_valeurs)

print(f"Température moyenne de la semaine : {moyenne\_generale:.2f}°C")



\# 3. Visualisation avec matplotlib

jours = list(range(1, 8))



plt.plot(jours, moyennes\_journalières, marker='o', color='blue', label="Moyenne quotidienne")

plt.title("Températures moyennes par jour")

plt.xlabel("Jour")

plt.ylabel("Température (°C)")

plt.grid()

plt.legend()

plt.savefig("graphique\_temperature.png")

plt.show()



\# 4. Exploration des chaînes de caractères (températures de midi)

nb\_midi\_sup\_18 = 0

for ligne in donnees:

&nbsp;   valeurs = ligne.split(",")

&nbsp;   midi = float(valeurs\[1].strip())

&nbsp;   if midi > 18:

&nbsp;       nb\_midi\_sup\_18 += 1



print(f"\\nNombre de jours où la température de midi a dépassé 18°C : {nb\_midi\_sup\_18}")

```



---



\### Résultat attendu (valeurs approximatives à cause des arrondis) :



```

Liste des températures (liste imbriquée) :

\[\[12.3, 16.8, 14.0], \[11.5, 18.2, 15.4], ..., \[11.7, 17.8, 15.0]]



Températures moyennes par jour :

\[14.37, 15.03, 14.43, 16.13, 17.6, 15.93, 14.83]



Température maximale : 20.2°C (Jour 5)



Température moyenne de la semaine : 15.47°C



Nombre de jours où la température de midi a dépassé 18°C : 2

```

