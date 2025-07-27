+++
chapter = true
pre = "<b>6.</b>"
title = " Répéter avec la boucle `for`"
weight = 106
draft = false
+++

## Objectifs

* Savoir identifier quand utiliser une boucle `for` vs. `while`.
* Savoir écrire des boucles `for` et `while`.

---


## La boucle `for` avec `range()`

Utilisée quand **on connaît d’avance** combien de fois répéter.

### Syntaxe :

```python
for i in range(début, fin, pas):
    instructions
```

* `début` : valeur initiale (optionnel, par défaut = 0)
* `fin` : valeur **non incluse**
* `pas` : saut entre chaque valeur (optionnel, par défaut = 1)

**Exemple** :

```python
for i in range(0, 5):
    print("i =", i)
```

> Affiche les valeurs de 0 à 4.



{{% notice style="blue" title="À retenir" groupid="notice-toggle" expanded="false" %}}
* `for` avec `range()` : Utilisée lorsque le nombre de répétitions est connu d'avance.  
   * Équivaut à dire:  
      * **POUR CHAQUE** *tour de boucle* **FAIRE...** ou
      * **POUR CHAQUE** *valeur d'une séquence* **FAIRE...**
{{% /notice %}}


---

## Exercices à faire avant le cours

[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_boucles.ipynb)

### Exercice 1 - For ou While ?

Pour chacun des contextes suivants, avant d'écrire le code, répondez à la question: "Quelle boucle devriez-vous utiliser ?":

a. Afficher les nombres de 1 à 10  
b. Compter jusqu’à 100 par bonds de 10  
c. Simuler la chute d’un objet de 100 m (baisse de 10 m/s)  
d. Lire une température jusqu’à ce qu’elle soit < 0 (entrée utilisateur)  
e. Écrire un programme qui :  
&nbsp;&nbsp;&nbsp;&nbsp; i. Affiche deux choix :  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. "Entrez votre prénom"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2."Quitter le programme"  
&nbsp;&nbsp;&nbsp;&nbsp; ii. Demande à l'utilisateur d'entrer son choix (`1` ou `2`) et tant qu'il choisi l'option 1, le programme lui redemande d'entrer son prénom. Si c'est 2, le programme s'arrête (Vous pouvez utiliser `break` ou afficher un message).  


### Exercice 2 – Utiliser `while` pour atteindre un objectif

Une température initiale est de 20 °C. Chaque heure, elle augmente de 1,5 °C.
Écrire un programme qui affiche l’évolution de la température **jusqu’à ce qu’elle atteigne 30 °C**.

1. Crée une variable `temp` avec 20 comme valeur initiale.
2. Utilise une boucle `while` pour vérifier si `temp` est inférieure à 30.
3. À chaque tour, affiche la température.
4. Augmente la température de 1.5.


### Exercice 3 – Répéter une mesure fixe avec `for`

On veut afficher les numéros de 10 échantillons : `Échantillon 1`, `Échantillon 2`, ..., `Échantillon 10`.

1. Utilise une boucle `for` avec `range(1, 11)`.
2. À chaque tour, affiche `Échantillon` suivi du numéro.

---

## À faire avant le prochain cours

1. Lire la matière sur [Listes, chaines et graphiques de base](../semaine7/)
2. Faire les [exercices se trouvant à la fin de la leçon 7](../semaine7/#exercices-à-faire-avant-le-cours)
