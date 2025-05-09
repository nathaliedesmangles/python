+++
title = "Projet: Effet de la caféine sur la fréquence cardiaque"
weight = 131
+++


## Consigne du projet final 

### Contexte :

Dans ce projet, vous allez analyser l'impact de la consommation de caféine sur la fréquence cardiaque. Les données collectées concernent la fréquence cardiaque de quatre sujets avant et après consommation de café à des intervalles de 30 minutes.

### Objectifs

1. **Importer et manipuler les données** : Vous allez charger les données dans un DataFrame `pandas` à partir du fichier CSV fourni et effectuer un traitement pour extraire les informations pertinentes.
2. **Analyser la variation** de la fréquence cardiaque après la consommation de café.
3. **Visualiser** les tendances de la fréquence cardiaque pour chaque sujet avec un graphique linéaire, en mettant en évidence l'effet de la consommation de café sur la fréquence cardiaque.
4. **Faire des comparaisons** entre les sujets et interpréter les résultats. Vous allez calculer des statistiques descriptives (moyenne, écart-type) et identifier les variations notables dans les données.
5. **Rédiger une conclusion** sur l'impact de la caféine sur la fréquence cardiaque, en basant votre analyse sur les résultats obtenus.

### Consignes spécifiques :

1. **Lecture et traitement des données** :

   * Importez les données à l'aide de `pandas` et affichez un résumé des données.
   * Utilisez `numpy` pour effectuer des calculs comme la moyenne et l'écart-type de la fréquence cardiaque pour chaque sujet avant et après l'ingestion de café.

2. **Création des fonctions** :

   * Créez une fonction `variation(frequence)` qui calcule les variations de fréquence cardiaque entre les mesures (avant et après).
   * Créez une fonction `analyser_impact(frequences_avant, frequences_apres)` qui retourne la différence moyenne de la fréquence cardiaque et des statistiques de variation.

3. **Visualisation** :

   * Utilisez `matplotlib` pour tracer l’évolution de la fréquence cardiaque pour chaque sujet avant et après l’ingestion de café.
   * Ajoutez une ligne horizontale pour la fréquence cardiaque moyenne avant consommation et une autre pour la fréquence après consommation.

4. **Exportation** :

   * Exportez un fichier CSV contenant les résultats de votre analyse, incluant les variations de fréquence cardiaque pour chaque sujet.

### Données :

* Le fichier CSV `problematique_1_cafeine.csv` contient les données à analyser. Il est structuré comme suit :

  * `Sujet` : Nom du sujet (A, B, C, D)
  * `Temps (min)` : Temps écoulé depuis le début de l’expérience (en minutes)
  * `Frequence (bpm)` : Fréquence cardiaque (battements par minute)

### Critères d’évaluation :

* **Précision de l'analyse** : Exactitude des calculs et des interprétations statistiques.
* **Qualité du code** : Clarté et organisation du code, utilisation adéquate des structures de données (`pandas`, `numpy`).
* **Visualisation** : Graphiques clairs et pertinents, avec une bonne utilisation de `matplotlib`.
* **Clarté de la conclusion** : Interprétation logique des résultats et conclusion sur l’effet de la caféine sur la fréquence cardiaque.

### Format du projet :

* **Délai** : Le projet est à rendre dans trois semaines (fin de la semaine 15).
* **Livrables** :

  1. Un notebook Jupyter contenant le code et les analyses.
  2. Le fichier CSV exporté avec les résultats.
  3. Un document PDF ou une section dans le notebook avec la conclusion.

### Ressources :

* Pandas : [https://pandas.pydata.org/](https://pandas.pydata.org/)
* Matplotlib : [https://matplotlib.org/](https://matplotlib.org/)

