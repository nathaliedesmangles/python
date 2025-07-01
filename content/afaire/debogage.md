+++
title = "Débogage pas à pas"
weight = 3
+++


## Objectifs de la séance (2h)

* Comprendre comment fonctionne le débogueur dans PyCharm.
* Apprendre à utiliser les points d'arrêt (breakpoints), la fenêtre des variables, les options **Step Over**, **Step Into**, **Evaluate Expression**, etc.
* Réviser les structures conditionnelles (`if/elif/else`) et les boucles (`for`, `while`) en les testant pas à pas.
* Apprendre à identifier les erreurs logiques classiques en sciences (unités, ordre des opérations, initialisation incorrecte, etc.).

---

## Plan de la séance (2h)

| Temps     | Activité                                                                         |
| --------- | -------------------------------------------------------------------------------- |
| 0:00-0:15 | Introduction au débogueur PyCharm (démonstration)                                |
| 0:15-0:35 | Exemple guidé 1 : `if/elif/else` – température de changement d’état              |
| 0:35-1:00 | Exercice 1 : Identifier les erreurs dans un modèle de dilatation thermique       |
| 1:00-1:20 | Exemple guidé 2 : boucle `for` – somme des masses d’échantillons                 |
| 1:20-1:40 | Exercice 2 : Corriger une boucle `while` mal conditionnée (demi-vie radioactive) |
| 1:40-2:00 | Défi final : simulation simplifiée de chute libre avec erreur à trouver          |

---

## Outils

* PyCharm installé.
* Mode “Debug” activé (menu **Run > Debug...**).
* Possibilité de partager l’écran de l’élève ou d’utiliser un environnement collaboratif si permis.
* [Vidéo YouTube](https://youtu.be/j0Wz_uBaDmo)
* [Site JetBrains](https://www.jetbrains.com/help/pycharm/part-1-debugging-python-code.html#start-debugger-session)

---

## Exemple guidé 1 : Conditions – Température de l’eau

```python
temp = 100

if temp < 0:
    print("Solide (glace)")
elif temp < 100:
    print("Liquide")
else:
    print("Gaz (vapeur)")
```

### But : mettre des points d'arrêt

1. Ajouter un point d'arrêt sur chaque ligne.
2. Exécuter le programme en mode Debug.
3. Observer la variable `temp` et les branches conditionnelles prises.
4. Modifier la valeur de `temp` à 50 et recommencer.

---

## 🔧 Exercice 1 : Dilatation thermique (avec erreur)

```python
# Dilatation thermique: ΔL = L0 * α * ΔT
L0 = 10  # longueur initiale en m
alpha = 0.000012  # coefficient de dilatation (/°C)
temp_initiale = 20
temp_finale = 50

delta_L = alpha * L0 + (temp_finale - temp_initiale)  # ERREUR ICI

print("Allongement =", delta_L, "m")
```

### Tâches de l’élève

* Mettre des points d’arrêt.
* Corriger l’erreur dans le calcul (`+` au lieu de `*`).
* Modifier `L0`, `alpha` et vérifier le résultat attendu.

---

## Exemple guidé 2 : Boucle `for` – Masse totale

```python
masses = [1.2, 3.5, 2.1, 0.9]
somme = 0

for m in masses:
    somme += m

print("Masse totale:", somme, "g")
```

### Objectifs :

* Suivre l’évolution de `somme` à chaque itération.
* Utiliser l’inspecteur de variables.
* Tester avec une liste vide ou avec des valeurs négatives.

---

## Exercice 2 : Boucle `while` – Demi-vie radioactive (avec erreur logique)

```python
# Masse d’un isotope radioactif qui décroît à chaque période
masse = 100
demi_vie = 5
temps = 0

while masse > 0:
    masse = masse / 2
    temps = temps + demi_vie

print("Temps total:", temps)
```

### Erreurs à détecter :

* Boucle infinie possible si `masse` devient très petit mais jamais exactement 0.
* Ajouter une **masse minimale détectable** comme critère d’arrêt.

### Version corrigée proposée :

```python
masse = 100
demi_vie = 5
temps = 0
seuil = 0.1

while masse > seuil:
    masse = masse / 2
    temps += demi_vie

print("Temps écoulé:", temps, "ans")
```

---

## Défi final : Chute libre (détection d’un bug)

```python
# Chute libre avec v = v0 + g*t, h = h0 - v*t
g = 9.8
v0 = 0
h0 = 100
t = 0
dt = 1
h = h0

while h > 0:
    v = v0 + g * t
    h = h0 - v * t
    print(f"Temps: {t}s, Hauteur: {h:.2f}m")
    t += dt
```

### Problèmes :

* `v` est recalculée à chaque fois en fonction du **temps total**, pas de l’étape actuelle.
* `h0` reste fixe – il faut accumuler les vitesses à chaque pas.

### Version corrigée :

```python
g = 9.8
v = 0
h = 100
t = 0
dt = 1

while h > 0:
    v = v + g * dt
    h = h - v * dt
    print(f"Temps: {t}s, Hauteur: {h:.2f}m")
    t += dt
```

---

## À faire après la séance

* Reprendre les exercices avec d'autres données ou contextes scientifiques (e.g., réaction exothermique, refroidissement de Newton).
* Installer un plugin PyCharm comme “EduTools” pour avoir d'autres exercices interactifs.
* Faire une fiche-rappel des **symboles du débogueur** (Step Over, Into, Out, Resume, etc.).
