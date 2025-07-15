+++
title = "Activité 9"
weight = 109
+++
 

## Objectif

Utiliser **NumPy** pour effectuer des calculs sur des données numériques, et **Pandas** pour analyser un fichier CSV contenant des données environnementales.

**Durée** : Entre 45 et 60 minutes, à faire en équipe de 2.

---

## Partie 1 – Calculs avec NumPy

1. Crée un tableau NumPy contenant les températures suivantes (en °C) mesurées chaque heure :

```python
import numpy as np

temperatures = np.array([18.5, 19.0, 20.1, 21.3, 22.8, 23.4, 22.9, 21.0])
```

2. Calcule et affiche :

   * La température moyenne
   * L’écart-type
   * La température maximale
   * Toutes les températures converties en degrés Fahrenheit (formule : `F = C × 9/5 + 32`)


## Partie 2 – Analyse avec Pandas

1. Télécharge le fichier `capteurs.csv` (fourni par l’enseignant), contenant des mesures de capteurs environnementaux :

```
Heure,Température,Humidité,pH
08:00,18.5,55,6.8
09:00,19.0,53,6.9
10:00,20.1,51,7.0
11:00,21.3,49,7.1
12:00,22.8,47,7.1
13:00,23.4,45,7.2
14:00,22.9,44,7.3
15:00,21.0,46,7.2
```

2. Utilise Pandas pour :

   * Lire le fichier
   * Afficher les 5 premières lignes
   * Afficher la moyenne de chaque variable
   * Trouver à quelle heure la température est la plus élevée
   * Filtrer les lignes où le pH est supérieur à 7.0

3. Bonus : ajoute une nouvelle colonne `Indice_confort` selon cette règle :

   * Si température ≥ 22 et humidité < 50 → "Élevé"
   * Sinon → "Modéré"


### Résultat attendu (exemples)

```python
Température moyenne : 21.125 °C
Températures en Fahrenheit : [65.3 66.2 68.2 ...]
Heure avec température max : 13:00
```

<!--

## Solutions

Voici le **corrigé commenté** de l’exercice pratique sur NumPy et Pandas. Il peut être remis à l’enseignant ou utilisé comme rétroaction à la suite de la séance.

---

## Corrigé commenté – Exercice : Analyse de données environnementales

### Partie 1 – NumPy

```python
import numpy as np

# Températures mesurées chaque heure
temperatures = np.array([18.5, 19.0, 20.1, 21.3, 22.8, 23.4, 22.9, 21.0])

# Température moyenne
moyenne = np.mean(temperatures)
print(f"Température moyenne : {moyenne:.2f} °C")  # 21.13 °C

# Écart-type
ecart_type = np.std(temperatures)
print(f"Écart-type : {ecart_type:.2f}")  # environ 1.66

# Température maximale
max_temp = np.max(temperatures)
print(f"Température maximale : {max_temp} °C")  # 23.4 °C

# Conversion en Fahrenheit
fahrenheit = temperatures * 9 / 5 + 32
print("Températures en Fahrenheit :", fahrenheit)
```

---

### Partie 2 – Pandas

```python
import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv("capteurs.csv")

# Affichage des 5 premières lignes
print(df.head())
```

#### Moyenne de chaque variable

```python
print(df.mean(numeric_only=True))  # Affiche moyenne de Température, Humidité, pH
```

#### Heure avec température maximale

```python
max_index = df["Température"].idxmax()
heure_max = df.loc[max_index, "Heure"]
print(f"Heure avec température maximale : {heure_max}")  # 13:00
```

#### Filtrage du pH

```python
ph_eleve = df[df["pH"] > 7.0]
print(ph_eleve)
```

#### Ajout d’une colonne « Indice\_confort »

```python
def calcul_indice(row):
    if row["Température"] >= 22 and row["Humidité"] < 50:
        return "Élevé"
    else:
        return "Modéré"

df["Indice_confort"] = df.apply(calcul_indice, axis=1)
print(df[["Heure", "Température", "Humidité", "Indice_confort"]])
```

---

### Résultat final (extrait)

```
Heure Température Humidité pH Indice_confort
12:00     22.8        47   7.1     Élevé
13:00     23.4        45   7.2     Élevé
14:00     22.9        44   7.3     Élevé
15:00     21.0        46   7.2     Modéré
```
-->


