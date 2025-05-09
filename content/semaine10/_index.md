+++
chapter = true
pre = "<b>Semaine 10.</b>"
title = "Visualisation de données avec matplotlib (bases)"
weight = 100
+++


## Objectif de la leçon

Apprendre à tracer des graphiques simples en 2D à partir de données scientifiques à l’aide de la bibliothèque `matplotlib`.

**Durée :**
50 minutes de théorie + 1 h 50 de pratique

---

## Contexte

Les scientifiques visualisent souvent des données sous forme de graphiques pour interpréter plus facilement des tendances, des anomalies ou des corrélations. Python permet de produire des graphiques de haute qualité grâce à la bibliothèque `matplotlib`.

Dans cette leçon, on apprend à créer des graphiques de base : courbe, points, étiquettes et titres. On travaille dans **Jupyter Notebook** à l’intérieur de l’environnement **Anaconda**.


## Notions abordées

1. **Importation de la bibliothèque**

   ```python
   import matplotlib.pyplot as plt
   ```

2. **Tracé simple d’une courbe**

   ```python
   x = [0, 1, 2, 3, 4]
   y = [0, 1, 4, 9, 16]
   plt.plot(x, y)
   plt.show()
   ```

3. **Ajout de titres et étiquettes**

   ```python
   plt.title("Croissance quadratique")
   plt.xlabel("Temps (s)")
   plt.ylabel("Distance (m)")
   ```

4. **Personnalisation de la courbe**

   * Style de ligne, couleur, marqueur

   ```python
   plt.plot(x, y, color='green', linestyle='--', marker='o')
   ```

5. **Tracer plusieurs courbes sur un même graphique**

   ```python
   plt.plot(x, y, label="objet A")
   plt.plot(x, [i**1.5 for i in x], label="objet B")
   plt.legend()
   ```

6. **Enregistrement du graphique**

   ```python
   plt.savefig("mon_graphique.png")
   ```


## Exercice pratique

**Titre :** Température d’un liquide en fonction du temps
**But :** À partir des données fournies, tracer la courbe de température d’un liquide chauffé pendant 10 minutes.

**Données :**

```python
temps = [0, 2, 4, 6, 8, 10]
temperature = [20, 35,  fifty, 65, 72, 74]  # Erreur volontaire à corriger
```

## Résultat attendu

Un graphique clair et lisible du type :

* Titre : Température du liquide en fonction du temps
* Axe X : Temps (min)
* Axe Y : Température (°C)
* Ligne rouge en pointillés avec des cercles
* Fichier PNG enregistré dans le dossier de travail








