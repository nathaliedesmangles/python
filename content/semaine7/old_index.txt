+++
chapter = true
pre = "<b>Semaine 8.</b>"
title = "Structures de données (listes, dictionnaires)"
weight = 80
+++


## Objectifs de la leçon

À la fin de cette leçon, vous devrez être capable de :

* Créer et manipuler une **liste** pour stocker une collection ordonnée de données
* Créer un **dictionnaire** pour représenter des associations clé-valeur
* Choisir la structure appropriée selon le contexte scientifique

---

## Listes (`list`)

Une **liste** est une structure **ordonnée et modifiable**.

### Création d’une liste

```python
temperatures = [22.1, 23.5, 21.8]
prenoms = ["louise", "georges", "mohammed", "julie"]
```

### Accès aux éléments

```python
print(temperatures[0])  # Affiche : 22.1
print(prenoms[2])  # Affiche : mohammed
```

### Ajout, suppression et modification

```python
temperatures.append(24.0)     # Ajout
temperatures[1] = 23.0        # Modification
del temperatures[0]           # Suppression
```

### Parcours d’une liste

```python
for t in temperatures:
    print(t)
```


## Dictionnaires (`dict`)

Un **dictionnaire** permet d’associer une **clé** à une **valeur**. Il est **non ordonné (jusqu’à Python 3.6)** mais très utile pour organiser des données complexes.

### Exemple

```python
element = {
    "symbole": "O",
    "nom": "Oxygène",
    "masse": 15.999
}
```

### Utilisations typiques

* Propriétés d’un élément chimique
* Informations biologiques sur une espèce
* Données de capteurs (clé = date, valeur = mesure)


## Combinaison des deux structures

On peut combiner les structures entre elles :

* **Liste de dictionnaires**

```python
especes = [
    {"nom": "Grenouille", "taille": 9},
    {"nom": "Salamandre", "taille": 15}
]
```


## Comparaison des structures

| Structure    | Ordonnée | Modifiable | Accès par | Utilisation typique                                                    |
| ------------ | -------- | ---------- | --------- | ---------------------------------------------------------------------- |
| Liste        | Oui      | Oui        | Index     | Série de données homogènes (températures, notes, etc.)                 |
| Dictionnaire | Non\*    | Oui        | Clé       | Représenter des objets complexes (éléments, espèces, mesures par date) |

\* En pratique, depuis Python 3.7+, l'ordre des clés est conservé.


