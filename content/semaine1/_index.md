+++
chapter = true
pre = "<b>Semaine 1.</b>"
title = "Introduction à Python et à l'algorithmie"
weight = 10
+++

## Objectifs de la leçon

- Comprendre ce qu’est un langage de programmation
- Identifier les types de données de base en Python
- Écrire des expressions simples en Python
- Créer des scripts simples avec des calculs scientifiques
- S’initier à la logique algorithmique

--- 

## Plan de la leçon

| Section | Durée (approx.) |
|--------|:--------:|
| 1. Pourquoi Python ? | 2 min |
| 2. Présentation d’Anaconda et Jupyter | 5 min |
| 3. Variables et types de base | 10 min |
| 4. Opérations mathématiques de base | 5 min |
| 5. Fonctions intégrées utiles | 15 min |
| 6. Qu’est-ce qu’un algorithme ? | 5 min |
| 7. Exemples d'algorithmes simples | 5 min |
| **Pause** | **10 min** |
| 8. Activité pratique en classe | 1h50 |
| 9. Activité pratique à la maison | 3h |

---

## 1. Pourquoi apprendre Python en science ?

- **Polyvalence** : utilisé en bio, chimie, physique, météo, environnement, IA.
- **Lisibilité** : syntaxe claire = moins de stress pour les débutants.
- **Gratuit** et supporté par une **grande communauté** scientifique.
- Nombreux modules utiles : `numpy`, `matplotlib`, `pandas`, etc.

📌 **Exemple** : _afficher le résultat d’un calcul_  
```python
print(9.81 * 2)
```

## 2. Présentation de l’environnement (Anaconda et Jupyter) 

- Lancer ***Anaconda Navigator*** → ouvrir ***Jupyter Notebook***
- Avantages de Jupyter :
  - Mélange de texte, de code, de graphiques
  - Très utilisé dans les labos pour documenter les expériences

💡 Cellule code vs cellule texte dans un notebook.

## 3. Variables et types de base

Une **variable** est une zone de la mémoire de l’ordinateur dans laquelle une valeur est stockée. 

### 3.1 Nommer une variable

### 3.2 Types principaux de base

| Type | Exemple | Description |
|------S-|:---------:|-------------|
| `int` | `5` | entier |
| `float` | `3.14` | nombre décimal |
| `str` | `"bonjour"` ou `'bonjour'` | chaîne de caractères |
| `bool` | `True`, `False` | valeur logique |

### 3.3 Création d’une variable

- Pour stocker un valeur dans une variable, on utilise le symbole **égal** (`=`) 

#### 3.3.1 Règles pour nommer une variable

- Utiliser des noms significatifs: le nom doit permettre de savoir quelle information elle contient.
- Commencer par une lettre ou un underscore (`_`)
- Ensuite, utiliser des lettres, des chiffres et/ou des underscores
   <span style="color:red;"><b>NB</b>: Ne jamais utiliser de lettres accentuées, ni de caractères spéciaux</span>.
- Respecter la casse (en Python, `prenom` et `Prenom` sont deux variables différentes.
- Ne pas utiliser les mots appartenant au langage Python (ex: `print`, `input`, etc.)

📌 **Exemples de noms valides**

```python
temperature_celsius = 22   # int
prenom = "Nathalie"	       # str
impot2025 = 1234.5         # float
coursReussi = True         # bool
```

> [!Warning]
> Une fois qu'on a créé une variable, c'est elle qu'on utilise à la place de la valeur qu'elle contient.

## 4. Opérations mathématiques de base

```python
# Addition
a = 5 + 2    # 7

# Soustraction
b = 10 - 4   # 6

# Multiplication
c = 3 * 4    # 12

# Divisions
d = 8 / 2    # 4.0 pas 4
e = 10 // 3  # 3 pas 3.0 ni 3.3333

# Puissance
f = 2 ** 3   # 8

# Modulo (reste)
g = 10 % 3   # 1
```

## 5. Fonctions intégrées utiles

| Fonction | Utilité | Exemple |
|----------|--------|---------|
| `print()` | Afficher à l’écran | `print("Bonjour !")` |
| `type()` | Voir le type d’une variable | `type(3.14)` |
| `round()` | Arrondir | `round(3.14159, 2)` → `3.14` |
| `input()` | Entrée utilisateur (à venir plus tard) | `input("Ton nom ?")` |

📌 **Exemple 1** : afficher à l'écran avec `print()` :
```python
prenom = "Nathalie"
print("Bonjour", prenom, "et bienvenue dans le monde de Python !")
```

📌 **Exemple 2** : prédire le type avec `type()` :
```python
type(22)
type("python")
type(3.0)
type(True)
```

📌 **Exemple 3** : arrondir avec `round()` :

**Arrondir à l'entier le plus proche**
```python
resultat = 10 / 3   # 3.333333333333333
resultat_arrondi = round(resultat)
print(resultat_arrondi)
3

nombre = 3.567
nombre_arrondi = round(nombre)
print(nombre_arrondi)
4
```

**Arrondir à 2 décimales**
```python
nombre = 3.567
nombre_arrondi = round(nombre,2)
print(nombre_arrondi)
3.57
```

## 6. Qu’est-ce qu’un algorithme ?

- **Définition simple** : une suite d’instructions ordonnées pour résoudre un problème.
- **Lien avec les sciences** : les expériences sont souvent des suites d’étapes.
- Exemples quotidiens :
  - Recette de cuisine
  - Mode d’emploi
  - Protocole expérimental

## 6.1. Exemples d'algorithmes simples

📌 **Exemple 1** : Pseudo-algorithme de conversion Celsius → Fahrenheit :
```
1. Lire la température en Celsius
2. Multiplier par 9
3. Diviser par 5
4. Ajouter 32
5. Afficher le résultat
```

**Traduit en Python**
```python
c = 25
f = c * 9 / 5 + 32
print(c, "°C = ", f, "°F°")
```

📌 **Exemple 2** : Calcul de l'aire d’un cercle
```
1. Lire le rayon du cercle.
2. Multiplier la valeur de Pi(3.14) au rayon²
3. Afficher le résultat.
```

**Traduit en Python**
```python
rayon = 3
aire = 3.14 * rayon ** 2
print("L'aire du cercle est de", aire, "cm²")
```

---

## 2. Activité pratique en classe :  Calculer l’indice de masse corporelle (IMC) pour une population d'étudiants.

**Contexte scientifique** : L’IMC est utilisé pour évaluer la corpulence d’une personne. Ce n’est pas un indicateur parfait, mais il est utile à grande échelle.
```
Formule : IMC = poids (kg) / (taille (m))²
```

Utiliser le fichier semaine1.ipynb: 
---

## 3. Activités pratiques à la maison (3h)

- Réviser la matière d'aujourd'hui, refaites les exemples et modifier ou ajouter des variables afin
- Gestion des fichiers et dossiers 
- Lecture du plan de cours (quiz oralement au prochain cours)

 