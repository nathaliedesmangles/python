+++
title = "Résumé du projet ADN du coupable"
weight = 121
draft = true
+++


Le projet *ADN du coupable* consiste à utiliser la programmation Python pour identifier quel suspect, parmi **150 profils ADN**, correspond le mieux au **profil ADN trouvé sur une scène de crime**.

Ce projet permet de mettre en pratique **toutes les compétences vues depuis le début de la session** :

* lecture de fichiers CSV avec *pandas*
* manipulation de données (moyennes, nettoyage, gestion de NaN)
* calculs scientifiques avec *numpy*
* création de fonctions
* utilisation de boucles
* filtrage logique
* visualisation de données avec *matplotlib*
* régression linéaire avec *numpy.polyfit*

Le projet s’effectue **en équipe de 2 ou 3**, sur environ **3 semaines**.



## Contexte scientifique

Chaque individu possède un profil ADN caractérisé ici par **3 valeurs numériques appelées “loci”** :

* `Locus1`
* `Locus2`
* `Locus3`

Ces valeurs varient entre **0,40 et 0,70**.
Plus les loci d’un suspect sont *proches* de ceux du crime, plus il est probable que ce soit le même individu.



## Objectif principal

**Trouver quel suspect a le profil ADN le plus proche** du profil du crime.

Pour cela, vous devez :

1. Lire les fichiers CSV des suspects et du crime ;
2. Nettoyer les données (remplacer les valeurs manquantes) ;
3. Calculer une **distance euclidienne 3D** pour chaque suspect ;
4. Classer les 150 distances du plus petit au plus grand ;
5. Identifier le **Top 10** des suspects les plus proches ;
6. Visualiser les résultats dans des graphiques.



## Distance euclidienne

La distance permet de quantifier la similarité entre deux profils ADN.

Formule utilisée :
```math
$$
	d = \sqrt{(s_1 - c_1)^2 + (s_2 - c_2)^2 + (s_3 - c_3)^2}  
$$
```
 où chaque $(s_i\)$ représente la valeur du locus d'un suspect et $(c_i\)$ représente la valeur d’un même locus chez un individu dont le profil ADN a été trouvé sur la scène de crime.

* Petite distance → suspect très proche du profil du crime
* Grande distance → suspect moins probable

<br>

## Analyses et graphiques à produire

Vous devrez produire :

### 1. **Barres du Top 10**

Un graphique qui montre clairement les 10 distances les plus faibles.

### 2. **Nuage de points (scatter)**

Comparer deux loci (ex. Locus1 vs Locus2).

### 3. **Droite de régression linéaire**

Estimer une relation entre deux loci avec :

```python
a, b = np.polyfit(x, y, 1)
```



## Variantes du projet

### Variante 1 : **Estimation d’un 4e locus par modélisation**

À partir d’une relation linéaire entre deux loci, les étudiants créent :

* un **Locus4_estime**
* une **distance 4D** optionnelle
  Cela montre le rôle de la modélisation scientifique.

### Variante 2 : **Simulation d’erreurs de mesure (bruit)**

Ajouter un bruit gaussien sur les données :

```python
np.random.normal(0, 0.01, taille)
```

Puis observer si le classement change.
Cela permet de discuter de la **robustesse** du modèle.

### Variante 3 : **Export du Top 10**

Créer un fichier `resultats.csv` contenant les 10 suspects les plus probables.



## Conclusion à rédiger

Dans la dernière section, les étudiants doivent expliquer :

* Quel suspect est le plus probable, et pourquoi ;
* Quelle est la distance minimale observée ;
* Ce que montrent les graphiques ;
* Si le bruit ou le Locus4 ont modifié le classement ;
* Si le résultat est stable ou sensible aux variations.



## Résultat final attendu

Un dossier contenant :

* un notebook `.ipynb` complet (code + graphiques + analyses),
* un fichier `resultats.csv`,
* une conclusion clairement rédigée.

