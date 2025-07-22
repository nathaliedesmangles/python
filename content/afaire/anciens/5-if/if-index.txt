+++
chapter = true
pre = "<b>Semaine 3.</b>"
title = "Prendre des décisions avec `if`, `elif`, `else`"
weight = 30
+++

### Objectifs d’apprentissage

À la fin de cette leçon, vous devrez être capable de :

* Écrire des instructions conditionnelles en Python
* Utiliser `if`, `elif` et `else` pour gérer plusieurs cas
* Évaluer des expressions logiques avec les opérateurs de comparaison (`==`, `!=`, `<`, `>`, `<=`, `>=`)
* Combiner plusieurs conditions avec les opérateurs logiques (`and`, `or`, `not`)

---

## Pourquoi des conditions ?

Un programme prend souvent des décisions :

* S’il fait moins de 0 °C, l’eau gèle.
* Si un patient a une température > 38 °C, il a de la fièvre.
* Si la vitesse dépasse 120 km/h, une alarme est déclenchée.

Ces situations sont modélisées avec des **conditions**.

## La structure `if` de base

```python
temp = -5

if temp < 0:
    print("L'eau est solide (glace).")
```

**Rappel important :** L’indentation (espaces ou tabulation) est **obligatoire** pour indiquer le bloc conditionnel.


## Ajouter un cas alternatif avec `else`**

```python
temp = 20

if temp < 0:
    print("Glace")
else:
    print("Pas de glace")
```

## Gérer plusieurs cas avec `elif`

```python
temp = 100

if temp < 0:
    print("Solide (glace)")
elif temp < 100:
    print("Liquide")
else:
    print("Gaz (vapeur)")
```

Note : Python évalue les conditions **dans l’ordre**. Dès qu’une condition est vraie, il saute les suivantes.

---

## Opérateurs de comparaison utiles

| Opérateur | Signification     | Exemple  |
| --------- | ----------------- | -------- |
| `==`      | égal à            | `a == b` |
| `!=`      | différent de      | `a != b` |
| `<`       | plus petit que    | `a < b`  |
| `>`       | plus grand que    | `a > b`  |
| `<=`      | inférieur ou égal | `a <= b` |
| `>=`      | supérieur ou égal | `a >= b` |


## Combiner les conditions avec `and`, `or`, `not`

```python
temp = 80
pression = 1.0

if temp > 0 and temp < 100:
    print("L’eau est liquide à pression normale.")
```

```python
if temp > 100 or pression > 1.5:
    print("Attention à l’ébullition !")
```

---

## Application scientifique simple

```python
temp = float(input("Température en °C : "))

if temp < 0:
    print("L’eau est sous forme de glace.")
elif temp < 100:
    print("L’eau est liquide.")
else:
    print("L’eau est sous forme de vapeur.")
```

---

## Petits exercices pratiques

1. Écris un programme qui indique si un étudiant a réussi ou échoué selon sa note (seuil : 60 %).
2. Demande un pH à l’utilisateur et affiche si la solution est acide, neutre ou basique.
3. Crée un programme qui vérifie si un triangle est équilatéral, isocèle ou scalène selon les longueurs des côtés.

---

## Pour aller plus loin

* Que se passe-t-il si aucune condition n’est vraie et qu’il n’y a pas de `else` ?
* Peut-on avoir plusieurs `elif` dans une même structure ? (Réponse : Oui)
* Peut-on imbriquer des `if` dans d’autres `if` ? (Réponse : Oui, mais attention à la lisibilité)

