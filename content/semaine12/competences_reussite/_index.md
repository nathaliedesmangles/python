+++
title = "Notions nécessaires pour réussir le projet"
weight = 112.3
+++

Voici une liste des **notions, fonctions et méthodes** que vous devez avoir **apprises avant de faire le projet ADN**. Elle couvre la programmation de base, les bibliothèques scientifiques et les compétences analytiques spécifiques au projet.



### A. Programmation de base en Python

| Thème                           | Notions, fonctions, méthodes                                             |
| ------------------------------- | ------------------------------------------------------------------------ |
| **Variables & types**           | `int`, `float`, `str`, `bool`, `list`, `dict`                            |
| **Structures de contrôle**      | `if`, `elif`, `else`, `for`, `while`, `break`, `continue`                |
| **Fonctions personnalisées**    | `def`, `return`, paramètres et portée locale                             |
| **Manipulation de chaînes**     | `str.lower()`, `str.replace()`, `in`, `==`, slicing, boucles sur chaînes |
| **Listes & tableaux imbriqués** | accès à un élément, boucles imbriquées, conditions dans les listes       |


### B. Manipulation de données avec Pandas

| Thème                      | Fonctions / méthodes                    |
| -------------------------- | --------------------------------------- |
| **Créer un DataFrame**     | `pd.DataFrame(...)`                     |
| **Lire un fichier CSV**    | `pd.read_csv(...)`                      |
| **Parcourir un DataFrame** | `.iterrows()`, indexation par colonne   |
| **Calculs sur colonnes**   | `.mean()`, `.round()`, `.sort_values()` |
| **Créer des colonnes**     | `df["nouvelle_colonne"] = ...`          |


### C. NumPy pour le calcul scientifique

| Thème                        | Fonctions / méthodes                                  |
| ---------------------------- | ----------------------------------------------------- |
| **Créer des tableaux NumPy** | `np.array(...)`                                       |
| **Fonctions mathématiques**  | `np.mean()`, `np.std()`, `np.full()`, `np.linspace()` |
| **Opérations vectorielles**  | tableau ± valeur, `array1 + array2`, etc.             |


### D. Visualisation avec Matplotlib

| Thème                               | Fonctions / méthodes                                                |
| ----------------------------------- | ------------------------------------------------------------------- |
| **Graphique à barres**              | `plt.bar(...)`, `plt.xticks(...)`, `plt.title(...)`, `plt.legend()` |
| **Graphique avec barres d’erreur**  | `plt.errorbar(x, y, xerr, yerr)`                                    |
| **Tracer une droite de régression** | `plt.plot(...)`, affichage de l’équation                            |
| **Affichage**                       | `plt.show()`, `plt.grid(True)`, `plt.tight_layout()`                |


### E. Statistiques et régression avec SciPy

| Thème                          | Fonctions / méthodes                                  |
| ------------------------------ | ----------------------------------------------------- |
| **Régression linéaire simple** | `from scipy.stats import linregress`                  |
| **Extraire les résultats**     | `slope`, `intercept`, `r_value`, `std_err`, `p_value` |
| **Évaluer la concordance**     | `r_value ** 2` pour le coefficient de détermination   |


### F. Programmation lettrée et structuration du bloc-notes

| Thème                     | Pratiques attendues                                          |
| ------------------------- | ------------------------------------------------------------ |
| **Markdown**              | Titres (`#`), sous-titres, explication des sections          |
| **Séparation claire**     | Théorie, code, interprétation                                |
| **Commentaires**          | `#` dans le code + commentaires en Markdown pour chaque bloc |
| **Exécution sans erreur** | Toutes les cellules exécutées du début à la fin sans blocage |

---

## Résumé des compétences transversales

* Analyser un problème scientifique
* Choisir les bons outils (librairie, type de graphique)
* Représenter des incertitudes et des relations mathématiques
* Interpréter les résultats dans un contexte réaliste
* Produire un rapport structuré, scientifique et rigoureux
