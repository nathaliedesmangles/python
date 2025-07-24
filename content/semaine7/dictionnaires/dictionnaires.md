+++
title = "Dictionnaires"
weight = 107.2
daft = false
+++

## Objectifs

* **Créer un dictionnaire** simple pour représenter des données associatives (ex. : atome → masse atomique).
* **Accéder à une valeur** à partir d’une clé.
* **Ajouter ou modifier** une paire clé/valeur dans un dictionnaire.
* **Parcourir un dictionnaire** à l’aide d’une boucle `for`.
* **Vérifier la présence** d’une clé avec `in`.
* **Utiliser un dictionnaire pour organiser des données scientifiques**, comme des constantes physiques ou des observations par catégorie.

---

## Qu’est-ce qu’un dictionnaire?

Un **dictionnaire** est une structure de données qui associe des **clés** à des **valeurs**.
Il permet de stocker des informations organisées, un peu comme un mini-fichier Excel, mais avec des étiquettes personnalisées au lieu d’indices numériques.

**Syntaxe de base** :

```python
mon_dictionnaire = {
    "clé1": valeur1,
    "clé2": valeur2
}
```

### Exemple

Un dictionnaire contenant les masses molaires de quelques éléments :

```python
masses_molaires = {
    "H": 1.008,
    "O": 15.999,
    "C": 12.011
}
```

## Accéder à une valeur avec une clé

```python
print(masses_molaires["O"])  # Affiche : 15.999
```

> Si la clé n’existe pas, Python déclenche une erreur `KeyError`.

### Ajouter ou modifier une valeur

#### Ajouter :

```python
masses_molaires["N"] = 14.007
```

#### Modifier :

```python
masses_molaires["C"] = 12.01  # Correction
```

## Vérifier si une clé est présente

```python
if "H" in masses_molaires:
    print("L’hydrogène est dans le dictionnaire.")
```

## Parcourir un dictionnaire

### a) Les clés :

```python
for element in masses_molaires:
    print(element)
```

### b) Les valeurs :

```python
for valeur in masses_molaires.values():
    print(valeur)
```

* `.values()` permet d’obtenir **uniquement les valeurs** du dictionnaire, sans les clés.
* **Utile quand on veut faire un calcul avec les valeurs**, comme une moyenne ou une somme.

```python
for valeur in densites.values():
    print(valeur)
```


### c) Les paires clé-valeur :

```python
for element, masse in masses_molaires.items():
    print(f"{element} → {masse}")
```

* `.items()` permet d’obtenir les couples **clé-valeur** sous forme de paires (appelées aussi tuples en Python).
* Utile quand on veut à la fois le **nom (clé)** et la **valeur associée** pour un affichage ou un traitement.

## Supprimer une entrée

```python
del masses_molaires["H"]
```

## Utilisation fréquente en sciences

Les dictionnaires sont utiles pour :

* Associer des symboles d’éléments à des valeurs (masse molaire, charge, état)
* Regrouper des résultats par échantillon (ex. température par lieu)
* Associer des noms de gènes à leur expression

---

## Exercice

Crée un dictionnaire `densites` qui contient la densité (en g/mL) de l’eau, de l’éthanol et du mercure :

```python
densites = {
    "eau": ...,
    "éthanol": ...,
    "mercure": ...
}
```

Puis :

1. Affiche la densité du mercure.
2. Ajoute la densité de l’huile (0.91 g/mL).
3. Affiche toutes les substances et leur densité.




