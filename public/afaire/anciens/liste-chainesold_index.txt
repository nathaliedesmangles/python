+++
chapter = true
pre = "<b>Semaine 5.</b>"
title = "Listes et chaînes de caractères"
weight = 50
+++


## Objectifs de la leçon

* Comprendre ce qu’est une **liste** et comment la manipuler
* Utiliser les **chaînes de caractères** comme des séquences
* Appliquer les connaissances à des données scientifiques simples
* Travailler en équipe sur une activité d’analyse de mesures

---

## Listes en Python

Une **liste** est une collection **ordonnée**, **modifiable**, qui peut contenir différents types de données.

### Définir une liste :

```python
mesures = [12.1, 13.0, 12.8, 13.5]
```

### Accéder à un élément

```python
print(mesures[0])    # 12.1
print(mesures[-1])   # 13.5 (dernier élément)
```

### Modifier un élément

```python
mesures[1] = 13.2
```

### Ajouter ou retirer

```python
mesures.append(14.0)     # Ajoute à la fin
mesures.remove(12.8)     # Retire la première occurrence
```

### Longueur d’une liste

```python
len(mesures)  # Nombre d’éléments
```

## Chaînes de caractères (strings)

Une chaîne de caractères est aussi une **séquence** (comme une liste), mais **immutable** (non modifiable).

```python
mot = "science"
print(mot[0])        # 's'
print(mot[-1])       # 'e'
print(len(mot))      # 7
```

### Quelques méthodes utiles

```python
mot.upper()          # 'SCIENCE'
mot.lower()          # 'science'
mot.replace("c", "k")  # 'skience'
```

### Parcourir une liste ou une chaîne (boucle for)

```python
for valeur in mesures:
    print(valeur)
```

```python
for lettre in mot:
    print(lettre)
```

## Mini-activité en équipe (20 min)

**Contexte :** Une étudiante en biologie a mesuré la croissance d’une colonie bactérienne pendant 5 jours :

```python
croissance = [0.8, 1.1, 1.5, 2.2, 2.9]
```

**Tâches (en équipe de 2 ou 3) :**

1. Affichez la croissance moyenne.
2. Trouvez le jour où la croissance dépasse 2.0.
3. Affichez tous les jours où la croissance a augmenté par rapport à la veille.
4. Ajoutez la valeur du jour 6 (valeur fictive) à la liste.

> **Bonus** : Créez une nouvelle liste avec uniquement les valeurs supérieures à 1.5.

## Défi individuel (10 min)

Demande à l’utilisateur de saisir une phrase. Ton programme doit :

* Compter le nombre de mots (en utilisant `.split()`)
* Afficher le mot le plus long

```python
phrase = input("Entrez une phrase : ")
```

## Pour aller plus loin (facultatif)

* Triez une liste de données (`.sort()`)
* Comptez combien de fois un mot ou une valeur apparaît (`.count()`)
