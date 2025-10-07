+++
title = "Graphiques Matplotlib - Codes de couleurs"
weight = 29.2
+++

## Les couleurs et Matplotlib

Matplotlib permet d’utiliser des **abréviations d’une seule lettre** pour les couleurs les plus courantes dans les tracés (`plot`, `scatter`, etc.). Voici la liste complète :

| Lettre | Couleur en anglais | Couleur affichée     |
| :----: | :----------------- | :------------------- |
|   `b`  | blue               | 🔵 bleu              |
|   `g`  | green              | 🟢 vert              |
|   `r`  | red                | 🔴 rouge             |
|   `c`  | cyan               | 🟦 cyan (bleu clair) |
|   `m`  | magenta            | 🟣 magenta / fuchsia |
|   `y`  | yellow             | 🟡 jaune             |
|   `k`  | black              | ⚫ noir               |
|   `w`  | white              | ⚪ blanc              |


## Exemple d’utilisation

```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3]
y = [0, 1, 4, 9]

plt.plot(x, y, 'r--')  # ligne rouge en pointillés
plt.show()
```

Ici :

* `'r'` = **red**
* `'--'` = **ligne pointillée**


## À retenir

* Ces lettres ne couvrent que les **couleurs de base**.
* Vous pouvez aussi utiliser :
	* des **noms complets** : `'orange'`, `'lime'`, `'navy'`, `'purple'`…
	* ou des **codes hexadécimaux** : `'#FF5733'`
	* ou même des **valeurs RVB** (Rouge Vert Bleu): `(0.1, 0.5, 0.8)` (entre 0 et 1)
* Il existe plusieurs sites web qui donnent les noms, les codes hexadécimaux et les valeurs RVB. En voici un:
	* [Noms des couleurs](https://www.w3schools.com/colors/colors_names.asp)
	* [Codes hexadécimaux](https://www.w3schools.com/colors/colors_hexadecimal.asp)
	* [Valeurs RVB](https://www.w3schools.com/colors/colors_rgb.asp)
