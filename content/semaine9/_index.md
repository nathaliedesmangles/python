+++
chapter = true
pre = "9."
title = " Révision ou rattrapage"
weight = 109
draft = false
+++

## Exercice de révision: Étude de la photosynthèse et de la température chez les plantes

### Objectifs pédagogiques

Cet atelier permet de :

* manipuler des **fichiers CSV** avec `pandas` et `numpy`,
* utiliser des **listes**, **chaînes**, **tableaux NumPy** et **dictionnaires**,
* produire des **graphiques professionnels** avec `matplotlib`,
* réaliser une **analyse scientifique complète** d’un jeu de données réel ou simulé,
* réviser toutes les structures de contrôle (boucles, conditions, fonctions).

### Concepts révisés

| Compétence Python                     | Présente dans l’atelier  |
| ------------------------------------- | ------------------------ |
| Listes, chaînes, boucles, conditions  | ✅                        |
| Dictionnaires                         | ✅                        |
| Tableaux NumPy et fonctions `np.*`    | ✅                        |
| Manipulation de fichiers `.csv`       | ✅ (avec pandas)          |
| Visualisation avec matplotlib         | ✅                        |
| Régression linéaire (bonus)           | ✅                        |
| Fonctions personnalisées (facultatif) | ✅ (à intégrer au besoin) |

---

### Contexte scientifique

Un groupe de biologistes a mené une expérience pour étudier l'effet de la **température** sur l’**efficacité de la photosynthèse** chez plusieurs espèces végétales.

Ils ont récolté les données suivantes :

* Température (°C),
* Taux de photosynthèse (μmol CO₂/m²/s),
* Espèce (nom),
* Nom du capteur utilisé (chaîne de caractères),
* Date de la mesure.

Les données sont stockées dans un fichier `.csv` nommé **`photosynthese.csv`**, dont voici un aperçu :

| Température | Taux | Espèce      | Capteur    | Date       |
| ----------- | ---- | ----------- | ---------- | ---------- |
| 22.5        | 18.2 | Arabidopsis | capteur-01 | 2023-06-01 |
| 24.1        | 19.3 | Arabidopsis | capteur-02 | 2023-06-01 |
| 28.0        | 20.5 | Maïs        | capteur-03 | 2023-06-02 |
| ...         | ...  | ...         | ...        | ...        |

---

### Instructions

#### Étape 1 – Lecture et nettoyage des données

1. Charge le fichier CSV avec **`pandas`**.
2. Vérifie la présence de données manquantes (`NaN`) et nettoie-les si nécessaire.
3. Transforme les colonnes **Température** et **Taux** en tableaux **NumPy**.

#### Étape 2 – Analyse par espèce (listes et dictionnaires)

1. Crée un dictionnaire dont les clés sont les noms des **espèces**, et les valeurs sont des **listes de taux de photosynthèse**.
2. Calcule pour chaque espèce :

   * la moyenne,
   * l’écart-type,
   * le nombre de mesures.

> Tu peux stocker ces résultats dans un second dictionnaire (`résumé[espèce] = {...}`).

#### Étape 3 – Analyse graphique

1. Trace un **nuage de points** température vs taux pour chaque espèce (couleurs différentes).
2. Ajoute une **droite de régression linéaire** pour chaque espèce.
3. Sauvegarde le graphique en PNG.

#### Étape 4 – Recherche par capteur (chaînes et conditions)

1. Demande à l’utilisateur le nom d’un capteur (`input()`).
2. Affiche toutes les mesures associées à ce capteur :

   * date, température, taux, espèce.

#### Étape 5 – Exploration temporelle (tri et regroupement)

1. Trie les données par **date**.
2. Pour chaque date, calcule le **taux moyen global**.
3. Affiche une **courbe de tendance** (date vs taux moyen).

---

### 📁 Bonus : Fichier CSV simulé

Si tu veux que je génère aussi le fichier **`photosynthese.csv`** et le **notebook corrigé**, je peux te les fournir immédiatement.

Souhaites-tu les fichiers ? Ou une version non corrigée pour les étudiants ?
