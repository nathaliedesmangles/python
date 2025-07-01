+++
title = ""
weight = 41
+++



Une expérience consiste à mesurer la température (°C) d’un liquide chaque minute pendant 10 minutes.

Voici les données recueillies :
`[20.1, 21.3, 22.0, 22.5, 23.1, 23.7, 24.0, 24.2, 24.5, 24.7]`

### Tâches demandées

1. **Afficher chaque température** avec la minute correspondante.

   * Exemple : `Minute 1 : 20.1 °C`

2. **Calculer la variation moyenne** de température par minute.

3. **Détecter les anomalies** : afficher un message si une variation dépasse 1 °C par minute.

4. (Optionnel, si le temps le permet) **Comparer avec un seuil théorique** (24.5 °C) et indiquer à quel moment il est dépassé.

### Exemple de sortie partielle

```
Minute 4 : 22.5 °C
Variation depuis minute 3 : +0.5 °C
Minute 5 : 23.1 °C
Variation depuis minute 4 : +0.6 °C
...
Seuil de 24.5 °C dépassé à la minute 10.
```

## Discussion en équipe (10 minutes)

* Pourquoi une boucle est-elle utile dans chacun de ces cas?
* Quelle bou
cle est préférable dans quel contexte (`for` vs `while`)?
* Quelle stratégie utiliser pour identifier une anomalie dans une séquence?