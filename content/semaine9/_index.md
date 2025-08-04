+++
chapter = true
pre = "9."
title = " Révision ou rattrapage"
weight = 109
draft = false
+++

[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_revision.ipynb)

[Fichier à utiliser: conductivite.csv](./conductivite.csv)


## Exercice 1 : Neutralisation acide-base (chimie)

**Notions** : conditions, boucles, dictionnaire, fonctions
**Contexte** : Un technicien doit ajuster progressivement le volume d’une base versée dans une solution acide pour atteindre un pH proche de 7.
**Tâche** :

* Simule une titration acide-base par paliers de 0.5 mL.
* Utilise une fonction `pH(volume_base)` (fourni ou à coder selon une loi empirique simplifiée).
* Arrête la simulation dès que le pH est compris entre 6.8 et 7.2.
* Affiche tous les volumes testés avec leur pH.

> Variante : Représente les valeurs sur un graphique volume vs pH pour visualiser le point d'équivalence.



## Exercice 2 : Série de désintégrations radioactives

**Notions** : boucles, listes, math, NumPy, fonctions
**Contexte** : Une substance radioactive se désintègre au fil du temps, et on veut modéliser la quantité restante.
**Tâche** :

* Simule la désintégration d’un isotope avec une demi-vie donnée.
* Crée une fonction `quantite_restante(q0, t, demivie)` qui retourne la quantité après t secondes.
* Génère et affiche la liste des quantités pour t = 0 à 60 s par pas de 5.
* Trace la courbe avec `matplotlib`.

> Variante : Ajouter un bruit expérimental (± 5%) et comparer avec la courbe théorique.



## Exercice 3 : Titrage par conductimétrie

**Notions** : dictionnaire, csv, matplotlib, compréhension de données
**Contexte** : Une série de mesures de conductivité sont enregistrées à chaque ajout de 1 mL de réactif.
**Tâche** :

* Lis un fichier `conductivite.csv` contenant deux colonnes : `volume`, `conductivite`.
* Affiche les données et trace le graphique.
* Calcule la pente moyenne avant et après l’équivalence pour déterminer approximativement le volume d’équivalence.
* Affiche ce volume estimé.

> Variante : Ajouter une estimation par interpolation entre deux points.



## Exercice 4 : Suivi d’un indicateur coloré (absorbance)

**Notions** : fonctions, tableaux NumPy, matplotlib, régression linéaire
**Contexte** : L’absorbance d’un indicateur est mesurée pour plusieurs concentrations connues (loi de Beer-Lambert).
**Tâche** :

* Enregistre les valeurs de concentration (mol/L) et d’absorbance dans des tableaux.
* Trace le nuage de points.
* Calcule la pente et l’ordonnée à l’origine de la droite de régression.
* Utilise la droite pour estimer la concentration d’une solution inconnue.

> Variante : Ajouter les barres d’erreur sur l’absorbance.



## Exercice 5 : Simulation de friction sur une rampe inclinée (physique)

**Notions** : input, conditions, boucles, fonctions, matplotlib
**Contexte** : Un objet glisse sur une rampe inclinée avec ou sans friction.
**Tâche** :

* Demande à l’utilisateur l’angle, la masse et le coefficient de friction.
* Calcule la force nette et l’accélération.
* Simule la position et la vitesse sur 10 secondes (delta t = 0.1 s).
* Affiche les positions et trace la courbe position vs temps.

> Variante : Comparer les trajectoires avec et sans friction sur un même graphique.


---

## 2. Atelier

[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/atelier_revision.ipynb)

### Étude de la photosynthèse et de la température chez les plantes

Cet atelier permet de :

* manipuler des **fichiers CSV** avec `pandas` et `numpy`,
* utiliser des **listes**, **chaînes**, **tableaux NumPy** et **dictionnaires**,
* produire des **graphiques professionnels** avec `matplotlib`,
* réaliser une **analyse scientifique complète** d’un jeu de données réel ou simulé,
* réviser toutes les structures de contrôle (boucles, conditions, fonctions).

### Concepts révisés

| Compétence Python                     |
| ------------------------------------- |
| Listes, chaînes, boucles, conditions  |
| Dictionnaires                         |
| Tableaux NumPy et fonctions `np.*`    |
| Manipulation de fichiers `.csv`       |
| Visualisation avec matplotlib         |
| Régression linéaire                   |
| Fonctions personnalisées (facultatif) |

---

### Contexte scientifique

Un groupe de biologistes a mené une expérience pour étudier l'effet de la **température** sur l’**efficacité de la photosynthèse** chez plusieurs espèces végétales.

Ils ont récolté les données suivantes :

* Température (°C),
* Taux de photosynthèse (μmol CO₂/m²/s),
* Espèce (nom),
* Nom du capteur utilisé (chaîne de caractères),
* Date de la mesure.

Les données sont stockées dans le fichier `.csv` disponible ici : [photosynthese.csv](./photosynthese.csv), dont voici un aperçu :

| Température | Taux | Espèce      | Capteur    | Date       |
| ----------- | ---- | ----------- | ---------- | ---------- |
| 22.5        | 18.2 | Arabidopsis | capteur-01 | 2023-06-01 |
| 24.1        | 19.3 | Arabidopsis | capteur-02 | 2023-06-01 |
| 28.0        | 20.5 | Maïs        | capteur-03 | 2023-06-02 |
| ...         | ...  | ...         | ...        | ...        |

---

### Instructions

#### Étape 1 – Lecture et nettoyage des données

1. Charger le fichier CSV avec **`pandas`**.
2. Vérifier la présence de données manquantes (`NaN`) et les nettoyer si nécessaire.
3. Transformer les colonnes **Température** et **Taux** en tableaux **NumPy**.

#### Étape 2 – Analyse par espèce (listes et dictionnaires)

1. Créer un dictionnaire dont les clés sont les noms des **espèces**, et les valeurs sont des **listes de taux de photosynthèse**.
2. Calculer pour chaque espèce :

   * la moyenne,
   * l’écart-type,
   * le nombre de mesures.

> Vous pouvez stocker ces résultats dans un second dictionnaire (`résumé[espèce] = {...}`).

#### Étape 3 – Analyse graphique

1. Tracer un **nuage de points** température vs taux pour chaque espèce (couleurs différentes).
2. Ajouter une **droite de régression linéaire** pour chaque espèce.
3. Sauvegarder le graphique en PNG.

![Nuage - régression](./photosynthese_regression.png?width=45vw)

#### Étape 4 – Recherche par capteur (chaînes et conditions)

1. Demander à l’utilisateur le nom d’un capteur (`input()`).
2. Afficher toutes les mesures associées à ce capteur :

   * date, température, taux, espèce.

#### Étape 5 – Exploration temporelle (tri et regroupement)

1. Trier les données par **date**.
2. Pour chaque date, calculer le **taux moyen global**.
3. Afficher une **courbe de tendance** (date vs taux moyen).