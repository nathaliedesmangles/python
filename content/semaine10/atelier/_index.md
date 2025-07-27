+++
title = "Activité 10"
weight = 210
draft = false
+++
 

## Objectifs

1. Lire le fichier CSV.
2. Organiser les données dans un dictionnaire structuré.
3. Explorer les données.
4. Comparer les températures selon les substances et les conditions.

---

## Exercice

On a réalisé des expériences pour mesurer la température de cristallisation de différentes substances dans plusieurs conditions (pression normale, pression élevée, en solution aqueuse, etc.).

Les données sont enregistrées dans un fichier CSV, sous la forme suivante :

[Fichier à utiliser: cristallisation.csv](./cristallisation.csv)

Contenu :

```csv
substance,condition,temp_cristallisation
NaCl,pression_normale,801
NaCl,en_solution,800
H2O,pression_normale,0
H2O,pression_elevee,-1
Fe,pression_normale,1538
Fe,en_solution,1530
```

### Instructions

1. **Lire le fichier CSV** `cristallisation.csv` et stocker les données sous forme de dictionnaire ayant la structure suivante :

```python
{
    "NaCl": {"pression_normale": 801, "en_solution": 800},
    "H2O": {"pression_normale": 0, "pression_elevee": -1},
    "Fe": {"pression_normale": 1538, "en_solution": 1530}
}
```

2. **Afficher** les températures de cristallisation pour chaque substance dans chaque condition avec une phrase comme :

```text
NaCl cristallise à 801°C sous pression normale.
NaCl cristallise à 800°C en solution.
...
```

3. **Ajouter** une nouvelle mesure : supposons qu’on a obtenu une température de cristallisation de `-5°C` pour `H2O` dans une nouvelle condition `en_solution`. Ajoutez cette donnée au dictionnaire.

4. **Vérifiez** si la substance `"Cu"` est présente dans le dictionnaire. Si elle ne l’est pas, affichez : `"Cu n'est pas présent dans les données."`

5. **Filtrer** et afficher toutes les substances ayant une température de cristallisation inférieure à `100°C` dans au moins une condition.

6. **Comparer** les températures de cristallisation d’une même substance selon les conditions expérimentales et afficher la différence maximale observée pour chaque substance, par exemple :

```text
Pour H2O, l’écart maximal est de 5°C entre deux conditions.
```

---

### Extension pour les rapides (facultatif)

Créer une fonction `comparaison_substances(donnees)` qui :

* Compare les températures moyennes de cristallisation de chaque substance.
* Identifie quelle substance cristallise en moyenne à la température la plus élevée.