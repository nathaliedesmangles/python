+++
chapter = true
pre = "<b>Semaine 2.</b>"
title = "Structures de contrôle (conditions et boucles)"
weight = 20
+++

## Objectifs de la leçon

- Comprendre et utiliser les structures de contrôle : `if`, `while`, `for`
- Maîtriser l’indentation en Python
- Appliquer des opérateurs logiques (`and`, `or`, `not`)
- Réfléchir à l’ordre logique dans un programme

--- 

## Plan de la leçon

| Section | Durée (approx.) |
|--------|:--------:|
| 1. Boucle while | 2 min |
| 2. Conditions d’arrêt | 5 min |
| 3. Listes pour stocker les températures | 10 min |
| 4. Affichage formaté (print, round)| 5 min |
| 5. (Optionnel) matplotlib pour visualisation | 15 min |
| **Pause** | **10 min** |
| 6. Activité pratique en classe | 1h50 |
| 7. Activité pratique à la maison | 3h |

---

## 1. Structure d’un `if` (10 min)

### Syntaxe :
```python
if condition:
    instruction1
elif autre_condition:
    instruction2
else:
    instruction3
```

### Indentation
- L’indentation **(espacement en début de ligne)** est **obligatoire** en Python pour indiquer les blocs de code.
- Convention : 4 espaces

### Opérateurs logiques utiles :
- `==` (égal à)
- `!=` (différent de)
- `>` `<` `>=` `<=`
- `and`, `or`, `not`

### Exemple en direct :
```python
x = float(input("Entrez un nombre : "))

if x > 0:
    print("Le nombre est positif.")
elif x < 0:
    print("Le nombre est négatif.")
else:
    print("Le nombre est nul.")
```

---

## 2. Boucle `while` (10 min)

### Principe :
La boucle `while` répète un bloc **tant qu’une condition est vraie**.

```python
while condition:
    instructions
```

### Exemple en direct :
**Affiche les minutes jusqu'à l’ébullition (100°C)**
```python
temp = 20
minutes = 0

while temp < 100:
    print(f"Minute {minutes} : {temp} °C")
    temp += 5
    minutes += 1

print("Ébullition atteinte !")
```

---

## 3. Boucle `for` (10 min)

### Principe :
La boucle `for` est idéale pour **répéter un nombre connu de fois**, ou **parcourir une séquence** (ex : liste, chaîne de caractères, `range()`).

```python
for élément in séquence:
    instructions
```

### Exemple en direct :
**Calculer la vitesse (v = d/t) pour plusieurs distances fixes**

```python
distances = [10, 20, 30, 40]  # en mètres
temps = 2  # secondes

for d in distances:
    v = d / temps
    print(f"Distance : {d} m, Vitesse : {v} m/s")
```

---

## 4. Importance de l’ordre logique (10 min)

- Un programme **se lit de haut en bas**.
- Une mauvaise organisation peut conduire à des **résultats erronés**.
- L’ordre : **entrée → traitement → sortie**
- Exemple courant d’erreur : utiliser une variable **avant de lui avoir donné une valeur**.

### Mini-démo :
```python
# Mauvais ordre :
print(resultat)
resultat = 5 + 2
# Erreur : la variable n'existe pas encore
```

---

## Conclusion et transition vers la pratique (5 min)

- Les structures conditionnelles (`if`) permettent à votre programme de **prendre des décisions**.
- Les boucles (`while` et `for`) permettent de **répéter des actions** efficacement.
- L’indentation est **essentielle** pour structurer le code.
- Il faut toujours penser à la **logique du déroulement** du programme.


---

2. Activité pratique (1h50)
Titre : Refroidissement d’un café – Modélisation par la loi de Newton
Contexte scientifique
Lorsqu’un café chaud est laissé sur une table, sa température diminue avec le temps. La loi de Newton du refroidissement modélise cette situation :

Formule :
T(t+1) = T(t) - k * (T(t) - T_env)
où :

T(t) est la température à l’instant t

T_env est la température ambiante

k est une constante de refroidissement





