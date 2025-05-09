+++
title = "L'environnement de travail et Introduction à Python"
weight = 11
+++

## Objectifs d’apprentissage

À la fin de cette leçon, devez être en mesure de :

* Utiliser **Anaconda** et **Jupyter Notebook**
* Créer et exécuter une cellule de code
* Définir des **variables**
* Manipuler des **types de base** : `int`, `float`, `str`, `bool`

---

## Qu'est-ce qu’Anaconda ?

**Anaconda** est une distribution Python qui inclut :

* Python 3
* Jupyter Notebook
* Des bibliothèques scientifiques (numpy, matplotlib, pandas, etc.)

## Lancement de Jupyter Notebook

1. Ouvrir **Anaconda Navigator**
[](./)
2. Cliquer sur **"Launch"** à côté de *Jupyter Notebook*
[](./)
3. Le navigateur s’ouvre sur une interface locale.
[](./)
4. Naviguer jusqu’au dossier de votre choix et cliquer sur **"New > Python 3 Notebook"**.
[](./)

## Premiers pas avec Jupyter

* Chaque **cellule** permet d’écrire du code Python.
* Pour **exécuter** une cellule : `Shift + Enter`
* Vous pouvez aussi ajouter du **texte formaté** en changeant le type de cellule en *Markdown*.

### Exemple :

```python
# Ceci est un commentaire
print("Bonjour le monde !")
```

## Variables et types de base

### Variables

Une **variable** sert à stocker une information :

```python
nom = "Camille"
age = 18
```

### Types de base

| Type    | Description                  | Exemple         |
| ------- | ---------------------------- | --------------- |
| `int`   | Nombre entier                | `x = 12`        |
| `float` | Nombre décimal               | `pi = 3.14`     |
| `str`   | Chaîne de caractères         | `nom = "Alice"` |
| `bool`  | Valeur booléenne (vrai/faux) | `actif = True`  |


### Exemples à tester :

```python
# Types de base
temperature = 22.5       # float
pression = 101325        # int
ville = "Montréal"       # str
pluie = False            # bool

# Affichage
print("Il fait", temperature, "degrés à", ville)
```

### Vérifier le type d’une variable :

```python
type(temperature)  # Résultat : <class 'float'>
```

---

### À retenir

* Python est sensible à la **casse** : `Nom` ≠ `nom`
* Les noms de variables ne doivent **pas commencer par un chiffre**
* Utilisez des noms clairs et significatifs (ex : `masse`, `volume`, `vitesse`)

---

### Activité suggérée pour la maison

* Si vous avez un ordinateur à la maison: Installer Anaconda et créer un premier fichier `.ipynb`
**Étapes pour installer Anaconda** :
	1. Aller sur [Le site d'Anaconda](https://www.anaconda.com/products/distribution)
	2. Télécharger la version **Windows, Mac ou Linux** selon votre système.
	3. Suivre les instructions d’installation. Accepter les options par défaut.
* Reproduire et modifier les exemples de cette leçon
* Changer les valeurs des variables et observer les résultats

