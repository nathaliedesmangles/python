+++
title = "Évaluation #1 (20%) + solution"
weight = 104
draft = false
+++

## Information générale

* **Durée** : 2h et 2h40 pour les étudiants du ***SAA***

{{% notice style="accent" title="Important" %}}

1. *Ce n’est pas un examen pour ChatGPT... c’est pour vous !*

   * Pendant cette évaluation, **vous êtes la seule intelligence permise dans la pièce.**

2. Voici ce qui est **interdit** (désolé ChatGPT, Copilot, etc.) :

   * **IA** : ChatGPT, Copilot, Bard, Gemini et toute la clique
   * **Internet** : site du cours, Stack Overflow, forums, TikTok,....
   * Vos **collègues**, votre **chat** 😉 ou votre **petit.e frère/sœur programmeur**.

3. La **seule ressource autorisée** :

   * **votre feuille de notes personnelle** recto-verso (manuscrite ou imprimée), faite par vous, pour vous.

---

**Pourquoi ?**

* Parce que ce qu’on veut corriger, c’est **votre cerveau, pas une application tierce.**

⚠️**Tricher = conséquences sérieuses.**

* On préfère vous voir réussir honnêtement, même partiellement, que parfaitement avec triche.
* 
{{% /notice %}}

---

## Barème général (100 pts)

| Compétence évaluée                   | Points  |
| ------------------------------------ | :-----: |
| Variables et types de base           | 20      |
| Fonctions prédéfinies                | 10      |
| Fonctions définies par l’utilisateur | 20      |
| Saisies et affichages clairs         | 15      |
| Traduction d’algorithmes             | 10      |
| Débogage avec explication            | 15      |
| Organisation des fichiers / nommage  | 10      |
| **Total**                           | **100** |

---

## Contexte général

Vous êtes stagiaire dans un laboratoire de nutrition animale. Vous devez automatiser certains calculs simples effectués sur les animaux d’élevage pour aider les techniciens à faire des recommandations. Toutes les données proviennent de pesées ou mesures manuelles faites en laboratoire.

Vous devez écrire plusieurs petits programmes Python autonomes qui répondront à des besoins spécifiques.

---

## Avant de commencer à coder

> Ouvrez **VS Code**, créez : 

* un **dossier appelé `examen1_nom_prenom`**, et placez-y
* **un fichier `.ipynb` par question**, nommé `question1.ipynb`, `question2.ipynb`, etc.

## Remise : format obligatoire

* Vous devez remettre **une archive (.zip)** du dossier `examen1_nom_prenom` sur Moodle.

### **Question 1** – Masse totale de rations (15 pts)

Chaque jour, un animal reçoit une ration de 2,4 kg de nourriture.
Écrivez un programme qui :

1. Demande à l’utilisateur **le nombre de jours d’alimentation** (`int`)
2. Calcule la **masse totale de nourriture** donnée pendant ces jours
3. **Affiche le tout clairement** sous forme de phrase

**Exemple d'exécution** :

```
Entrez le nombre de jours d'alimentation : 5
L'animal a reçu 12.0 kg de nourriture au total.
```

---

### **Question 2** – Conversion de longueur intestinale (15 pts)

Chez certains animaux, on mesure la **longueur de l’intestin** en **cm**, mais on doit la rapporter en **mètres** dans les rapports.

Écrivez un programme qui :

1. Demande à l’utilisateur une longueur en **centimètres** (float).
2. Calcule la longueur en **mètres**.
3. Affiche les deux valeurs dans une **phrase claire**.

---

### **Question 3** – Utiliser des fonctions prédéfinies (10 pts)

1. Demandez à l’utilisateur une **masse en kg** à 2 décimales (float)
2. Utilisez la fonction `round()` pour arrondir cette masse à **1 chiffre après la virgule**.
3. Affichez la masse initiale et la **masse arrondie**.

---

### **Question 4** – Définir et utiliser une fonction simple (20 pts)

Vous devez calculer l’**indice de consommation alimentaire (ICA)** qui se définit ainsi :

$$
ICA = \frac{\text{quantité de nourriture consommée (kg)}}{\text{gain de poids (kg)}}
$$


1. Créez une fonction nommée `indice_consommation` qui prend deux paramètres : `nourriture` et `gain`.
2. Elle retourne l’ICA (float).
3. Dans le programme principal, demandez à l’utilisateur les deux valeurs.
4. Appelez la fonction et affichez le résultat de manière lisible.

---

### **Question 5** – Débogage (15 pts)

Voici un programme incomplet. Corrigez les erreurs **une à une**, en utilisant des instructions `print()` si nécessaire pour comprendre les erreurs. Expliquez brièvement **chaque correction** dans un **commentaire**.

```python
def masse_totale(nbr_animaux, masse_individuelle)
    total = nbr_animaux * masse_individuelle
    return total

nbr = input("Nombre d'animaux : ")
masse = input("Masse de chaque animal (kg) : ")

resultat = masse_totale(nbr, masse)
print "Masse totale :  resultat kg"
```

---

### **Question 6** – Types de base (15 pts)

Écrivez un programme qui déclare et affiche les variables suivantes :

* `espece` = `"bovins"`
* `nombre` = 12 (int)
* `masse_totale` = 564.3 (float)
* `controle_qualite` = True (bool)

Exemple d'affichage :

```
Espèce : bovins
Nombre d’individus : 12
Masse totale : 564.3 kg
Contrôle qualité passé : True
```

---

### **Question 7** – Traduction d’un algorithme (10 pts)

Traduisez cet **algorithme en langage naturel** en **code Python**.

1. Demander la masse sèche (en kg) et le taux d’humidité (%)
2. Calculer la masse humide avec :

```math
$$masse\\\_humide = masse\\\_seche / (1 - taux\\\_humidite / 100)$$
```

3. Afficher la masse humide obtenue de façon claire et précise.

---
---

## Solutions

### `question1.ipynb` – Masse totale de rations (15 pts)

```python
# Masse quotidienne en kg
ration = 2.4

# Entrée
jours = int(input("Entrez le nombre de jours d'alimentation : "))

# Calcul
masse_totale = jours * ration

# Affichage
print(f"L'animal a reçu {masse_totale} kg de nourriture au total.")
```

---

### `question2.ipynb` – Conversion de longueur intestinale (15 pts)

```python
# Entrée
longueur_cm = float(input("Entrez la longueur de l’intestin (en cm) : "))

# Conversion
longueur_m = longueur_cm / 100

# Affichage
print(f"Longueur : {longueur_cm} cm = {longueur_m} m")
```

---

### `question3.ipynb` – Utiliser des fonctions prédéfinies (10 pts)

```python
# Entrée
masse = float(input("Entrez une masse en kg (2 décimales): "))

# Arrondi
masse_arrondie = round(masse, 1)

# Affichage
print(f"Masse initiale : {masse} kg")
print(f"Masse arrondie : {masse_arrondie} kg")
```

---

### `question4.ipynb` – Définir et utiliser une fonction simple (20 pts)

```python
# Définition de la fonction
def indice_consommation(nourriture, gain):
    return nourriture / gain

# Entrées utilisateur
n = float(input("Quantité de nourriture consommée (kg) : "))
g = float(input("Gain de poids de l’animal (kg) : "))

# Appel de la fonction
ica = indice_consommation(n, g)

# Affichage
print(f"L’indice de consommation alimentaire (ICA) est : {ica}")
```

---

### `question5.ipynb` – Débogage (15 pts)

```python
# Correction 1 : oubli des deux-points à la fin de la ligne def
def masse_totale(nbr_animaux, masse_individuelle):
    # Correction 2 : ok ici
    total = nbr_animaux * masse_individuelle
    return total

# Correction 3 : convertir les entrées en float
nbr = int(input("Nombre d'animaux : "))
masse = float(input("Masse de chaque animal (kg) : "))

# Correction 4 : appel correct
resultat = masse_totale(nbr, masse)

# Correction 5 : print avec parenthèses (Python 3)
print("Masse totale :", resultat, "kg")
```

---

### `question6.ipynb` – Types de base (15 pts)

```python
espece = "bovins"           # str
nombre = 12                 # int
masse_totale = 564.3        # float
controle_qualite = True     # bool

print(f"Espèce : {espece}")
print(f"Nombre d’individus : {nombre}")
print(f"Masse totale : {masse_totale} kg")
print(f"Contrôle qualité passé : {controle_qualite}")
```

### `question7.ipynb` – Traduction d’un algorithme (10 pts)

```python
# Entrées
masse_seche = float(input("Entrez la masse sèche (kg) : "))
taux_humidite = float(input("Entrez le taux d’humidité (%) : "))

# Calcul
masse_humide = masse_seche / (1 - taux_humidite / 100)

# Affichage
print(f"La masse humide est de {masse_humide} kg.")
```

