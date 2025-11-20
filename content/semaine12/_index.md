+++
chapter = true
pre = "<b>12-14</b>"
title = " 🧬 Projet intégrateur — L’ADN du coupable"
weight = 112
draft = false
+++


## Informations générales

> **Durée :** 3 semaines (en classe)  
> **Pondération :** 15 % de la note finale  
> **Thème scientifique :** biologie moléculaire et identification génétique  
> **En équipe :** de 1 😉 2 ou 3 maximum.  

## Pour ceux qui sont **en équipe** et souhaitent pouvoir **travailler à distance** :

1. Il faut installer l'extension ***Live Share*** sur Visual Studio Code	
   > Elle doit déjà être installée sur les ordinateurs au cégep
2. Suivre les étapes dans la vidéo [Installation et mise en route de Live Share](https://youtu.be/nf0xHJ2tQjU?si=e3Smn0_mtqefDsFr)



## Résumé des compétences évaluées

* Lecture et traitement de fichiers scientifiques (`pandas`)
* Calculs et modélisation numériques (`numpy`)
* Représentations graphiques (`matplotlib`)
* Logique algorithmique et tri (boucle `for`)
* Communication scientifique et analyse critique


## Fichiers fournis sur Moodle

- `adn_suspects.csv` — contient les données de 150 suspects (nom et valeurs de 3 loci).  
- `adn_crime.csv` — contient les 3 valeurs de l’ADN trouvé sur la scène du crime.  
- `projet_adn_etudiant.ipynb` - Le bloc-notes de départ à utiliser.  
- `grille_correction_adn_coupable.pdf` - La grille de correction du projet.


## Fichiers à remettre sur Moodle

* `projet_prenom_nom.ipynb` - Le bloc-notes complété avec votre code.
* `adn_suspects_corrige.csv` - contient les données nettoyées pour les 150 suspects.  
* `resultats.csv` - contient les données des 10 premiers suspects.  
* Les 3 graphiques :
	* `graphique_top10_3loci.png` - Top 10 des suspects les plus proches (3 loci)  
	* `graphique_regression_locus1_locus2.png` - Corrélation entre Locus1 et Locus2  
	* `graphique_bruit_locus.png` - Effet du bruit expérimental sur les valeurs d'un Locus


## Bibliothèques autorisées et contraintes pédagogiques

* Numpy
* Pandas
* Matplotlib.pyplot

* <b style="color:red;">Aucune fonction non apprise dans le cours n'est autorisée. Toute fonction ou méthode ne faisant pas partie du cours sera considérée comme du plagiat.</b>

{{% notice style="red" icon="warning" style="warning" title="Remises hebdomadaires" %}}
* Afin de suivre votre avancée, **à chaque fin de cours, avant de quitter**, vous devez déposer votre fichier .ipynb sur Moodle.
* Une remise manquante entrainera une **pénalité de 10%/jours de retard (tel que prescrit par la PIEA article 7.4.2)**.
* La remise finale sur Moodle doit être faite **au plus tard la veille de l'examen 3 (semaine 15)**. En cas de non respect de ce délai, une **pénalité de 10%/jours de retard** sera aussi appliquée, **après quatre jours de retard**, sans égard aux congés, la **note de 0** sera attribuée. 
* Seule la dernière remise sera évaluée.
{{% /notice %}}


## Grille d’évaluation

| Section                                 | Critères                                                                                      | Pts    |
| --------------------------------------- | --------------------------------------------------------------------------------------------- | :------: |
| **1. Lecture et nettoyage des données** | Lecture correcte des fichiers CSV. <br>Calculs de moyennes et écart-types.<br> remplacement des NaN | 10
| **2. Calculs et logique de tri**        | Distance euclidienne correcte.<br> Respect des contraintes.<br> Tri manuel avec boucles. | 20 
| **3. Visualisations scientifiques**     | Graphique en barres (Top 10).<br>Scatter + droite de régression.<br>Mise en forme claire. | 20
| **4. Modélisation & bruit** | 4ᵉ locus estimé. <br>Bruit expérimental simulé.<br>Export `resultats.csv` réussi.   | 25
| **5. Rapport scientifique**             | Interprétation, clarté, rigueur et conclusion cohérente.<br> Commentaires clairs, exécution sans erreur.    | 25


---

## Quelques définitions

{{% notice style="green" title="Locus / Loci et Distances euclidiennes (3D, 4D)" groupid="notice-toggle" expanded="false" %}}
 1. Un **locus** (pluriel **loci**) désigne **l’emplacement précis d’un gène ou d’une séquence d’ADN sur un chromosome**.  
 
 **Contexte biologique :**  
 * Chaque individu possède deux copies de chaque locus (une d’origine maternelle et une d’origine paternelle).  
 * Un même locus peut contenir **plusieurs versions d’un gène**, appelées **allèles**.  
 * L’analyse de plusieurs loci permet de **comparer les profils ADN** de différents individus, comme dans les enquêtes criminelles ou les tests de filiation.  
 

2. La **distance euclidienne** mesure **la différence numérique entre deux ensembles de valeurs**, souvent utilisées pour **comparer des profils génétiques** ou **des séquences d’ADN**.
 
 **Formule mathématique) (pour **`n`** loci) :**
```math
 $$
 d = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + \ldots + (x_n - y_n)^2}
 $$
```
 où chaque $(x_i\)$ et $(y_i\)$ représente la valeur d’un même locus chez deux individus.

3. Une **distance 3D** est une comparaison dans un espace à **trois dimensions**, correspondant ici aux trois premiers loci (`Locus1`, `Locus2`, `Locus3`).  
Chaque suspect est représenté par un point dans cet espace, et la **distance euclidienne** entre le suspect et le profil du crime est donnée par :

```math
$$
d_{3D} = \sqrt{(L1_s - L1_c)^2 + (L2_s - L2_c)^2 + (L3_s - L3_c)^2}
$$
```

**Interprétation**:

 * Une **petite distance euclidienne** → profils ADN **très similaires**.    
 * Une **grande distance** → profils **différents**.   

Dans ce projet, chaque locus ADN varie entre **0,40 et 0,70**, donc une différence maximale d’environ **0,30 par locus**.  
La distance totale (3 loci) peut ainsi varier entre **0,00 et ~0,52** :

| Distance (3D) | Interprétation |
|----------------|----------------|
| **d < 0.10** | Profils presque identiques — suspect très probable |
| **0.10 ≤ d < 0.20** | Profils similaires — suspect plausible |
| **0.20 ≤ d < 0.30** | Profils différents — faible probabilité |
| **d ≥ 0.30** | Profils incompatibles — suspects distincts |


4. Lorsqu’on ajoute un **4ᵉ locus estimé** (`Locus4_estime`) grâce à une régression linéaire,  
on travaille alors dans un espace à **quatre dimensions** :

```math
$$
d_{4D} = \sqrt{(L1_s - L1_c)^2 + (L2_s - L2_c)^2 + (L3_s - L3_c)^2 + (L4_s - L4_c)^2}
$$
```

 **Interprétation possible :**  

| Observation | Interprétation possible |
|--------------|------------------------|
| **d₄D < d₃D** | La modélisation affine (corrélation entre loci) **renforce la similarité** : le suspect devient encore plus compatible avec le profil du crime. |
| **d₄D ≈ d₃D** | Le 4ᵉ locus estimé **n’apporte pas d’information nouvelle** : la modélisation ne modifie pas la conclusion. |
| **d₄D > d₃D** | L’ajout du 4ᵉ locus **augmente l’écart global** : le modèle révèle une incohérence génétique ou une surestimation. |

5. Le **bruit** est généré avec une loi normale centrée sur 0 (sans biais).

* Chaque valeur du locus est donc légèrement modifiée dans une plage typique de ±0,01.
* Cela correspond à une incertitude de mesure de ±1 % à ±2 %.

 **Interprétation possible :**  

| Comparaison                | Interprétation                                                                                                            |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **d_bruitée ≈ d_initiale** | Le modèle est **robuste** : le bruit n’affecte pas la conclusion, le suspect reste le même.                               |
| **d_bruitée < d_initiale** | Le bruit a **réduit légèrement l’écart** : le modèle semble même un peu plus cohérent (effet aléatoire non significatif). |
| **d_bruitée > d_initiale** | Le bruit **augmente la distance** : les écarts sont amplifiés, le modèle est plus sensible aux variations.                | 

{{% /notice %}}


## Objectifs généraux

* Identifier le suspect dont le profil génétique est le plus proche de l’échantillon d’ADN retrouvé sur la scène de crime.  
* Effectuer l’analyse à partir de **données réelles simulées** pour 150 suspects et 3 loci d’ADN.  
* Utiliser les outils de **programmation scientifique en Python** (avec `numpy`, `pandas`, `matplotlib`).


## Étapes du projet

### 1. Exportations des bibliothèques

***Déjà inclu dans le fichier de départ .ipynb***

### 2. Lecture des fichiers CSV

**Objectif**: Charger les données des suspects et du crime dans deux DataFrame distincts.

* Lire le fichier `adn_suspects.csv` dans un DataFrame nommé `suspects`.
* Lire le fichier `adn_crime.csv` dans un DataFrame nommé `crime`.
* Utiliser `delimiter=";"` et `decimal=","`.
* Afficher les 5 premières lignes de `suspects` avec `.head()` pour vérifier la lecture.


### 3. Aperçu et statistiques

**Objectif**: Vérifier que les valeurs des loci sont valides.

* Afficher les statistiques des colonnes `Locus1`, `Locus2`, `Locus3`.
* Vérifier (à l'oeil) que les valeurs sont entre environ 0.40 et 0.70.


### 4. Nettoyage des NaN

**Objectif** : Remplacer les valeurs manquantes par la moyenne de chaque colonne.

* Vérifier le nombre de `NaN` dans les trois loci.
* Pour chaque locus :
  * Calculer la moyenne.
  * Remplacer les `NaN` par cette moyenne.
* Créer un nouveau DataFrame : `suspects_corrige` pour stocker les données nettoyées.
* Confirmer qu’il ne reste aucun `NaN`.


### 5. Extraction des valeurs du crime

**Objectif** : Récupérer les trois valeurs du profil du crime.

* Accéder à la première ligne de `crime`.
* Extraire les **valeurs** des 3 loci.
* Les stocker dans `c1`, `c2`, `c3`.
* Les afficher.


### 6. Fonction de distance

**Objectif** : Créer une fonction qui calcule la distance entre un suspect et le crime.

* Définir une fonction `calculer_distance(...)` avec 6 paramètres (Les valeurs des 3 loci des **s**uspects et des 3 loci de la scène de **c**rime).
* Coder la formule pour calculer la distance:
* Retourner la distance.

**Vérifier que** : 
   * La fonction s’exécute.
   * Un test simple retourne une valeur positive.


### 7. Distance pour 150 suspects

**Objectif** : Calculer la distance 3D pour toutes les lignes.

* Extraire les trois colonnes et les convertir en trois tableaux NumPy.
* Créer une liste vide `distances3d`.
* Pour calculer toutes les distances, faire une boucle `for i in range(n)`. Dans la boucle : 
   * Utiliser `calculer_distance(...)` pour calculer les 150 distances:
   * Ajouter chaque distance dans la liste.
* Ajouter la colonne `Distance3D` dans le DataFrame `suspects_corrige`.


### 8. Tri des données (ordre croissant des valeurs des distances)

**Objectif** : Trier les suspects du plus proche au plus éloigné.

* Créer deux listes `noms` et `distances3d` pour stoker les noms des 150 suspects et les 150 distances calculées à l'étape 6.
* Pour chaque position `i` :
  * Trouver la plus petite distance dans les positions restantes.
  * Échanger les distances.
  * Échanger les noms de la même façon.
* Extraire les 10 premiers suspects. Vérifier que les valeurs sont dans l’ordre croissant.


### 9. Graphique Top 10

**Objectif** : Faire un graphique à barres simple du classement.

* Tracer le graphique à barres.
   * **Titre**: "Top 10 des suspects les plus proches (3 loci)"
   * **Étiquette de l'axe x**: il n'y a pas d'étiquette
   * **Étiquette de l'axe y**: "Distance ADN (u.a.)"
   * **Nom du fichier**: `graphique_top10_3loci.png`
* Sauvegarder le graphique.


### 10. Relation entre deux loci et régression

**Objectif** : Comprendre la relation entre deux loci.

* Choisir :
  * `x = Locus1`
  * `y = Locus2`
* Tracer le nuage de points.
   * **Titre**: "Corrélation entre Locus1 et Locus2"
   * **Étiquette de l'axe x**: "Locus2"
   * **Étiquette de l'axe y**: "Locus1"
   * **Nom du fichier** : `graphique_regression_locus1_locus2.png`
* Calculer la droite : `a, b = np.polyfit(x, y, 1)`.
* Tracer la droite avec `plt.plot`.
* Sauvegarder le graphique.


### 11. Export du Top 10

**Objectif** : Créer un fichier `resultats.csv` contenant les informations des 10 suspects les plus probables.

* Créer un nouveau DataFrame pour stocker les 10 suspects.
  ```python
  nouveau_df  = pd.DataFrame({
          "Nom": liste des 10 noms,
          "Distance3D":  liste des distances des 10 noms
      })
   ```
* Exporter le nouveau dataframe dans le fichier .csv avec :
  * `sep=";"`
  * `decimal=","`
  * `index=False`


### 12. Variante 1: 4e locus estimé

**Objectif** : Créer un nouveau locus basé sur une relation linéaire.

* Faire une régression entre `Locus1` et `Locus2`.
* Construire :
  `Locus4_estime = a * Locus1 + b`
* Ajouter la colonne `Distance4D` au dataframe.
* Calculer la distance 4D.
* Afficher les 5 premières lignes pour comparer la colonne `Distance4D` avec la colonne `Distance3D`.


### 13. Variante 2: Bruit expérimental

**Objectif** : Simuler des erreurs de mesure.

* Générer 3 tableaux de bruit.
```python
bruit = np.random.normal(0, 0.01, n)	# n est le nombre total de suspects
```
* Construire trois colonnes bruitées.
* Recalculer les distances bruitées.
* Ajouter la colonne `Distance3D_bruitee`.
* Comparer les distances sans bruit / avec bruit.


### 14. Effet du bruit sur les 3 loci

**Objectif** : Visualiser l'effet du bruit sur un locus

* Tracer le nuage de points pour `Locus1` vs `Locus1_bruite`. 
   * **Titre**: "Effet du bruit expérimental sur les valeurs du Locus1"
   * **Étiquette de l'axe x**: "Locus1"
   * **Étiquette de l'axe y**: "Locus1_bruite"
   * **Nom du fichier** : `graphique_bruit_locus1.png`
* Calculer la droite : `a, b = np.polyfit(x, y, 1)`.
* Tracer la droite avec `plt.plot`.
* Sauvegarder le graphique.


### 15. Conclusion

**Objectif** : Résumer vos résultats en ~ 10-15 lignes.

Idées à inclure :
* Rappel des objectifs du projet incluant l'utilisation des bibliothèques. 
* Qui semble être le suspect principal.
* Écarts entre les distances du Top 10.
* Effet du 4e locus sur l'identification du suspect (distances).
* Effet du bruit sur l'identification du suspect (locus original vs locus bruité).
* Graphiques qui soutiennent votre conclusion et pourquoi.


<!--

### 1. Lecture et exploration des données

1. Lire les fichiers CSV (`;` comme séparateur, `,` pour décimales).  
2. Afficher le nombre de suspects.  
3. Afficher les statistiques de base pour chaque locus.  
4. Remplacer les valeurs manquantes par la moyenne correspondante.  
5. Sauvegarder les données nettoyées dans un fichier nommé `adn_suspects_corrige.csv`.


### 2. Calcul des distances ADN (3 loci = 3D)

1. Extraire et afficher les valeurs des 3 loci sous forme de tableaux NumPy.  
2. Calculer et afficher la **distance euclidienne** entre chaque suspect et le profil du crime.  
3. Créer deux listes :  
   - `noms` (noms des 150 suspects)  
   - `distances` (valeurs des distances)
4. **Trier** les deux listes (boucles imbriquées + échanges entre listes).
5. Afficher le **top 5 des suspects les plus proches**.
6. Créer un **graphique en barres** affichant le **top 10 des suspects** avec barres d’erreur **±5 %**.
	* Titre: "Top 10 des suspects les plus proches (3 loci)"
	* Étiquette de l'axe x: il n'y a pas d'étiquette
	* Étiquette de l'axe y: "Distance ADN (u.a.)"
	* Nom du fichier : `graphique_top10_3loci.png`
7. Créer un **nuage de points** (`scatter`) pour `Locus1` vs `Locus2`. Ajouter une **droite de régression linéaire** avec `np.polyfit()` et `plt.plot()`.
	* Titre: "Corrélation entre Locus1 et Locus2"
	* Étiquette de l'axe x: "Locus2"
	* Étiquette de l'axe y: "Locus1"
	* Nom du fichier : `graphique_regression_locus1_locus2.png`
-->

<!--
```python
for i in range(len(distances) - 1):
    for j in range(i + 1, len(distances)):
        if distances[j] < distances[i]:
            tmp = distances[i]
            distances[i] = distances[j]
            distances[j] = tmp

            tmp_nom = noms[i]
            noms[i] = noms[j]
            noms[j] = tmp_nom
```
-->
<!--
### 3. Exporter les résultats

1. Extraire les 10 premiers suspects triés (noms + distances).
2. Créer un DataFrame `resultats` avec ces données.
3. Exporter dans `resultats.csv`


### 4. Variantes expérimentales

#### a) Ajout d'un 4ᵉ locus estimé par régression linéaire

1. Calculer les coefficients `a` et `b` avec `np.polyfit(Locus1, Locus2, 1)`.
2. Créer une nouvelle colonne : `Locus4_estime = a * Locus1 + b`.
3. Estimer aussi `Locus4` du crime à l'aide des 3 ADN trouvés sur la scène de crime.
4. Recalculer et afficher les **distances à 4 loci (4D)**.

#### b) Bruit expérimental (incertitude de mesure)

Dans cette partie, vous allez simuler l’effet d’erreurs de mesure sur chacun des trois loci ADN.
Ce bruit représente l’incertitude liée aux instruments scientifiques (pipettes, spectromètres, capteurs, etc.).

1. Générer un bruit aléatoire (0.01) **pour chacun des trois loci**
   * Créez **trois tableaux de bruit gaussien** (distribution normale), chacun de **longueur `n`**.
   ```python
   bruit = np.random.normal(0, 0.01, n)
   ```
2. Créer les **trois loci bruités** en ajoutant le bruit à chaque locus original. Ces trois loci bruités sont les valeurs "mesurées avec incertitude".
3. Recalculer toutes les distances 3D bruitées. Pour chaque suspect :
      * utilisez la fonction `calculer_distance()` avec les **versions bruitées des 3 loci**.
      * comparez-les au profil du crime (`c1`, `c2`, `c3`)
   * Stockez les résultats dans une nouvelle liste nommée `distances_bruitees`.
   * Ajoutez ensuite cette liste au DataFrame dans une nouvelle colonne nommée `Distance3D_bruitee`.
4. Comparer les valeurs originales et bruitées
   * Affichez simplement les 5 premières lignes (`.head()`) des données avec les colonnes : `Nom`, `Distance3D` (sans bruit) et `Distance3D_bruitee` (avec bruit). Ce tableau permet de voir si l’incertitude de mesure modifie ou non les distances.
   * Créer un **nuage de points** (`scatter`) pour **un des trois locus et sont équivalent bruité* (à vous de choisir lequel). Utiliser des couleurs différentes pour les deux nuages de points. 
	* Titre: "Effet du bruit expérimental sur Locus1, 2 ou 3" (**précider lequel**)
	* Étiquette de l'axe x: ""Locus (valeur réelle)""
	* Étiquette de l'axe y: "Locus / Locus_bruite"
	* Nom du fichier : `graphique_bruit_locus.png`
-->
<!--
#### b) Bruit expérimental (incertitude de mesure)

1. Simuler un bruit aléatoire gaussien :

   ```python
   bruit = np.random.normal(0, 0.01, len(suspects_corrige))
   ```
2. Créer `Locus1_bruite = Locus1 + bruit`.
3. Créer un **nuage de points** (`scatter`) pour `Locus1` vs `Locus1_bruite`. 
	* Titre: "Effet du bruit expérimental sur les valeurs du Locus1"
	* Étiquette de l'axe x: "Locus1"
	* Étiquette de l'axe y: "Locus1_bruite"
	* Nom du fichier : `graphique_bruit_locus1.png`
4. Recalculer les distances 3D avec `Locus1_bruite`.
5. Refaire un **tri** et afficher le **top 5 bruité**.
-->

<!--
### 5. Rapport scientifique (Conclusion 10-15 lignes)

#### Éléments de la conclusion

* a) **Objectif du projet**
  * Rappeler brièvement la tâche principale.
  * Mentionner les outils utilisés.

* b) **Résultats principaux**
  * Indiquer quel suspect présente la plus petite distance.
  * Donner la valeur de la distance minimale (arrondie à 2 ou 3 décimales).
  * Mentionner les 5 suspects les plus proches (Top 5).

* c) **Analyse des distances**
  * Comparer la plus petite distance avec les autres pour montrer l’écart.
  * Dire si la différence est claire ou si plusieurs suspects ont des valeurs proches.

* d) **Effet des variantes**
  * **4ᵉ locus estimé :** préciser si cela change ou confirme le classement.
  * **Bruit expérimental :** dire si les résultats restent similaires ou non.

* e) **Graphiques**
  * Citer les trois graphiques produits (barres du Top 10, nuage de points avec droite de régression et nuages de points des loci bruités).
  * Indiquer brièvement ce qu’ils permettent de visualiser.
-->
