+++
pre = "8."
title = " Dictionnaires et fichiers texte"
weight = 308
draft = true
+++


```python
# 1. Lecture du fichier CSV
import csv

donnees = {}

with open("cristallisation.csv", newline='', encoding='utf-8') as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        substance = ligne["substance"]
        condition = ligne["condition"]
        temp = float(ligne["temp_cristallisation"])

        if substance not in donnees:
            donnees[substance] = {}
        donnees[substance][condition] = temp

# 2. Affichage des données
for substance in donnees:
    for condition in donnees[substance]:
        temp = donnees[substance][condition]
        print(f"{substance} cristallise à {temp}°C {condition.replace('_', ' ')}.")

# 3. Ajout d'une nouvelle condition pour H2O
donnees["H2O"]["en_solution"] = -5

# 4. Vérification de la présence de "Cu"
if "Cu" in donnees:
    print("Cu est présent dans les données.")
else:
    print("Cu n'est pas présent dans les données.")

# 5. Filtrage : substances ayant une température < 100°C dans au moins une condition
print("Substances ayant au moins une température de cristallisation < 100°C :")
for substance in donnees:
    for condition in donnees[substance]:
        if donnees[substance][condition] < 100:
            print(f"- {substance} ({condition.replace('_', ' ')} : {donnees[substance][condition]}°C)")
            break  # on passe à la substance suivante

# 6. Comparaison : écart maximal de température pour chaque substance
print("Écart maximal entre les conditions pour chaque substance :")
for substance in donnees:
    temperatures = list(donnees[substance].values())
    ecart = max(temperatures) - min(temperatures)
    print(f"Pour {substance}, l’écart maximal est de {ecart:.1f}°C entre deux conditions.")

# 7. (Facultatif) Comparaison moyenne entre substances
def comparaison_substances(donnees):
    moyennes = {}
    for substance in donnees:
        valeurs = list(donnees[substance].values())
        moyennes[substance] = sum(valeurs) / len(valeurs)

    substance_max = max(moyennes, key=moyennes.get)
    print(f"\nSubstance avec la température moyenne de cristallisation la plus élevée : {substance_max} ({moyennes[substance_max]:.1f}°C)")

comparaison_substances(donnees)
```