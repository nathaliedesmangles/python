+++
title = "Evaluation formative"
weight = 104.1
draft = true
+++

## Informations générales

**Durée : 2h**  
**Outils autorisés :** VS Code, feuille de notes personnelle.  
**Interdits :** Internet, site du cours, IA, etc.  

---

## Objectifs évalués

* Comprendre l’utilité des variables
* Utiliser les types de base (`int`, `float`, `str`, `bool`)
* Gérer les entrées et les affichages
* Utiliser des fonctions prédéfinies
* Créer des fonctions simples (`def`, `param`, `return`)
* Traduire un algorithme simple
* Lire et corriger un code erroné

---

## Instructions

1. Créez un dossier nommé `formatif_nom_prenom`
2. Enregistrez un fichier `.ipynb` par question : `q1.ipynb`, `q2.ipynb`, etc.

---

### **Q1 – Masse d’eau transpirée (15 pts)**

Une plante transpire en moyenne **0,35 litre d’eau par jour**.

Écrivez un programme qui :

1. Demande à l’utilisateur combien de jours ont été mesurés
2. Calcule la masse d’eau totale transpirée
3. Affiche le résultat dans une phrase claire

---

### **Q2 – Conversion de surface foliaire (15 pts)**

Une feuille a une surface mesurée en **cm²**, mais les données doivent être présentées en **m²**.

Écrivez un programme qui :

1. Demande une surface en cm² (float)
2. La convertit en m²
3. Affiche les deux valeurs avec une phrase claire

---

### **Q3 – Utilisation de fonctions prédéfinies (10 pts)**

Écrivez un programme qui :

1. Demande à l’utilisateur une **hauteur de tige** en cm
2. Utilise `round()` pour arrondir la hauteur à **l’unité la plus proche**
3. Affiche la hauteur initiale et la hauteur arrondie

---

### **Q4 – Définir une fonction : densité de plantation (20 pts)**

On souhaite calculer la **densité de plantation** :
```math
$$
\text{densité} = \frac{\text{nombre de plants}}{\text{surface (en m²)}}
$$
```

1. Définissez une fonction `densite_plants(nb_plants, surface)` qui retourne la densité
2. Demandez à l’utilisateur les deux valeurs
3. Appelez la fonction et affichez le résultat

---

### **Q5 – Débogage (15 pts)**

Corrigez ce programme en expliquant **chaque correction** dans un commentaire.

```python
def surface_totale(nb_feuilles surface_feuille_cm2):
    total = nb_feuilles * surface_feuille_cm2
    return total

nb = input("Nombre de feuilles : ")
sf = input("Surface d’une feuille (cm2) : ")

total_surface = surface_totale(nb, sf)
print("Surface totale : total_surface  cm2")
```

---

### **Q6 – Types de base (15 pts)**

Créez un programme qui déclare et affiche les variables suivantes :

* `plante` = `"Tournesol"`
* `hauteur` = 158.6
* `fleurie` = True
* `nombre_feuilles` = 34

Affichez ces informations clairement, chacune sur sa propre ligne.

---

### **Q7 – Traduction d’un algorithme (10 pts)**

Traduisez ce petit algorithme en code Python :

1. Demander la **masse fraîche** (en g) et le **taux d’eau** (%)
2. Calculer la **masse sèche** :
    `masse_sèche = masse_fraîche * (1 - taux_eau / 100)`
3. Afficher la masse sèche obtenue.