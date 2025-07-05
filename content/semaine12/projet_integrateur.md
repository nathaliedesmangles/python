+++
title = "Projet intégrateur"
weight = 112
+++


Voici l’énoncé du projet mis à jour avec les nouveaux éléments (régression linéaire, barres d’erreur, incertitudes), tout en conservant le thème **d’enquête ADN**.

---

# 🕵️‍♀️ **Projet intégrateur – Enquête scientifique par analyse d’ADN**

### Programmation scientifique en Python — Valeur : **40 %**

---

## 🔎 **Contexte**

Une scène de crime a été découverte dans un laboratoire. Des échantillons biologiques (contenant de l’ADN partiel) ont été récupérés sur place, mais les séquences sont **incomplètes ou partiellement contaminées**.

Les enquêteurs ont recueilli l’ADN de 4 suspects. L’équipe médico-légale a analysé **trois loci distincts** (zones de l’ADN) pour chaque individu. Vous avez été mandaté pour **identifier le ou les suspects les plus susceptibles de correspondre à l’échantillon retrouvé**.

Mais l’enquête ne s’arrête pas là : afin de renforcer l’analyse, vous devez également **évaluer la cohérence des correspondances entre loci** grâce à des **méthodes statistiques (régression linéaire)** et tenir compte de **l’incertitude biologique dans les séquences.**

---

## 🎯 **Tâche attendue**

Vous devez produire un **rapport scientifique interactif** (format `.ipynb`) dans lequel vous :

### 1. **Nettoyez, analysez et structurez les données ADN**

* Comparer les séquences des suspects à celles de la scène de crime malgré les caractères manquants (`?`).
* Calculer les pourcentages de correspondance pour chaque locus et la moyenne globale.

### 2. **Présentez vos résultats**

* Générer un tableau synthèse des taux de correspondance.
* Identifier le ou les suspects les plus proches du profil génétique.

### 3. **Représentez les données avec des graphiques clairs**

* Créer un **diagramme à barres** montrant la correspondance pour chaque locus et chaque suspect.
* Ajouter des **barres d’erreur** illustrant une incertitude estimée (ex: ±5 %).

### 4. **Utilisez la régression linéaire (scipy)**

* Évaluer la relation entre les scores de deux loci (ex. : `Locus_1` vs `Locus_2`).
* Tracer la **droite de régression** avec l’équation et l’incertitude sur la pente.

### 5. **Discutez vos résultats**

* Interprétez vos résultats avec rigueur.
* Distinguez les suspects potentiels, discutez les limites méthodologiques et biologiques.
* Proposez des pistes pour améliorer la précision de l’analyse.

---

## 💻 **Contraintes techniques**

* Utiliser **Python** avec **Jupyter Notebook** (`.ipynb`)
* Bibliothèques obligatoires : `pandas`, `numpy`, `matplotlib`, `scipy`
* Utiliser des fonctions personnalisées (`def`)
* Respecter les normes de **programmation lettrée** (sections Markdown, titres, explications)

---

## ⏳ **Durée**

* Devoir réalisé sur une période de **6 à 8 heures en classe** (accompagnée ou autonome)

---

## 📥 **Remise**

* Remettre un seul fichier `.ipynb` avec toutes les cellules exécutées
* Facultatif : remettre une version PDF exportée du notebook

---

Souhaites-tu que je :

* 📄 Le convertisse en document Word ou PDF ?
* 🧪 Joigne à l’énoncé les fichiers `.csv` d’exemple et un `.ipynb` de départ ?
* 💡 Ajoute une version “niveau débutant allégé” pour une adaptation pédagogique ?
