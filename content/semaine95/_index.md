+++
chapter = false
pre = "9.1"
title = " Culture générale (pour Physique mécanique)"
weight = 110
draft = true
+++


## Objectifs

**Avec NumPy**
* Lire des données à partir de fichiers `.txt` et `.csv` avec NumPy.
* Écrire des données dans des fichiers `.txt` et `.csv`.
* Manipuler les données lues sous forme de tableaux NumPy pour faire des calculs scientifiques.  
<!--
[Fichier démo](https://python-a25.netlify.app/blocnotes/demo_fichiers.ipynb)
-->
**Avec Pandas**
* Sélection et parcours des données dans un DataFrame

**Avec SciPy**
* Utiliser le module `scipy.stats` pour calculer une régression linéaire.  
* Extraire la pente, l’ordonnée à l’origine et le coefficient de corrélation.    
* Tracer la droite de régression sur un nuage de points avec `matplotlib`.  

---

# Aller plus loin avec le module NumPy

## Pourquoi lire et écrire des fichiers ?

En sciences, on ne travaille pas toujours avec des données générées dans le programme.
Souvent, les données proviennent :

* d’expériences mesurées,
* de fichiers partagés par d’autres chercheurs,
* de simulations précédentes.

Pour traiter ces données en Python, les bibliothèques `NumPy` et `Pandas` fournissent des fonctions rapides pour **lire** et **écrire** des tableaux numériques.


## 1. Lecture et écriture avec NumPy

### Lecture de fichiers

#### Fichiers texte simples (`.txt`)

Supposons que nous avons un fichier `mesures.txt` contenant des valeurs de température (sans en-tête) :

```
20.1 21.3 19.8 22.0
21.0 22.2 20.5 23.1
```

Lecture en NumPy :

```python
import numpy as np

# Lecture du fichier
donnees = np.loadtxt("mesures.txt")

print(donnees)
print(type(donnees))
```

**Explications :**

* `np.loadtxt()` lit un fichier texte et retourne un tableau NumPy.
* Par défaut, les colonnes sont séparées par des espaces.
* `donnees` est un tableau NumPy 2D (lignes × colonnes).


#### Fichiers CSV (`.csv`)

Un fichier CSV (*Comma-Separated Values*) contient des données tabulaires séparées par des virgules (ou parfois par un autre séparateur).

Si les données sont séparées par des virgules :

```
20.1,21.3,19.8,22.0
21.0,22.2,20.5,23.1
```

On peut lire le fichier avec :

```python
donnees = np.loadtxt("mesures.csv", delimiter=",")
print(donnees)
```

**Remarque :**
`delimiter=","` indique que les colonnes sont séparées par des virgules.


### Option 1 : Utiliser `np.genfromtxt()` (plus robuste)

Si ton fichier contient :

* une **première ligne d’en-têtes**,
* des **valeurs manquantes**,
* ou des **colonnes non numériques** (comme des dates),

alors `np.loadtxt()` échouera.
Dans ce cas, on utilise `np.genfromtxt()`.

Exemple :

```
timestamp,temperature
2021-01-01 00:00:00,20.1
2021-01-01 01:00:00,21.3
2021-01-01 02:00:00,19.8
```

Lecture uniquement de la colonne numérique :

```python
import numpy as np

# Lecture en sautant la première ligne et en lisant la 2e colonne
temperatures = np.genfromtxt("temperatures.csv", delimiter=",", skip_header=1, usecols=1)

# Conversion en Kelvin
temperatures_K = temperatures + 273.15

# Sauvegarde dans un nouveau fichier
np.savetxt("temperatures_kelvin.csv", temperatures_K, delimiter=",", fmt="%.2f")
print("Fichier 'temperatures_kelvin.csv' enregistré.")
```

**Explications :**

* `skip_header=1` : ignore la première ligne contenant les titres.
* `usecols=1` : lit seulement la colonne d’indice 1 (ici, les températures).
* `np.genfromtxt()` : accepte les fichiers mixtes (texte + nombres) et les valeurs manquantes.


#### Exemple avancé avec plusieurs types de données

Si on veut **conserver les dates** et les températures :

```python
data = np.genfromtxt("temperatures.csv", delimiter=",", dtype=None, encoding=None, names=True)

dates = data['timestamp']
temperatures = data['temperature']
temperatures_K = temperatures + 273.15

# Combine dates et températures converties
output = np.column_stack((dates, temperatures_K))
np.savetxt("temperatures_kelvin.csv", output, fmt="%s,%.2f", delimiter=",", header="timestamp,temperature_K", comments="")
```


### 2. Écriture de fichiers

#### Fichiers texte (`.txt` ou `.csv`)

Pour écrire un tableau NumPy dans un fichier texte :

```python
import numpy as np

donnees = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt("resultats.txt", donnees)
```

* Chaque ligne du tableau devient une ligne dans le fichier.
* Par défaut, les valeurs sont séparées par un espace.

Pour un séparateur différent :

```python
np.savetxt("resultats.csv", donnees, delimiter=",")
```

**Format et précision des nombres** :

```python
np.savetxt("resultats.csv", donnees, delimiter=",", fmt="%.2f")
```

* `%.2f` : deux chiffres après la virgule.

---

# Aller plus loin avec le module Pandas

## 1. Sélection de données dans un DataFrame avec `iloc`

* `iloc` permet de **sélectionner des **lignes** ou des **colonnes** selon leur position (index numérique)** plutôt que leur nom.
* C’est pratique quand on ne connaît pas les noms des colonnes ou qu’on veut simplement accéder à une portion du tableau.

	* `df.iloc[0]` → première ligne
	* `df.iloc[:, 1]` → toute la 2ᵉ colonne
	* `df.iloc[2:5, 0:2]` → lignes 2 à 4 et colonnes 0 et 1

**Exemple** :
```python
import pandas as pd

data = {
    "Espèce": ["Truite", "Saumon", "Perchaude", "Brochet"],
    "Longueur_cm": [35, 52, 27, 61],
    "Masse_g": [450, 1500, 320, 2200]
}

poissons = pd.DataFrame(data)

# Affiche la 2e ligne (index 1)
print(poissons.iloc[1])

# Affiche la première colonne
print(poissons.iloc[:, 0])

# Affiche les 2 premières lignes et colonnes
print(poissons.iloc[0:2, 0:2])
```


## 2. Parcourir les lignes d'un DataFrame avec `.iterrows()`

* `.iterrows()` permet de **parcourir chaque ligne d’un DataFrame** dans une boucle `for`. 
* C’est utile pour faire des vérifications ou des calculs ligne par ligne.
* Chaque itération retourne :
	* l’**index de la ligne**
	* la **ligne elle-même** (comme une mini-série Pandas)

**Exemple** : 

```python
import pandas as pd

data = {
    "Échantillon": ["A", "B", "C"],
    "pH": [6.5, 7.2, 8.1]
}
eau = pd.DataFrame(data)

for index, ligne in eau.iterrows():
    if ligne["pH"] > 7:
        print(f"Échantillon {ligne['Échantillon']} : basique")
    else:
        print(f"Échantillon {ligne['Échantillon']} : acide ou neutre")
```

---

# Utiliser le module SciPy pour tracer une droite de régression linéaire

## 1. Contexte scientifique

En sciences expérimentales, on cherche souvent à établir une **relation linéaire** entre deux grandeurs mesurées.
Par exemple :

> Plus la température augmente, plus la solubilité d’un sel dans l’eau augmente.

On peut modéliser cette relation par une **droite** :
[
y = a , x + b
]
où :

* (a) est la **pente** (variation de (y) par unité de (x)),
* (b) est l’**ordonnée à l’origine** (valeur de (y) quand (x = 0)).


## 2. Préparation du code

### Importation des modules

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
```

### Données expérimentales (exemple)

Solubilité d’un sel selon la température :

```python
# Températures (°C)
T = np.array([0, 10, 20, 30, 40, 50])

# Solubilité (g/100g d’eau)
S = np.array([35, 38, 42, 47, 51, 57])
```


## 3. Calcul de la régression linéaire

```python
resultats = stats.linregress(T, S)

print(f"Pente (a) = {resultats.slope:.2f}")
print(f"Ordonnée à l’origine (b) = {resultats.intercept:.2f}")
print(f"Coefficient de corrélation (r) = {resultats.rvalue:.3f}")
print(f"Coefficient de détermination (r²) = {resultats.rvalue**2:.3f}")
```

**Interprétation :**

* Si `r` est proche de **1 ou -1**, la relation est fortement linéaire.
* Si `r²` est proche de **1**, le modèle linéaire explique bien les données.


## 4. Tracer le graphique avec la droite de régression

```python
# Droite calculée : y = a*x + b
S_modele = resultats.slope * T + resultats.intercept

plt.scatter(T, S, color="blue", label="Données expérimentales")
plt.plot(T, S_modele, color="red", label="Régression linéaire")

plt.title("Solubilité d’un sel en fonction de la température")
plt.xlabel("Température (°C)")
plt.ylabel("Solubilité (g/100g d’eau)")
plt.legend()
plt.grid(True)
plt.show()
```

## 5. Résultat attendu

Un graphique montrant :

* des points bleus (mesures expérimentales) ;
* une ligne rouge (modèle linéaire) ;
* la droite de régression qui suit bien la tendance.


## 6. Aller plus loin

Tu peux ajouter l’équation directement sur le graphique :

```python
eq = f"y = {resultats.slope:.2f}x + {resultats.intercept:.2f}\nR² = {resultats.rvalue**2:.3f}"

plt.scatter(T, S, color="blue", label="Données expérimentales")
plt.plot(T, S_modele, color="red", label="Régression linéaire")

plt.text(5, 50, eq, fontsize=10, color="black", bbox=dict(facecolor='white', alpha=0.7))
plt.legend()
plt.show()
```

## 7. Questions de compréhension

1. Que représente la **pente** de la droite dans ce contexte ?
2. Quelle serait la solubilité prédite à 25 °C selon le modèle ?
3. Si (r² = 0.99), que peux-tu conclure sur la qualité du modèle ?
4. Que changerait le signe négatif de la pente dans une autre expérience ?


## 8. Exercice pratique

On a mesuré la **vitesse de réaction chimique** en fonction de la température :

| Température (°C) | Vitesse (mmol/s) |
| ---------------- | ---------------- |
| 10               | 2.1              |
| 20               | 3.2              |
| 30               | 4.8              |
| 40               | 6.3              |
| 50               | 7.5              |

1. Calcule la régression linéaire avec `scipy.stats.linregress()`.
2. Affiche les paramètres `a`, `b` et `r²`.
3. Trace la droite de régression et affiche l’équation sur le graphique.


## 9. À retenir

| Élément                  | Description                       |
| ------------------------ | --------------------------------- |
| `stats.linregress(x, y)` | Calcule la régression linéaire    |
| `.slope`                 | Pente de la droite                |
| `.intercept`             | Ordonnée à l’origine              |
| `.rvalue`                | Coefficient de corrélation        |
| `.rvalue**2`             | Coefficient de détermination (r²) |
| `plt.scatter()`          | Nuage de points                   |
| `plt.plot()`             | Droite de régression              |


<!--

=========================

# Exercices 

## Fichiers de départ à utiliser

1. Cliquez sur les liens pour télécharger les fichiers (`.ipynb`, `.csv` et `.txt`).  
[**Bloc-notes de départ - NumPy**](https://python-a25.netlify.app/blocnotes/exercices_fichiers_np.ipynb)  
**Fichiers de données** :   
	* [**temperatures.csv**](./temperatures.csv) : données météorologiques prévisibles pour Bâle (France).<br>
	* [**etudiants.csv**](./etudiants.csv) : 3 colonnes : `Nom,Âge,Note`.<br>
	* [**solubilite_sel.csv**](./solubilite_sel.csv) : 2 colonnes : `temperature,solubilite`.<br>
	* [**plantes.csv**](./plantes.csv) : 3 colonnes : `Nom,Hauteur_cm,Teneur_eau_%`.<br>
	* [**solutions.csv**](./solutions.csv) : 2 colonnes : `Temp_C,Concentration_mol_L`.<br>
	* [**mineraux.csv**](./mineraux.csv) : 2 colonnes : `Nom,Densité`.<br>
	* [**experience.txt**](./experience.txt). Une fois ouvert, faites un clic-droit et choisir ***Enregistrer sous*** pour enregistrer le fichier dans votre dossier **exercices**.
2. Enregistrez les fichiers dans votre dossier **exercices** de la semaine en cours **(au même endroit que votre fichier .ipynb)**.
3. Ouvrez **Visual Studio Code**.
4. Dans VS Code, recherchez et ouvrez les fichiers `exercices_fichiers_np.ipynb` et `exercices_fichiers_pd.ipynb`.
5. Assurez-vous que le noyau Python (`Kernel`) soit sélectionné.
6. Vous pouvez commencer à faire les exercices.

### Exercice 1 (NumPy)

**Objectif :** À l'aide de NumPy, créez un fichier `vitesses.txt` avec les valeurs suivantes (4 valeurs par ligne, 3 lignes) :
```
5.2 6.1 5.8 6.0
5.5 6.2 6.1 6.3
5.9 6.0 5.7 6.1
```

1. **Créer le tableau de données**
   * Utilisez **une liste de 3 listes** pour stocker les vitesses.
     ``` 
     [
       [5.2, 6.1, 5.8, 6.0],
       [5.5, 6.2, 6.1, 6.3],
       [5.9, 6.0, 5.7, 6.1]
     ]
     ```
   * Utilisez `np.array()` pour créer un tableau 2D contenant les vitesses.

2. **Enregistrer le tableau dans un fichier**
   * Utilisez `np.savetxt("nom_fichier.ext", tableau_numpy, format)` pour écrire le tableau dans un fichier `vitesses.txt`.  
		* Pour appliquer le format des nombres, par exemple pour 2 décimales, remplacez ***format*** par `fmt="%.2f"`.

3. **Lire le fichier avec NumPy**
   * Utilisez `np.loadtxt()` pour lire les données à partir du fichier créé précédemment.
   * Affichez les données lues et vérifiez que le tableau lu a bien la même forme que le tableau original.
   ```
   [[5.2 6.1 5.8 6. ]
    [5.5 6.2 6.1 6.3]
    [5.9 6.  5.7 6.1]]
   ```

4. **Calculer la moyenne de chaque colonne**
   * Utilisez `np.mean(..., axis=0)` pour obtenir les moyennes colonne par colonne.

5. **Enregistrer les moyennes dans un nouveau fichier**
   * Utilisez `np.savetxt()` pour écrire les moyennes dans un fichier nommé `moyennes.txt`.
   * Vérifiez le contenu du fichier après écriture. Vous devriez voir ceci : 
   ```
   5.53
   6.10
   5.87
   6.13
   ```

**Résultats** :
```
Moyennes enregistrées : [5.53333333 6.1        5.86666667 6.13333333]
```

### Exercice 2 (NumPy)

**Objectif :** lire un fichier CSV (`temperatures.csv`), manipuler les données et sauvegarder les résultats.

1. **Lire le fichier CSV `temperatures.csv`**
   * Vérifiez le séparateur utilisé dans le fichier (généralement `,`) et utilisez `delimiter=","`, `skip_heade=1` et `usecols=1` dans `np.genfromtxt()`.

2. **Conversion en Kelvin**
   * Pour convertir des degrés Celsius en Kelvin, ajoutez 273.15 à toutes les valeurs du tableau.
     * **Astuces** : NumPy permet d’effectuer cette opération sur tout le tableau en une seule instruction (sans boucle).

3. **Enregistrer les données converties**
   * Utilisez `np.savetxt()` avec `delimiter=","` pour créer un **nouveau** fichier CSV (ex: `temperature_K.csv`).
   * Choisissez un format de nombres lisible (`fmt="%.2f"` par exemple).
   * Vérifier le contenu du fichier `temperature_K.csv` (données en K). Vous devriez voir ceci (partiel):
   
   ![Températures en K](./tempK_csv.png?width=15vw&height=25vw)

**Résultats** :
```
Températures en °C :
[2.31 2.37 2.43 ... 1.92 1.96 1.68]

Températures converties en K :
[275.46 275.52 275.58 ... 275.07 275.11 274.83]
```
-->













