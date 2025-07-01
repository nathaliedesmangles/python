+++
title = "Activité 5 – Traitement d’une série de mesures et moyenne mobile"
weight = 51
+++

## Objectifs d’apprentissage

* Manipuler des **listes** en Python
* Écrire une fonction pour calculer une **moyenne mobile**
* Visualiser l’effet du lissage sur une série de données
* Renforcer les notions de boucles, indices et opérations sur les listes

---

## Contexte scientifique

En laboratoire, on mesure la concentration d’un produit chimique toutes les 2 minutes pendant une expérience de 20 minutes. Les mesures présentent des fluctuations dues à des imprécisions expérimentales. Pour lisser ces données et observer les tendances, on applique une **moyenne mobile** sur les résultats.

## Données de départ

Voici les mesures de concentration (en mg/L) prises toutes les 2 minutes :

```python
mesures = [10.2, 9.8, 10.5, 10.0, 9.7, 10.1, 10.3, 10.0, 9.9, 10.2]
```

## Tâches à réaliser

### Étape 1 – Affichage simple des données

* Afficher chaque mesure avec son indice et le temps correspondant (temps = indice × 2 minutes).
* Exemple de sortie :

  ```
  Temps : 0 min — Mesure : 10.2 mg/L
  Temps : 2 min — Mesure : 9.8 mg/L
  ...
  ```

### Étape 2 – Fonction de moyenne mobile

* Écrire une fonction `moyenne_mobile(liste, k)` qui retourne une nouvelle liste contenant la moyenne mobile sur **k valeurs consécutives**.
* Exemple : avec k = 3, la moyenne mobile des trois premières valeurs est `(10.2 + 9.8 + 10.5)/3 = 10.17`.

```python
def moyenne_mobile(liste, k):
    resultats = []
    for i in range(len(liste) - k + 1):
        moyenne = sum(liste[i:i+k]) / k
        resultats.append(moyenne)
    return resultats
```

### Étape 3 – Comparaison avant/après

* Afficher les valeurs originales et les valeurs lissées (par exemple avec k = 3) côte à côte.

### Étape 4 – (Optionnel) Visualisation avec matplotlib

* Tracer deux courbes :

  * la courbe des mesures originales
  * la courbe des mesures lissées
* L’objectif est de bien voir l’effet du lissage.

```python
import matplotlib.pyplot as plt

temps = [i * 2 for i in range(len(mesures))]
mesures_lissees = moyenne_mobile(mesures, 3)
temps_lisse = [i * 2 + 2 for i in range(len(mesures_lissees))]  # Décalage pour centrage

plt.plot(temps, mesures, label="Mesures originales")
plt.plot(temps_lisse, mesures_lissees, label="Moyenne mobile (k=3)")
plt.xlabel("Temps (min)")
plt.ylabel("Concentration (mg/L)")
plt.legend()
plt.title("Mesures expérimentales avec lissage")
plt.grid(True)
plt.show()
```

## Critères de réussite

* La fonction `moyenne_mobile` est fonctionnelle et générale (k variable)
* Les boucles et les indices sont bien utilisés
* L’affichage est clair et informatif
* (Optionnel) Le graphique est lisible et correctement légendé

