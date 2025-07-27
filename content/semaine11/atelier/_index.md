+++
title = "Activité 11"
weight = 111
draft = true
+++


## Objectif pédagogique

Apprendre à lire et traiter un fichier contenant des données expérimentales, effectuer des calculs simples, et produire un résumé statistique à l’aide de Python.

---

## Exercice 1 : Analyse de données de température

**Contexte** : Un technicien a mesuré la température d’un liquide toutes les 5 minutes pendant 30 minutes. Les données sont enregistrées dans un fichier CSV.

**Étapes :**

1. **Télécharger et lire le fichier `donnees_temp.csv`** fourni par l’enseignant.
2. **Afficher les données ligne par ligne**, avec mise en forme : « À t = 10 min, T = 25.8 °C »
3. **Calculer la température moyenne à partir des données lues.**
4. **Écrire un nouveau fichier `analyse.csv`** qui contient :

   * Une colonne « temps »
   * Une colonne « température »
   * Une colonne « écart à la moyenne »
5. **Bonus** : Tracer les données avec matplotlib (si le temps le permet).


**Éléments d’évaluation formative (en équipe)**

* Capacité à extraire et utiliser les données du fichier
* Respect des bonnes pratiques (indentation, noms de variables, commentaires)
* Clarté du fichier CSV généré
* Travail collaboratif dans la répartition des tâches

---

## Exercice 2 : Impact de la température sur le pH de l’eau

**Contexte :**
Une équipe d’étudiants en chimie a réalisé une série de mesures du pH d’un échantillon d’eau à différentes températures, à raison de 3 mesures par température. Les données ont été consignées dans un fichier CSV.

**Contenu du fichier `ph_mesures.csv` :**

```
Température (°C),Mesure1,Mesure2,Mesure3
10,7.12,7.10,7.13
15,7.05,7.06,7.04
20,6.98,6.97,6.99
25,6.92,6.91,6.93
30,6.85,6.86,6.87
```

## Consignes

1. **Lecture du fichier :**

   * Utiliser Python (avec `csv` ou `pandas`) pour lire les données.

2. **Traitement des données :**

   * Calculer la moyenne du pH pour chaque température.
   * Conserver les résultats dans une nouvelle structure de données (liste ou dictionnaire).

3. **Analyse simple :**

   * Identifier s’il y a une tendance du pH en fonction de la température.
   * Ajouter une colonne "Moyenne\_pH" aux données.

4. **Affichage des résultats :**

   * Afficher les résultats dans une table lisible.
   * Écrire les résultats dans un nouveau fichier CSV : `ph_moyennes.csv`.

5. **Extension (facultative) :**

   * Tracer un graphique température vs moyenne du pH à l’aide de `matplotlib`.

**Livrable attendu :**
Un script Python complet et bien commenté, ainsi qu’un fichier CSV de sortie contenant les moyennes.

**Discussion en équipe (20 minutes) :**
En petits groupes (2-3), comparer les résultats, discuter de la fiabilité des mesures et de l’impact de la température sur le pH de l’eau. Chaque équipe propose une conclusion en 2-3 phrases à partager au groupe.



