+++
chapter = true
pre = "<b>12-14</b>"
title = " Projet - Présentation, analyse et traduction"
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

## Enquête scientifique par analyse d’ADN

### Contexte

Vous êtes le ou la bioinformaticien·ne en charge d’une **enquête médico-légale** : votre rôle est d’identifier, à partir de données génétiques partielles, le ou les suspects les plus compatibles avec un échantillon d’ADN trouvé sur une scène de crime.

Mais votre mission ne s'arrête pas à un simple tri de valeurs : vous devrez aussi **modéliser les relations génétiques** par analyse statistique, **quantifier l’incertitude**, et **présenter vos résultats de manière claire et rigoureuse** à l’aide de Python.


### Contraintes techniques

* **Fichiers de départ** : Bloc-notes de travail `projet_enquete_adn.ipynb` et le fichier de données contenant les profils ADN `suspects.csv` se trouvant sur Moodle.  
* **Langage** : Python dans Jupyter Notebook (`.ipynb`).  
* **Bibliothèques autorisées** : `pandas`, `numpy` et `matplotlib`  
* **Programmation lettrée** : structurez votre rapport avec des **sections Markdown**, des **titres explicites**, et des **explications claires**.  
* **Fonctions personnalisées** : vous devez créer vos propres fonctions à l’aide de `def`, avec paramètres et valeurs retournées, pour automatiser les analyses.  
* **Normes** : code lisible, modulaire, commenté.


### Remise

* Remettre **un seul fichier** : `projet_prenom_nom.ipynb`, toutes cellules **exécutées**.
* **Facultatif** : joindre une version PDF exportée du bloc-notes.


### Rappel : vos superpouvoirs Python

* Pensez à tester chaque fonction sur des **cas simples** avant de l’appliquer aux données complètes.
* Utilisez les **cellules Markdown** pour documenter vos choix et expliquer votre démarche.
* Soyez créatifs·ves, mais rigoureux·ses.


### Bonne enquête !

Que la science éclaire vos soupçons… et que votre code résiste à toutes les erreurs !

---

## Étapes de votre enquête (guide progressif)

### 1. Élaboration de votre plan de travail

**Avant de coder**, rédigez une **brève stratégie** :

* Quelles sont les étapes de l’enquête ?
* Quelles fonctions pourriez-vous créer pour structurer votre code (par exemple : comparaison, calcul, affichage graphique, etc.) ?
* Dans quel ordre allez-vous procéder ?

> Cette planification peut évoluer en cours de route, mais elle doit être claire dès le départ.


### 2. Chargement et nettoyage des données

* Importez les bibliothèques autorisées.
* Chargez le fichier `suspects.csv`.
* Observez la structure des données.
* Identifiez les **caractères manquants** (ex. `?`) et préparez vos fonctions pour gérer ces cas lors des comparaisons.

> Créez une fonction pour comparer deux séquences ADN et calculer le **pourcentage de correspondance** malgré les caractères ambigus.


### 3. Calculs de correspondance

* Pour chaque suspect et pour chaque locus, **comparez sa séquence** avec celle trouvée sur la scène de crime.
* Calculez :

  * Le **taux de correspondance par locus** (en %)
  * La **moyenne globale de correspondance**

> Créez des fonctions réutilisables pour ces calculs. Par exemple : `calculer_correspondance(sequence1, sequence2)`, `analyser_suspects(df)`…


### 4. Résumé et visualisation des résultats

* Présentez les **taux de correspondance** dans un **tableau synthèse** (DataFrame).
* **Identifiez les suspects** ayant les correspondances les plus élevées.
* Représentez les résultats avec :

  * Un **diagramme à barres** (correspondance par locus, par suspect)
  * Des **barres d’erreur** illustrant l’incertitude estimée (±5 %)

> Créez une fonction pour générer ces graphiques à partir d’un DataFrame.


### 5. Analyse statistique (régression linéaire)

* Choisissez deux loci (ex. : Locus_1 et Locus_2).
* Utilisez `NumPy` pour :

  * Obtenir la pente, l’interception, le R² et l’incertitude sur la pente.
  * Tracer la droite de régression sur un nuage de points (scores par suspect).
  * Afficher l'équation de la droite et l’erreur sur la pente.

> Vous pouvez créer une fonction comme `analyser_relation_loci(df, locus1, locus2)`.


### 6. Interprétation scientifique

Dans une section Markdown :

* **Concluez** sur les suspects les plus probables.
* Discutez de :

  * La **qualité des données**
  * L'impact des **caractères manquants**
  * La **valeur explicative** de vos analyses statistiques
  * D’éventuelles **améliorations** (plus de loci, meilleure qualité des échantillons, approches bioinformatiques plus avancées…)


<!--

==================

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

## Bonus (facultatif)

Ajoutez une courte section **“Limites biologiques et bioinformatiques”** :

* Quelles erreurs pourraient exister dans un contexte réel ?
* Pourquoi la correspondance ADN n’est-elle pas une preuve absolue ?
-->