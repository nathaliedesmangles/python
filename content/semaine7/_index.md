+++
chapter = true
pre = "7."
title = " Dictionnaires"
weight = 107
draft = false
+++
 

## Objectifs

* Créer un dictionnaire simple pour représenter des données associatives (ex. : atome → masse atomique)
* Manipuler des données dans un dictionnaire (accès, ajout, modification, parcours).
* Lire un fichier csv contenant des données expérimentales
* Explorer les données.
* Filtrer les résultats pour une donnée ciblée.
* Comparer des valeurs selon une donnée.

## Fichier .ipynb pour la démonstration en classe

[Fichier utilisé pour la démonstration](https://python-a25.netlify.app/blocnotes/demo_dictionnaires.ipynb)

---

{{% notice style="accent" title="Apprendre par la pratique" %}}
- **Faites les exercices** en vous aidant des notes de cours ci-dessous.
- Certains seront fait en classe à titre de démonstration.
- Les solutions seront disponibles à la fin de la semaine prochaine.
{{% /notice %}}

---

# Exercices

## Objectifs

* **Créer / accéder / modifier / supprimer** des éléments,
* **Parcourir** un dictionnaire,
* **Transformer en listes** (`keys()`, `values()`, `items()`),
* **Faire des calculs** à partir des valeurs.

## Fichiers de départ à utiliser

1. Cliquez sur le lien pour télécharger le fichier `.ipynb`:
[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_dictionnaires.ipynb)
2. Enregistrez le fichier dans votre dossier **exercices** de la semaine en cours.
3. Ouvrez **Visual Studio Code**.
4. Dans VS Code, recherchez et ouvrez le fichier `exercices_dictionnaires.ipynb`
5. Assurez-vous que le noyau Python (`Kernel`) soit sélectionné.
6. Vous pouvez commencer à faire les exercices.


## Exercice 1 : Créer un dictionnaire

* Créer un dictionnaire vide nommé `cubes`.
* En utilisant une boucle `for`, ajouter les entiers de 1 à 5 comme **clés**, et leur cube comme **valeurs**.
* Afficher ensuite le dictionnaire.

**Résultat attendu** :
```
Dictionnaire des cubes : {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
```


## Exercice 2 : Extraire clés et valeurs

À partir du dictionnaire `cubes` créé à l’exercice 1 :

1. Créer une liste `cles` contenant toutes les clés.
2. Créer une liste `valeurs` contenant toutes les valeurs.
3. Afficher les deux listes.

*Indice* : utiliser `list(mon_dict.keys())` et `list(mon_dict.values())`.

**Résultat attendu** :
```
Clés : [1, 2, 3, 4, 5]
Valeurs : [1, 8, 27, 64, 125]
```


## Exercice 3 : Parcourir `items()`

Toujours avec le dictionnaire `cubes`, utiliser une boucle `for` sur `cubes.items()` pour afficher chaque clé et sa valeur sous la forme :

**Résultat attendu** :
```
Le cube de 1 est 1
Le cube de 2 est 8
Le cube de 3 est 27
Le cube de 4 est 64
Le cube de 5 est 125
```


### Exercice 4 : Modifier et supprimer

1. Ajouter une nouvelle paire `6: 216` dans le dictionnaire.
2. Modifier la valeur associée à la clé `3` pour qu’elle devienne `30` (au lieu de `27`).
3. Supprimer la clé `1` du dictionnaire.
4. Afficher le dictionnaire final.


**Résultat attendu** :
```
Dictionnaire final : {2: 8, 3: 30, 4: 64, 5: 125, 6: 216}
```

---

# Cours

## Qu’est-ce qu’un dictionnaire ?

* **Définition** : un dictionnaire est une structure de données qui associe une **clé** à une **valeur**.
* **Image mentale** : c’est comme un **vrai dictionnaire** de langue → chaque mot (clé) a une définition (valeur).
* **Syntaxe** :

```python
mon_dico = {clé1: valeur1, clé2: valeur2, ...}
```

## Créer un dictionnaire

**Exemple 1** : concentrations de trois échantillons

```python
concentrations = {
    1: 0.10,   # échantillon 1
    2: 0.15,   # échantillon 2
    3: 0.20    # échantillon 3
}
```

> Ici, les clés sont des **entiers** (numéro de l'échantillon), et les valeurs sont des nombres à virgule flottante (concentrations).

**Exemple 2** : capitales des pays

```python
capitales = {
    "Canada": "Ottawa",
    "France": "Marseille",	# Erreur volontaire
    "Japon": "Tokyo"
}
```

> Ici, les clés sont aussi des **chaînes de caractères** (pays), et les valeurs sont des chaînes (capitales).

### Types **autorisés** comme clés 

* **Chaînes de caractères** : "nom", "programme", etc.
* **Nombres** : 1, 2.5, -3
* **Booléens** : True, False
* **Tuples immuables** (ne contenant que des éléments immuables) : (1, 2), ("x", "y")

{{% notice style="accent"  title="Sachez que..." %}}
En pratique, on utilise **surtout des chaînes de caractères pour la lisibilité**, mais Python permet cette flexibilité.
{{% /notice %}}

### Types **interdits** comme clés

* Listes (car modifiables)
* Dictionnaires (car modifiables)
* Ensembles (set) (car modifiables)


## Accéder à une valeur

On utilise la clé entre crochets `[ ]`.

```python
print(capitales["Canada"])   # Ottawa
```

```
Ottawa
```

{{% notice style="accent"  title=Attention %}}
Si la clé n’existe pas, Python déclenche une erreur `KeyError`.
```python
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[3], line 1
----> 1 print(capitales["USA"])

KeyError: 'USA'
```
{{% /notice %}}

Pour éviter ça, on peut utiliser la méthode `.get()` :

```python
print(capitales.get("USA", "Inconnu"))   # Inconnu
```
```
Inconnu
```


## Ajouter ou modifier une valeur

On peut ajouter une nouvelle clé ou modifier une valeur existante.

```python
capitales["Mexique"] = "Mexico"   # ajout
capitales["France"] = "Paris" # modification
print(capitales)
```

```
{'Canada': 'Ottawa', 'France': 'Paris', 'Japon': 'Tokyo', 'Mexique': 'Mexico'}
```

## Supprimer une entrée

On utilise le mot-clé `del`.

```python
del capitales["France"]
print(capitales)
```

```
{'Canada': 'Ottawa', 'Japon': 'Tokyo', 'Mexique': 'Mexico'}
```

## Parcourir un dictionnaire

{{% notice style="accent"  title="Rappel sur la boucle for" %}}
### Syntaxe générale de la boucle for
`for variable in séquence:`

Dans une boucle `for`, la **séquence** est l’ensemble des éléments à parcourir.
La **variable** sert simplement à **recevoir chaque élément** de cette séquence, un à la fois.
{{% /notice %}}

1. Si on veut parcourir toutes les **clés** et **valeurs** on utilise `.items()`.

```python
for pays, capitale in capitales.items():
    print(pays, "→", capitale)
```

```
Canada → Ottawa
Japon → Tokyo
Mexique → Mexico
```

* `.items()` retourne **toutes les paires clé-valeur**.
* `capitales.items()` → c’est **la séquence**, c’est-à-dire **toutes les clés ET toutes les valeurs** du dictionnaire.
* `pays` → c’est la **variable** qui prend **une clé à la fois** pendant le parcours.
* `capitale` → c’est la **variable** qui prend **une valeur à la fois** pendant le parcours.


2. Si on veut parcourir seulement les **clés** on utilise `.keys()`:

```python
for pays in capitales.keys():
    print(pays)
```

```
Canada
Japon
Mexique
```

* `.keys()` retourne **toutes les clés** du dictionnaire.
* `capitales.keys()` → c’est **la séquence**, c’est-à-dire **toutes les clés** du dictionnaire.
* `pays` → c’est la **variable** qui prend **une clé à la fois** pendant le parcours.


3. Si on veut parcourir seulement les **valeurs** on utilise `.values()` :

```python
for capitale in capitales.values():
    print(capitale)
```
```
Ottawa
Tokyo
Mexico
```

* `.values()` retourne **toutes les valeurs** du dictionnaire.
* `capitales.values()` → c’est **la séquence**, c’est-à-dire **toutes les valeurs** du dictionnaire.
* `capitale` → c’est la **variable** qui prend **une valeur à la fois** pendant le parcours.


## Créer une liste à partir d’un dictionnaire

Imaginons que l’on ait relevé les températures d’une ville à différents moments de la journée. On stocke ces données dans un dictionnaire :

```python
# Dictionnaire : heure → température (°C)
temperatures = {
    6: 12,
    9: 15,
    12: 20,
    15: 22,
    18: 19,
    21: 16
}
```

#### 1. Créer une liste avec les **valeurs** du dictionnaire avec `list()` et `.values()`

```python
liste_temp = list(temperatures.values())
print(liste_temp)
```

**Résultat :**
```
[12, 15, 20, 22, 19, 16]
```

#### 2. Créer une liste avec les **clés** du dictionnaire avec `list()` et `.keys()`


```python
liste_heures = list(temperatures.keys())
print(liste_heures)
```

**Résultat :**
```
[6, 9, 12, 15, 18, 21]
```


#### 3. Construire une liste avec une boucle `for`

On peut aussi parcourir le dictionnaire et remplir une liste à la main :

```python
liste_temp2 = []
for valeur in temperatures.values():
    liste_temp2.append(valeur)

print(liste_temp2)
```

**Résultat :**
```
[12, 15, 20, 22, 19, 16]
```

#### 4. Obtenir des couples `(clé, valeur)` avec `.items()`

Si on veut garder **l’heure et la température ensemble**, on peut utiliser `.items()` :

```python
paires = list(temperatures.items())
print(paires)
```

**Résultat :**
```
[(6, 12), (9, 15), (12, 20), (15, 22), (18, 19), (21, 16)]
```
{{% notice style="primary"  title="À savoir" %}}
Ici, il s'agit d'une liste de **tuples**. Un **tuple** c'est un type de données que nous n'étudierons pas dans ce cours.
{{% /notice %}}

## Récapitulatif

* Un **dictionnaire** associe une **clé** à une **valeur**.
* Créer : `{clé: valeur, ...}`
* Accéder : `mon_dico[clé]` ou `mon_dico.get(clé)`
* Ajouter/modifier : `mon_dico[clé] = valeur`
* Supprimer : `del mon_dico[clé]`
* Créer une liste des valeurs : `liste_valeurs = list(mon_dico.values())`
* Créer une liste des clés : `liste_clés = list(mon_dico.keys())`
* Parcourir : boucle `for`. Une boucle `for` permet aussi de construire une liste étape par étape
  * `.values()` → liste des valeurs.
  * `.keys()` → liste des clés.
  * `.items()` → couples (clé, valeur).


<!--
## Exemples d'applications scientifiques

### Exemple 1 – Concentration de solutions

On veut stocker les concentrations de plusieurs solutions.

```python
solutions = {
    "NaCl": 0.10,    # mol/L
    "HCl": 0.05,
    "C6H12O6": 0.20
}
print("Concentration de NaCl :", solutions["NaCl"], "mol/L")
```
```
Concentration de NaCl : 0.1 mol/L
```

### Exemple 2 – Comptage d’ADN

On veut compter le nombre de nucléotides dans une séquence.

```python
sequence = "ATGCGATAC"
compte = {"A": 0, "T": 0, "C": 0, "G": 0}

for base in sequence:
    compte[base] += 1	# Ou compte[base] = compte[base] + 1

print(compte)
```
```
{'A': 3, 'T': 2, 'C': 2, 'G': 2}
```


### Exemple 3 – Résultats expérimentaux

Stocker les résultats de quatre étudiants pour trois examen.

```python
resultats = {
    "Alice": [0.50, 0.88, 0.92],
    "Bob": [0.45, 0.77, 0.86],
    "Chloé": [0.61, 0.69, 0.80],
    "Julien": [0.51, 0.79, 0.90]
}

# Moyenne par étudiant
print("Moyenne par étudiant :")
for etudiant, notes in resultats.items():
    total = 0
    for note in notes:
        total += note
    moyenne = total / len(notes)
    print(f"{etudiant} → {moyenne:.2f}")

# Moyenne par examen
print("\nMoyenne par examen :")
nb_examens = len(next(iter(resultats.values())))  # nombre de colonnes
for i in range(nb_examens):
    total_examen = 0
    nb_etudiants = 0
    for notes in resultats.values():
        total_examen += notes[i]
        nb_etudiants += 1
    moyenne_examen = total_examen / nb_etudiants
    print(f"Examen {i+1} → {moyenne_examen:.2f}")
```
```
Moyenne par étudiant :
Alice → 0.77
Bob → 0.69
Chloé → 0.70
Julien → 0.73

Moyenne par examen :
Examen 1 → 0.52
Examen 2 → 0.78
Examen 3 → 0.87
```

#### Explications

**Moyenne par étudiant** :

* On parcourt chaque clé (nom) et sa liste de notes.
* On fait la somme des notes puis on divise par le nombre de notes.

**Moyenne par examen** :

* On parcourt les indices i correspondant aux examens.
* Pour chaque examen, on additionne la note de tous les étudiants et on divise par le nombre d’étudiants.
-->

---

# Atelier

1. Téléchargez les fichiers de départ (`.ipynb`):   
[Bloc-notes de départ - Physique](https://python-a25.netlify.app/blocnotes/atelier_dictionnaires_physique.ipynb)  
[Bloc-notes de départ - Math](https://python-a25.netlify.app/blocnotes/atelier_dictionnaires_math.ipynb)  
2. Déplacez-le dans votre dossier prévu pour **de la semaine en cours**.
3. Ouvrez votre dossier de travail `programmation-sciences` **à partir de Visual Studio Code**.
   * Vous devriez voir votre structure de dossiers et vos fichiers (.ipynb).


## Exercice - Physique mécanique

### Objectifs

* Manipuler des **dictionnaires** en Python (`temps → valeur`).
* Transformer un dictionnaire en listes triées pour tracer des courbes.
* Tracer **deux courbes** (`v(t)` et `y(t)`) sur le même graphe avec `plot()` et légende.
* Interpréter qualitativement les formes (linéaire vs quadratique).

On veut représenter l’évolution d’un objet en chute libre (sans frottement).
La formule de la vitesse est :
```math
$$
v(t) = g \cdot t
$$
```
et la formule de la position est :
```math
$$
y(t) = \tfrac{1}{2} g \cdot t^2
$$
```

```math
où $ g = 9.8 , m/s^2 $
```

1. **Créer deux dictionnaires vides** `vitesses = {}` et `positions = {}`.

2. **Définir la constante** `g = 9.8` (m/s²).

3. **Remplir les dictionnaires**
   * Pour chaque temps `t` allant de `0` à `5` (inclus), calculez :
     * `v(t) = g * t`
     * `y(t) = 0.5 * g * t**2`
   * Stockez ces valeurs dans les dictionnaires avec `t` comme clé (ex. `vitesses[t] = ...`).
   **Indice** : utiliser `for t in range(6):`

4. **Vérifier le contenu**
   * Affichez les dictionnaires (`print(vitesses)` et `print(positions)`).
   * Vérifiez que les clés apparaissent pour `0,1,2,3,4,5`.

   **Exemple d’attendu (valeurs arrondies)** :
     ```
     vitesses = {0:0.0, 1:9.8, 2:19.6, 3:29.4, 4:39.2, 5:49.0}
     positions = {0:0.0, 1:4.9, 2:19.6, 3:44.1, 4:78.4, 5:122.5}
     ```

5. **Préparer les listes pour le tracé**
   * Les dictionnaires ne garantissent pas l’ordre des clés ; créez une **liste triée** des temps (**Indice** : utiliser `temps = sorted(vitesses.keys())`) :
   * Avec une boucle `for` ou avec la fonction `list`, construire **deux listes** (`valeurs_v` et `valeurs_y`) qui regroupent, dans l’ordre des temps triés (`temps`), les valeurs de la vitesse et de la position extraites des dictionnaires.

6. **Tracer les courbes**
   * Importez `matplotlib.pyplot as plt`.
   * Tracez la **vitesse** : `plt.plot(temps, valeurs_v, label='Vitesse (m/s)')`
   * Tracez la **position** : `plt.plot(temps, valeurs_y, label='Position (m)')`
   * Ajoutez : `plt.title(...)`, `plt.xlabel('Temps (s)')`, `plt.ylabel('Valeur')`, `plt.legend()`, `plt.grid(True)` puis `plt.show()`.
   * Sauvegarder le graphique en PNG : `plt.savefig('chute_libre.png')`.

7. **Interprétation**
   * Écrivez 2–3 phrases : que montre la pente de `v(t)` ? Pourquoi `y(t)` a-t-elle une forme différente ?

![Graphe - Mécanique](./chute_libre.png?width=35wv)
---

## Exercice - Mathématiques

{{% notice style="green" title="Information" %}}
Cet exercice utilise les mêmes notions que dans l'exercice précédent, mais avec moins d'indices.
{{% /notice %}}


### Objectifs

* Utiliser des dictionnaires pour associer `x → f(x)` et `x → f'(x)`.
* Tracer `f(x)` et sa dérivée `f'(x)` sur la même figure.


1. **Créer deux dictionnaires vides** `carres` et `derivees`

2. **Remplir les dictionnaires** pour x = -5 à +5
   * Pour chaque `x`:
     * Calculez `f(x) = x**2` → stockez dans le dictionnaire `carres`.
     * Calculez `f'(x) = 2*x` → stockez dans le dictionnaire `derivees`.

3. **Afficher & vérifier les deux dictionnaires**
   * Vérifiez la symétrie de `carres` (même valeur pour `x` et `-x`) et l’antisimétrie de `derivees` (`f'(-x) = -f'(x)`).

4. **Préparer pour les listes pour le tracé**
   * Trier les `clés` de `carres`.
   * Créer **deux listes** (y_carres et y_derivees) contenant, dans l’ordre des x triés, les valeurs de la fonction et de sa dérivée extraites des dictionnaires correspondants.

5. **Tracer les deux graphiques sur la même figure**
   * Ajoutez titre, axes, légende, grille.
   * Sauvegarder le graphique en PNG avec le nom `quadratique.png`.

6. **Interprétation**
   * Identifiez les points où `f'(x) = 0`. Que se passe-t-il pour `f(x)` à ces points (minimum/maximum) ?

![Graphe - Math](./quadratique.png?width=35wv)
---

## À faire avant le prochain cours


1. Lire la prochaine leçon : [8. Tableaux NumPy et droite de régression](../semaine8/)
2. Faire les exercices de la prochaine leçon <!--[prochaine leçon :](../semaine8/#exercices)  A MODIFIER -->
