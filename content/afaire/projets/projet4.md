+++
title = "Projet: Analyse de la croissance bactérienne"
weight = 134
+++

## Consigne du projet final

### Contexte :

Vous avez mené une expérience de croissance bactérienne dans un milieu nutritif contrôlé. La concentration bactérienne a été mesurée à différents moments. Vous devez analyser ces données pour comprendre la dynamique de croissance et déterminer le modèle le plus approprié (linéaire, exponentiel, logistique).

---

### Objectifs :

1. **Charger et manipuler les données expérimentales.**
2. **Analyser la progression de la population bactérienne** dans le temps.
3. **Visualiser** les résultats pour identifier un modèle de croissance.
4. **Tirer des conclusions** sur les caractéristiques de la croissance.

---

### Consignes spécifiques :

1. **Lecture et traitement des données** :

   * Charger un fichier CSV contenant les mesures de concentration bactérienne (`cfu/mL`) en fonction du temps (`heures`).
   * Vérifier les types de données et nettoyer si nécessaire.

2. **Création de fonctions** :

   * Une fonction `calculer_taux_croissance(df)` pour calculer le taux de croissance moyen entre chaque intervalle de temps.
   * Une fonction `modeliser_croissance(df)` pour proposer un modèle de croissance à partir des données observées.

3. **Visualisation avec matplotlib** :

   * Graphique de la croissance (courbe de concentration vs. temps).
   * Visualisation du taux de croissance par intervalle.
   * Comparaison avec un modèle mathématique si applicable (optionnel).

4. **Exportation** :

   * Export d’un fichier CSV contenant le temps, la concentration, les taux de croissance entre les mesures.


### Données :

Le fichier `problematique_1_croissance.csv` contient deux colonnes :

* `Temps (h)`
* `Concentration (cfu/mL)`


### Critères d’évaluation :

* **Analyse correcte des données** : traitements justes, interprétations logiques.
* **Clarté et structure du code**.
* **Pertinence des visualisations et interprétations.**
* **Capacité à proposer une modélisation simple.**


### Format du projet :

* **Durée** : À remettre à la fin de la semaine 15.
* **Livrables** :

  1. Un notebook Jupyter (`.ipynb`) avec votre travail complet.
  2. Le fichier CSV exporté avec vos résultats.
  3. Une section de **conclusion** expliquant la nature de la croissance observée.

