+++

chapter = true

pre = "<b>11.</b>"

title = " Les graphiques avancés et la regression linéaire"

weight = 111

draft = false

+++





* Tracer un graphique à barres

* Ajouter des barres d’erreur

* Tracer une droite de régression

* Interpréter la pente, l’ordonnée à l’origine et le coefficient de détermination R²

* Établir une relation entre deux données

* Interpréter les résultats pour répondre à une question scientifique



---



## Importer la bibliothèque



```python
import matplotlib.pyplot as plt
```





## Graphique à barres



**Exemple de base :**



```python
noms = ["A", "B", "C"]
valeurs = [4, 7, 5]

plt.bar(noms, valeurs)
plt.title("Résultats")
plt.xticks(rotation=0)
plt.legend(["Score"])
plt.show()
```



| Fonction        | Rôle                                |

| --------------- | ----------------------------------- |

| `plt.bar(x, y)` | Crée des barres                     |

| `plt.xticks()`  | Contrôle les étiquettes sur l’axe x |

| `plt.title()`   | Ajoute un titre                     |

| `plt.legend()`  | Affiche une légende                 |





## Graphique avec barres d’erreur



**Exemple :**



```python
x = [1, 2, 3]
y = [10, 12, 9]
erreurs = [0.5, 0.3, 0.6]

plt.errorbar(x, y, yerr=erreurs, fmt="o", label="Mesures")
plt.title("Mesures avec incertitude")
plt.legend()
plt.grid(True)
plt.show()
```



| Argument  | Signification                    |

| --------- | -------------------------------- |

| `yerr`    | barres d’erreur verticales       |

| `xerr`    | (optionnel) erreurs horizontales |

| `fmt="o"` | style des points                 |



---



## Tracer une droite de régression



**Rappel** : L'équation d'une droite est `y = a·x + b`



**Exemple :**



```python
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([2.1, 4.2, 6.1, 8.0])

# Droite de régression : y = a·x + b

a, b = np.polyfit(x, y, 1)
y_reg = a * x + b

plt.plot(x, y, "o", label="Données")
plt.plot(x, y_reg, "-", label=f"y = {a:.2f}x + {b:.2f}")
plt.legend()
plt.grid(True)
plt.show()
```





## Affichage propre



| Fonction             | Effet                                            |

| -------------------- | ------------------------------------------------ |

| `plt.show()`         | Affiche le graphique                             |

| `plt.grid(True)`     | Ajoute une grille                                |

| `plt.tight_layout()` | Ajuste l'espacement pour éviter le chevauchement |





## Résumé minimal



| Tâche                | Fonction                           |

| -------------------- | ---------------------------------- |

| Graphique à barres   | `plt.bar()`                        |

| Barres d’erreur      | `plt.errorbar()`                   |

| Titre                | `plt.title()`                      |

| Légende              | `plt.legend()`                     |

| Grille               | `plt.grid(True)`                   |

| Droite de régression | `np.polyfit()`, `plt.plot()`       |

| Affichage final      | `plt.show()`, `plt.tight_layout()` |





---

## Exercices à faire avant le cours



[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_graphes_barres_reg.ipynb)





### Exercice 1 – Sulfate de cuivre



1. Températures : `[0, 10, 20, 30, 40, 50]`

2. Solubilité (g/100g eau) : `[23, 27, 32, 37, 44, 51]`

3. Calcule la régression linéaire.

4. Affiche les résultats et une conclusion scientifique.





### Exercice 2 – Comparaison de deux sels



1. Sel A :



   * Température : `[0, 20, 40, 60]`

   * Solubilité : `[15, 21, 30, 38]`



2. Sel B :



   * Température : `[0, 20, 40, 60]`

   * Solubilité : `[30, 32, 33, 33.5]`



3. Pour chaque sel :



   * Effectue la régression

   * Affiche pente, intercept, R²

   * Déduis quel sel est le plus influencé par la température





### Exercice 3 – Prévision



1. Utilise les données de l’exemple principal

2. Calcule la solubilité prévue à 60 °C avec la formule :



```python
valeur_predite = resultat.slope * 60 + resultat.intercept
print(f"Solubilité prévue à 60 °C : {valeur_predite:.2f} g/100g d’eau")
```



### Exercice 1 – Graphique à barres



**Énoncé :**

Affiche un graphique à barres pour les éléments `"Fer"`, `"Cuivre"`, `"Zinc"` avec les valeurs `[12, 7, 5]`.



**Solution :**



```python
elements = ["Fer", "Cuivre", "Zinc"]
quantites = [12, 7, 5]

plt.bar(elements, quantites)
plt.title("Concentration des métaux")
plt.legend(["mg/L"])
plt.show()
```





### Exercice 2 – Barres d’erreur



**Énoncé :**

Pour `x = [1, 2, 3]`, `y = [5.1, 5.0, 5.2]`, `yerr = [0.1, 0.2, 0.15]`, trace les points avec barres d’erreur.



**Solution :**



```python
x = [1, 2, 3]
y = [5.1, 5.0, 5.2]

yerr = [0.1, 0.2, 0.15]

plt.errorbar(x, y, yerr=yerr, fmt="o", label="Mesures")
plt.title("Tension mesurée")
plt.legend()
plt.grid(True)
plt.show()
```





### Exercice 3 – Droite de régression



**Énoncé :**

Pour `x = [0, 1, 2, 3]`, `y = [1, 2.1, 3.9, 6.0]`, trace les points et la droite de régression, avec son équation dans la légende.



**Solution :**



```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3])
y = np.array([1, 2.1, 3.9, 6.0])

a, b = np.polyfit(x, y, 1)

plt.plot(x, y, "o", label="Points")
plt.plot(x, a*x + b, "-", label=f"y = {a:.2f}x + {b:.2f}")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
```

> **RAPPEL**: Le **troisième et dernier examen** (20%) et prévu à la **semaine 15**.

1. Lire la description du [Projet final](../semaine12/)
2. Prendre connaissance de la [Grille de correction](../semaine12/grille/)
3. S'approprier des [Notions à savoir pour réussir le projet](../semaine12/competences_reussite/)