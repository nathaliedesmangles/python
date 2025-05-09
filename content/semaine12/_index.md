+++
chapter = true
pre = "<b>Semaine 12.</b>"
title = "Examen 2 (30%)"
weight = 120
+++

# Examen formatif
## Description

**Type** : Activité formative  
**Durée** : 2h40  
**But** : Révision collaborative, application active  
**Modalité :** Individuelle – Accès aux notes de cours permis, mais aucun partage entre étudiants.
**Outils autorisés :** Jupyter Notebook avec Anaconda (numpy, pandas, matplotlib intégrés)

Cette activité n’est pas notée, mais vous recevrez une **rétroaction qualitative** sur :

* La clarté et la structure de votre code
* Votre capacité à repérer et expliquer des erreurs

**Notions évaluées**

* Fonctions définies par l'utilisateur
* Structures de données (listes et dictionnaires)
* Bibliothèques **numpy** et **pandas**
* Visualisation avec **matplotlib**
* Lecture/écriture de fichiers **CSV**


---
## Consigne générale

### Contexte scientifique : Étude d’une expérience de fermentation

Un laboratoire a mesuré la concentration de dioxyde de carbone (CO₂) produite par un mélange de levure et de sucre dans un récipient fermé, à intervalles de 10 minutes pendant 2 heures. Ces données ont été enregistrées dans un fichier CSV.


### Fichier fourni : `fermentation_co2.csv`

Contenu du fichier :

```
Temps (min),CO2 (mg/L)
0,0
10,5.2
20,10.4
30,17.5
40,25.1
50,32.0
60,38.5
70,43.2
80,46.0
90,48.1
100,49.2
110,49.8
120,50.0
```


### Partie 1 – Lecture et traitement des données (30 %)

1. Lire le fichier CSV à l’aide de `pandas`.
2. Convertir la colonne CO2 en tableau numpy et calculer :

   * la moyenne
   * l’écart-type
   * la variation maximale entre deux mesures consécutives
3. Créer un dictionnaire associant chaque temps à la variation de CO₂ depuis la mesure précédente.

### Partie 2 – Fonctions personnalisées (25 %)

1. Écrire une fonction `variation(co2)` qui prend une liste de valeurs de CO₂ et retourne une nouvelle liste des variations absolues entre chaque mesure et la précédente.
2. Écrire une fonction `alerte_variation(var, seuil)` qui retourne les indices où la variation dépasse un seuil donné (par exemple 5 mg/L).

### Partie 3 – Visualisation des données (20 %)

1. Tracer un graphique montrant la concentration de CO₂ en fonction du temps.
2. Ajouter au graphique une ligne horizontale représentant la moyenne de CO₂.
3. Ajouter une annotation (flèche ou texte) au moment où la variation maximale s’est produite.

### Partie 4 – Exportation des résultats (15 %)

1. Ajouter une colonne "Variation\_CO2" au DataFrame.
2. Écrire un nouveau fichier `fermentation_analyse.csv` avec les colonnes :

   * Temps (min)
   * CO2 (mg/L)
   * Variation\_CO2

### Partie 5 – Interprétation et conclusion (10 %)

1. En 4 à 5 lignes, résumez :

   * L’allure générale de l’évolution du CO₂
   * Le moment où l’activité fermentaire est la plus intense
   * Une hypothèse sur le ralentissement ou la stabilisation observée


### Critères de correction (résumé)

| Section                     | Pondération | Éléments évalués                              |
| --------------------------- | ----------- | --------------------------------------------- |
| Lecture et traitement       | 30 %        | Lecture correcte, calculs numpy, dictionnaire |
| Fonctions                   | 25 %        | Syntaxe, utilité, bon usage des structures    |
| Graphique                   | 20 %        | Clarté, précision, annotations                |
| Fichier exporté             | 15 %        | Structure correcte, données exactes           |
| Interprétation scientifique | 10 %        | Clarté, pertinence de l’analyse               |




