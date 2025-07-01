+++
title = "Boucles while et for"
weight = 2
+++

## Objectifs de la séance

* Réviser les structures conditionnelles (`if`, `elif`, `else`)
* Comprendre les boucles (`while`, `for`)
* Appliquer ces notions à des situations scientifiques simples (physique, chimie, biologie)

## Plan de la séance

### **0. Accueil et mise en contexte (10 min)**

* Présentation des objectifs
* Brève discussion sur ce que les étudiants trouvent difficile
* Partage d’un fichier Jupyter Notebook ou Google Colab

---

### 1. Révision des structures conditionnelles (30 min)

#### Théorie (10 min)

* Rappel syntaxe :

```python
temp = 36.5
if temp > 37.5:
    print("Fièvre")
elif temp < 35.5:
    print("Hypothermie")
else:
    print("Température normale")
```

* Opérateurs de comparaison : `==`, `!=`, `<`, `>`, `<=`, `>=`
* Opérateurs logiques : `and`, `or`, `not`

#### Exemples scientifiques (10 min)

* **Physique : vitesse et seuil de dépassement**

```python
vitesse = 120
if vitesse > 100:
    print("Dépassement de vitesse")
else:
    print("Vitesse acceptable")
```

* **Chimie : pH d’une solution**

```python
pH = 3
if pH < 7:
    print("Solution acide")
elif pH > 7:
    print("Solution basique")
else:
    print("Solution neutre")
```

#### Exercices guidés (10 min)

> Les étudiants partagent leurs réponses via chat ou vocalement, ou écrivent dans le notebook partagé.

1. Un corps a une température de 39,5 °C. Déterminez son état.
2. Un étudiant obtient 82 % à un test. Catégorisez la performance :

   * < 60 : échec
   * 60–69 : passable
   * 70–84 : bien
   * 85 et + : excellent

---

### 2. Introduction aux boucles (30 min)

#### Théorie (10 min)

* **Boucle `while`**

```python
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1
```

* **Boucle `for` avec `range()`**

```python
for i in range(5):
    print(i)
```

#### Applications simples (10 min)

* **Biologie : répétition de cycles cellulaires**

```python
cycles = 3
for cycle in range(cycles):
    print(f"Cycle {cycle+1}: réplication de l’ADN")
```

* **Chimie : simulation de gouttes de solution**

```python
gouttes = 0
while gouttes < 10:
    print("Ajout d'une goutte")
    gouttes += 1
```

#### Exercices guidés (10 min)

1. Affichez les entiers pairs de 2 à 10.
2. Simulez la décroissance radioactive sur 5 étapes (texte seulement).
3. Demandez à l’utilisateur un nombre, puis affichez tous les entiers jusqu’à ce nombre.

---

### 3. Activité d’intégration (20 min)

> Problème à résoudre en petits groupes (ou seul si le groupe est petit) puis discussion en plénière.

**Énoncé :**

> Un étudiant mesure le pH de plusieurs solutions. Écrivez un programme qui :
>
> * Demande à l’utilisateur combien de solutions il veut tester.
> * Pour chaque solution, demande le pH.
> * Affiche si chaque solution est acide, basique ou neutre.

*Bonus : compter combien de solutions sont acides, basiques ou neutres.*

---

### 4. Retour et questions (10 min)

* Retour sur les concepts clés
* Répondre aux questions
* Partage du code final et de ressources supplémentaires (site Python Tutor, W3Schools, exercices sur [exercicespython.fr](https://exercicespython.fr))

---

## Matériel à préparer

* Un notebook Google Colab (ou fichier Jupyter) avec :

  * Sections de code à compléter
  * Exemples illustrés
  * Cases de texte pour consignes
* Lien de partage en mode "commentaire" ou "édition"