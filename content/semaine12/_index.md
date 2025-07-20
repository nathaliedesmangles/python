+++
chapter = true
pre = "<b>12.</b>"
title = " Projet - Présentation et analyse"
weight = 112
draft = false
+++


## Objectifs

* Présentation du projet
* Présentation de la grille de correction
* Analyse préliminaire du projet (activité guidée):
	* Comprendre le problème
	* Identifier les variables (types), constantes, formules, fonctions, etc.
	* Élaborer les algorithmes

---

## Contraintes techniques

* Utiliser **Python** avec **Jupyter Notebook** (`.ipynb`)
* Utiliser le bloc-notes `projet_enquete_adn.ipynb` et le fichier de données `suspects.csv` se trouvant sur Moodle.
* Bibliothèques obligatoires : uniquement `pandas`, `numpy`, `matplotlib`, `scipy`
* Utiliser des fonctions personnalisées (`def`)
* Respecter les normes de **programmation lettrée** (sections Markdown, titres, explications)

---

## Remise

* Remettre un seul fichier `projet_prenom_nom.ipynb` avec toutes les cellules exécutées.
* **Facultatif** : remettre une version PDF exportée du bloc-notes.

---

# Enquête scientifique par analyse d’ADN

## Contexte

Une scène de crime a été découverte dans un laboratoire. Des échantillons biologiques (contenant de l’ADN partiel) ont été récupérés sur place, mais les séquences sont **incomplètes ou partiellement contaminées**.

Les enquêteurs ont recueilli l’ADN de 4 suspects. L’équipe médico-légale a analysé **trois loci distincts** (zones de l’ADN) pour chaque individu. Vous avez été mandaté pour **identifier le ou les suspects les plus susceptibles de correspondre à l’échantillon retrouvé**.

Mais l’enquête ne s’arrête pas là : afin de renforcer l’analyse, vous devez également **évaluer la cohérence des correspondances entre loci** grâce à des **méthodes statistiques (régression linéaire)** et tenir compte de **l’incertitude biologique dans les séquences.**


## Tâche attendue

Votre mission, à supposer que vous l'acceptiez 😬, consiste à analyser des données scientifiques à l’aide de **Python**, afin d’en extraire des résultats fiables, illustrés par des graphiques clairs et rigoureux.

Comme toujours, si vous ou l’un de vos collègues échouez dans cette tâche ou générez des erreurs d’exécution, l’enseignante niera toute responsabilité 😉.
Ce bloc-notes pourrait bien s’autodétruire en cas de fautes de syntaxe critiques.

Bonne chance... et que la science soit avec vous ! 😉

Dans votre **rapport scientifique interactif** vous devrez:

### 1. Nettoyer, analyser et structurer les données ADN

* Comparer les séquences des suspects à celles de la scène de crime malgré les caractères manquants (`?`).
* Calculer les pourcentages de correspondance pour chaque locus et la moyenne globale.

### 2. Présenter vos résultats

* Générer un tableau synthèse des taux de correspondance.
* Identifier le ou les suspects les plus proches du profil génétique.

### 3. Représenter les données avec des graphiques clairs

* Créer un **diagramme à barres** montrant la correspondance pour chaque locus et chaque suspect.
* Ajouter des **barres d’erreur** illustrant une incertitude estimée (ex: ±5 %).

### 4. Utiliser la régression linéaire (scipy)

* Évaluer la relation entre les scores de deux loci (ex. : `Locus_1` vs `Locus_2`).
* Tracer la **droite de régression** avec l’équation et l’incertitude sur la pente.

### 5. Discuter de vos résultats

* Interprétez vos résultats avec rigueur.
* Distinguez les suspects potentiels, discutez les limites méthodologiques et biologiques.
* Proposez des pistes pour améliorer la précision de l’analyse.