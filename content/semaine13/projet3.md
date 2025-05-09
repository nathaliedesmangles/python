+++
title = "Projet: Analyse de l’impact de l'entraînement sur la performance physique"
weight = 133
+++


## Consigne du projet final

### Contexte :

Une équipe d’étudiants a participé à un programme d’entraînement visant à améliorer leurs performances en course à pied. Des tests de temps de course (sur une même distance) ont été réalisés avant et après le programme. Vous devez analyser ces données pour déterminer si le programme a été efficace.

### Objectifs :

1. **Importer et manipuler les données** : Charger les données à partir d’un fichier CSV, puis préparer les données pour l’analyse.
2. **Comparer les performances** avant et après l'entraînement.
3. **Visualiser** les résultats de manière claire et significative.
4. **Interpréter les résultats** pour conclure sur l’efficacité du programme d’entraînement.

---

### Consignes spécifiques :

1. **Lecture et traitement des données** :

   * Charger les données avec `pandas`.
   * Calculer la différence entre les temps "avant" et "après" pour chaque élève.
   * Ajouter une colonne `"Amélioration"` (temps avant - temps après).

2. **Création de fonctions** :

   * Créez une fonction `calculer_amelioration(df)` qui retourne les améliorations individuelles et les statistiques globales (moyenne, écart-type).
   * Créez une fonction `interpreter_resultats(améliorations)` qui détermine si l'amélioration est significative pour l'ensemble des participants.

3. **Visualisation avec matplotlib** :

   * Diagramme en barres comparant les temps "avant" et "après" pour chaque élève.
   * Histogramme des améliorations individuelles.
   * Option : tracer une ligne horizontale représentant l’amélioration moyenne.

4. **Exportation** :

   * Exportez un fichier CSV avec les colonnes suivantes : `Nom`, `Avant`, `Après`, `Amélioration`.


### Données :

Le fichier `problematique_4_course.csv` contient les temps de course (en secondes) de plusieurs élèves avant et après un programme d’entraînement.
Colonnes :

* `Nom`
* `Avant (s)`
* `Apres (s)`


### Critères d’évaluation :

* **Précision de l’analyse** : Calculs corrects et cohérence des conclusions.
* **Qualité du code** : Code clair, bien commenté et bien structuré.
* **Visualisation** : Graphiques clairs, bien étiquetés, pertinents.
* **Interprétation** : Interprétation logique, soutenue par les données, sur l’efficacité du programme.


### Format du projet :

* **Durée** : Projet à remettre à la fin de la semaine 15.
* **Livrables** :

  1. Un fichier `.ipynb` (notebook Jupyter) avec votre analyse complète.
  2. Le fichier CSV exporté avec les résultats.
  3. Une section "Conclusion" claire dans le notebook ou en fichier PDF séparé.


