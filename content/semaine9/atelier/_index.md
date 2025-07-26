+++
title = "Activité 9"
weight = 109
draft = false
+++
 

## Objectifs

* Création de tableaux à 1D et 2D (`numpy`).
* Calcul de moyennes et d’écarts types.
* Gestion de données manquantes (`np.nan`).
* Comparaison entre conditions expérimentales.

---

## Exercice : Analyse d’une expérience sur l’effet de la lumière sur la croissance des plantes

Une équipe de recherche a mesuré la hauteur (en cm) de jeunes plantes après 10 jours de croissance dans trois conditions lumineuses différentes :

* lumière naturelle,
* lumière LED blanche,
* lumière LED rouge.

Pour chaque condition, 5 plantes ont été mesurées. Certaines données sont manquantes, car une ou deux plantes n’ont pas survécu. Les données brutes sont les suivantes :

| Condition   | Plante 1 | Plante 2 | Plante 3 | Plante 4 | Plante 5 |
| ----------- | -------- | -------- | -------- | -------- | -------- |
| Naturelle   | 12.5     | 13.1     | 12.9     | 13.0     | 12.8     |
| LED blanche | 11.2     | 11.6     | np.nan   | 11.5     | 11.3     |
| LED rouge   | 10.4     | 10.1     | 10.2     | np.nan   | np.nan   |


Écris un programme Python qui :

1. **Représente les données sous forme d’un tableau 2D** (à l’aide de `numpy`).
2. **Calcule la moyenne et l’écart-type** de la hauteur des plantes pour chaque condition, en **ignorant les valeurs manquantes**.
3. **Compare les hauteurs moyennes** entre les conditions (affiche par exemple la condition ayant la croissance moyenne la plus élevée).
4. **Affiche un résumé clair**, par exemple :

   ```
   Moyenne (Naturelle) = 12.86 cm, écart-type = 0.22 cm
   Moyenne (LED blanche) = ...
   ...
   Condition avec la plus grande croissance moyenne : Naturelle
   ```

---

### Aide

* Utilise `numpy.array()` pour construire le tableau.
* Utilise `np.nanmean()` et `np.nanstd()` pour les calculs.
* Utilise des f-strings pour formater les sorties.
* Tu peux créer une liste `conditions = ["Naturelle", "LED blanche", "LED rouge"]` pour faciliter l'affichage.