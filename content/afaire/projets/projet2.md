+++
title = "Projet: Cinétique d'une réaction chimique"
weight = 132
+++


## Consigne du projet final

### Contexte :

Dans ce projet, vous allez analyser la cinétique d'une réaction chimique en utilisant des données simulées de la concentration d’un réactif au cours du temps. Ces données vous permettront de déterminer la vitesse de la réaction et d’observer l’évolution de la concentration.

### Objectifs :

1. **Importer et manipuler les données** : Charger les données à partir du fichier CSV fourni, puis traiter et préparer les informations pour l'analyse.
2. **Analyser la cinétique** de la réaction chimique : Déterminer l’évolution de la concentration en fonction du temps et estimer des paramètres de la réaction (comme la vitesse de réaction).
3. **Visualiser** les données avec un graphique montrant l'évolution de la concentration en fonction du temps.
4. **Rédiger une conclusion** : Basée sur l’analyse des résultats, vous devrez expliquer la forme de la courbe de concentration et déterminer la nature de la réaction (par exemple, réaction de premier ordre, second ordre, etc.).

### Consignes spécifiques :

1. **Lecture et traitement des données** :

   * Importez les données à l’aide de `pandas` et affichez un résumé des données.
   * Utilisez `numpy` pour effectuer des calculs comme la variation moyenne de la concentration entre chaque mesure.
2. **Création des fonctions** :

   * Créez une fonction `taux_reaction(concentration_initiale, concentration_finale, temps)` qui calcule la vitesse de la réaction en fonction des concentrations initiale et finale et du temps.
   * Créez une fonction `analyse_reaction(temps, concentrations)` qui permet d'analyser la courbe et de déterminer la nature de la réaction (ordre de réaction).
3. **Visualisation** :

   * Utilisez `matplotlib` pour tracer la courbe de la concentration du réactif en fonction du temps.
   * Ajoutez une ligne pour la concentration initiale, la concentration finale et tracez la pente de la courbe si applicable.
4. **Exportation** :

   * Exportez un fichier CSV contenant les résultats de votre analyse, incluant la concentration du réactif à chaque instant et les vitesses de réaction calculées.

### Données :

* Le fichier CSV `problematique_3_reaction.csv` contient les données à analyser. Il est structuré comme suit :

  * `Temps (s)` : Temps écoulé depuis le début de la réaction (en secondes)
  * `Concentration (mol/L)` : Concentration du réactif à chaque instant de temps mesuré

### Critères d’évaluation :

* **Précision de l'analyse** : Exactitude des calculs et des interprétations des résultats.
* **Qualité du code** : Clarté et organisation du code, utilisation appropriée des bibliothèques (`pandas`, `numpy`).
* **Visualisation** : Graphiques clairs et pertinents, avec une bonne utilisation de `matplotlib`.
* **Interprétation des résultats** : Excellente capacité à interpréter les données et à déterminer la nature de la réaction chimique.

### Format du projet :

* **Délai** : Le projet est à rendre dans trois semaines (fin de la semaine 15).
* **Livrables** :

  1. Un notebook Jupyter contenant le code et les analyses.
  2. Le fichier CSV exporté avec les résultats.
  3. Un document PDF ou une section dans le notebook avec la conclusion sur la cinétique de la réaction.

### Ressources :

* Pandas : [https://pandas.pydata.org/](https://pandas.pydata.org/)
* Matplotlib : [https://matplotlib.org/](https://matplotlib.org/)

