+++
title = "Faire croiser les axes à l’origine (0,0)"
weight = 29.1
+++


## 1. Rappel : les axes par défaut

Quand tu fais un graphique avec Matplotlib, les axes sont placés **autour** du graphique, pas au centre.

Exemple :

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = x**2

plt.plot(x, y)
plt.show()
```

**Résultat** :
Les axes sont en bas et à gauche, et ils **ne passent pas par (0,0)**.

![Axes par défaut](./axes_defaut.png?width=30vw)

## 2. Les *spines*, c’est quoi ?

Les *spines* sont les **lignes qui forment les axes du graphique** :

* `'left'` : axe vertical gauche
* `'bottom'` : axe horizontal bas
* `'right'` : axe vertical droit
* `'top'` : axe horizontal haut

On peut les **déplacer**, **colorer** ou **masquer** facilement.



## 3. Faire croiser les axes à (0,0)

Voici le code le plus simple :

```python
import matplotlib.pyplot as plt
import numpy as np

# Données simples
x = np.linspace(-5, 5, 100)
y = x**2

# Création de la figure et du repère
fig, ax = plt.subplots()
ax.plot(x, y)

# Déplacer les axes au centre
ax.spines['left'].set_position('zero')     # axe vertical à x = 0
ax.spines['bottom'].set_position('zero')   # axe horizontal à y = 0

# Masquer les spines inutiles
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
```

**Résultat attendu :**
* Les axes x et y se croisent à l’origine.
* C’est souvent ce qu’on veut en mathématiques ou en physique.

![Axes décalés](./axes_decales.png?width=30vw)

{{% notice style="cyan" title="Explications sur `fig, ax = plt.subplots()`" groupid="notice-toggle" expanded="false" %}}

### Qu'est-ce que fig et ax ?

| Élément | Rôle                                 |
| ------- | ------------------------------------ |
| `fig`   | la **figure** = la feuille blanche   |
| `ax`    | les **axes** = le repère où on trace |

```python
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```


### Pourquoi pas juste `plt.plot()` ?

* `plt.plot()` → rapide, automatique, peu de contrôle.
* `plt.subplots()` → plus précis : on peut déplacer les axes, ajouter des flèches, etc.

{{% /notice %}}

## À retenir

| Action                          | Commande                                                                       |
| ------------------------------- | ------------------------------------------------------------------------------ |
| Déplacer l’axe vertical à x=0   | `ax.spines['left'].set_position('zero')`                                       |
| Déplacer l’axe horizontal à y=0 | `ax.spines['bottom'].set_position('zero')`                                     |
| Cacher les spines inutiles      | `ax.spines['top'].set_color('none')` et `ax.spines['right'].set_color('none')` |

