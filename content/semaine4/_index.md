+++
chapter = true
pre = "4."
title = " Boucles et débogage simple"
weight = 104
+++


## Objectifs

* Répéter des instructions tant qu'une condition est vraie, avec la boucle `while`.
* Répéter des instructions un nombre de fois connu d'avance avec la boucle `for`.
* Interrompre le déroulement d'une boucle.
* Comprendre les messages d'erreurs et découvrir des stratégies simples de débogage.

---

{{% notice style="accent" title="Apprendre par la pratique" %}}
- **Faites les exercices** en vous aidant des notes de cours ci-dessous.
- Certains seront fait en classe à titre de démonstration.
- Les solutions seront disponibles à la fin de la semaine prochaine.
{{% /notice %}}

# Exercices

## Fichier de départ à utiliser

1. Cliquez sur le lien pour télécharger le fichier.
[Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/exercices_boucles.ipynb)
2. Enregistrez le fichier dans votre dossier **exercices** de la semaine en cours.
3. Ouvrez **Visual Studio Code**.
4. Dans VS Code, recherchez et ouvrez le fichier `exercices_boucles.ipynb`
5. Assurez-vous que le noyau Python (`Kernel`) soit sélectionné.
6. Vous pouvez commencer à faire les exercices.

## Exercice 1 - For ou While ?

Pour chacun des contextes suivants, avant d'écrire le code, répondez à la question: "Quelle boucle devriez-vous utiliser ?":

a. Afficher les nombres de 1 à 10  
b. Compter jusqu’à 100 par bonds de 10  
c. Simuler la chute d’un objet de 100 m (baisse de 10 m/s)  
d. Lire une température jusqu’à ce qu’elle soit < 0 (entrée utilisateur)  
e. Écrire un programme qui demande à l'utilisateur d'entrer un chiffre (1 à 10). Tant qu'il ne tape pas le chiffre `0`, le programme lui redemande d'entrer un chiffre (1 à 10) Sinon (i.e. il a tapé `0`) le programme s'arrête (Vous pouvez utiliser `break` et afficher un message).  


## Exercice 2  – Table de multiplication

* Écrire un programme qui affiche la table de multiplication d’un nombre donné par l’usager (entre 1 et 12), jusqu’à 12 × ce nombre.
* utiliser une boucle `while` pour refaire une autre table tant que l’usager le souhaite.

**Exemple de sortie :**
```
Entrez un nombre entre 1 et 12 : 7
1 x 7 = 7
2 x 7 = 14
3 x 7 = 21
...
12 x 7 = 84
```

## Exercice 3 – Utiliser `while` pour atteindre un objectif

Une température initiale est de 20 °C. Chaque heure, elle augmente de 1,5 °C.
Écrire un programme qui affiche l’évolution de la température **jusqu’à ce qu’elle atteigne 30 °C**.

1. Crée une variable `temp` avec 20 comme valeur initiale.
2. Utilise une boucle `while` pour vérifier si `temp` est inférieure à 30.
3. À chaque tour, affiche la température.
4. Augmente la température de 1.5.

**Exemple de sortie** :
```
Température : 20.0 °C
Température : 21.5 °C
Température : 23.0 °C
Température : 24.5 °C
Température : 26.0 °C
Température : 27.5 °C
Température : 29.0 °C
Température : 30.5 °C
```

## Exercice 4 – Répéter une mesure fixe avec `for`

On veut afficher les numéros de 10 échantillons : `Échantillon 1`, `Échantillon 2`, ..., `Échantillon 10`.

1. Utilise une boucle `for` avec `range(1, 11)`.
2. À chaque tour, affiche `Échantillon` suivi du numéro.

**Exemple de sortie** :
```
Échantillon 1
Échantillon 2
Échantillon 3
Échantillon 4
Échantillon 5
Échantillon 6
Échantillon 7
Échantillon 8
Échantillon 9
Échantillon 10
```

## Exercice 5 - Trouver les erreurs !

Corrige les erreurs dans ce programme pour qu’il fonctionne :

```python
nom = input("Quel est ton nom?")
print("Bonjour", name)

age = input("Quel âge as-tu?")
print("Dans 10 ans, tu auras" age + 10)
```

# Cours

## À quoi servent les boucles ?

Répéter des instructions plusieurs fois, soit un nombre connu (`for`), soit jusqu’à ce qu’une condition soit atteinte (`while`).

## Boucle `while`

La boucle `while` répète un bloc **tant qu’une condition est vraie**.

```python
while condition:
    instructions
```

### Exemple :

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

{{% notice style="accent" title="Important" %}}
Il faut **modifier l'état de la condition dans la boucle** pour éviter une boucle infinie. Dans l'exemple, c'est à ça que sert l'instruction `compteur += 1`
{{% /notice %}}


### Boucle infinie

C'est lorsque la boucle ne s'arrête jamais. Cela peut arriver principalement dans deux situations:

**Cas 1**: oublier de modifier l'état de la condition

```python
temp = 100  # température initiale
while temp > 0:
    print(f"Température : {temp} °C")
    					# temp n'est pas modifié 
```

**Cas 2**: oublier de modifier l'état de la condition
```python
temp = 100  # température initiale
while temp > 0:
    print(f"Température : {temp} °C")
    temp += 10				# Erreur de logique
```

#### Arrêter une boucle infinie

> Cliquer dans la case **Arrêter l'exécution des cellules** se trouvant à gauche de la cellule contenant la boucle infinie

![Arrêt d'une boucle infinie dans VS Code Jupyter](./arret_boucle_infinie.png?width=35vw)

## Boucle `for`

La boucle `for` est idéale pour **répéter un nombre connu de fois**, ou **parcourir une séquence** (ex : liste, chaîne de caractères, `range()`).

```python
for élément in séquence:
    instructions
```

### La boucle `for` avec `range()`

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

## Interrompre une boucle

* `break` : arrête **immédiatement** la boucle.
* `continue` : saute **à l’itération suivante**.

**Exemple avec `break`** :

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

> Affiche 0 à 4. S’arrête à 5.

```python
compteur = 0
while compteur < 10:
    if compteur == 5:
        break
    print("Valeur :", compteur)
    compteur += 1
```

> Affiche : 
``` 
Valeur : 0  
Valeur : 1  
Valeur : 2  
Valeur : 3  
Valeur : 4  
```
### Exemple avec `continue`

```python
for i in range(1, 11):
    if i % 3 == 0:
        continue  # On saute les multiples de 3
    print(i)
```

> Affiche:
```
1
2
4
5
7
8
10
```

## C’est quoi un bogue?

Un **bogue** (ou bug) est une **erreur dans un programme** qui empêche le code de fonctionner comme prévu.
Il peut être :

* **syntaxique** : le programme ne se lance même pas (ex. oubli de `:` ou de parenthèse);
* **logique** : le programme fonctionne mais donne un **mauvais résultat**;
* **d’exécution** : le programme se lance mais plante en cours de route (ex. division par zéro).

## Types d’erreurs fréquentes

| Type d'erreur     | Exemple           | Message typique     |
| ----------------- | ----------------- | ------------------- |
| Syntaxe           | `if x = 5:`       | `SyntaxError`       |
| Typo              | `pritn("Hello")`  | `NameError`         |
| Zéro              | `10 / 0`          | `ZeroDivisionError` |
| Type invalide     | `int("chat")`     | `ValueError`        |
| Oubli de variable | `print(resultat)` | `NameError`         |

### Importance de l’ordre logique

* Un programme **se lit de haut en bas**.
* Une mauvaise organisation peut conduire à des **résultats erronés**.
* L’ordre : **entrée → traitement → sortie**
* Exemple courant d’erreur : utiliser une variable **avant de lui avoir donné une valeur**.

```python
# Mauvais ordre :
print(resultat)
resultat = 5 + 2
# Erreur : la variable n'existe pas encore
```

## Techniques de débogage simples

### 1. Lire les messages d’erreur

* **Que dit-il?**
* **Sur quelle ligne?**
* **Quel type d’erreur?**

Quand Python rencontre une erreur, il t’affiche un **message d’erreur**. C’est comme un indice pour t’aider.

**Exemple** :
```python
val = int(input("Donne un nombre: "))
print("Le carré est: " val * val)
```

> `SyntaxError: invalid syntax`

* Le message t’indique une **erreur de syntaxe**. Ici, il manque une **virgule** ou un `+` dans le `print`.

```python
print("Le carré est:", val * val)
```

### 2. Ajouter des `print()`

C’est ta **lampe de poche** : affiche les variables pour voir ce qui se passe.

```python
age = int(input("Âge : "))
print("DEBUG - âge reçu :", age)
if age >= 18:
    print("Majeur")
```

### 3. Tester petit à petit

N’écris pas tout d’un coup. Teste **par morceaux**.

```python
# Mauvais
# tout écrit avant de tester

# Mieux
# écrire un input → tester
# ajouter un if → tester
# ajouter un calcul → tester
```

{{% notice style="cyan" title="À retenir" groupid="notice-toggle" expanded="false" %}}
* Les boucles (`while` et `for`) permettent de **répéter des actions** efficacement.
* Il est possible d'interrompre le déroulement d'une boucle à l'aide de `break` ou `continue`.
* L’indentation est **essentielle** pour structurer le code.
* `while` : Utilisée lorsqu'une condition doit être respectée pour que la boucle s'exécute.
   * Équivaut à dire: **TANT QUE** *condition est vraie* **FAIRE...**
* `for` avec range() : Utilisée lorsque le nombre de répétitions est connu d’avance.
   * Équivaut à dire: POUR CHAQUE tour de boucle FAIRE… ou  
                      POUR CHAQUE valeur d’une séquence FAIRE…
* **Avant de commencer à coder** c'est très important de comprendre le problème afin d’identifier les variables ou constantes et les formules.
* Lorsqu'une erreur apparait, bien lire le message d'erreur, utiliser la fonction `print()``à pour suivre l’exécution d’un programme et identifier les bogues.
* Toujours “challenger” les résultats obtenus, à l’aide de différentes valeurs: “Est-ce que ça a du sens scientifiquement ?”
{{% /notice %}}

---

# Atelier

1. Téléchargez le fichier de départ : [Bloc-notes de départ](https://python-a25.netlify.app/blocnotes/atelier_boucles.ipynb)
2. Déplacez-le dans votre dossier prévu pour **l'atelier de la semaine 2**.
3. Ouvrez votre dossier de travail `programmation-sciences` **à partir de Visual Studio Code**.
   * Vous devriez voir votre structure de dossiers et vos fichiers (.ipynb).


## Exercice 1 – Réaction chimique : combien de fois?

Une réaction chimique simple a lieu entre deux réactifs A et B. À chaque cycle, 1 mL de A réagit avec 2 mL de B pour produire un précipité. Vous disposez d’un certain volume de A et de B.

Demander à l’utilisateur combien de millilitres il a de A et de B. Puis, afficher **combien de fois la réaction peut avoir lieu en entier** (sans fractions), et combien de mL de chaque réactif il reste après la dernière réaction complète.

* Utiliser une boucle `while` pour simuler la réaction répétée.
* À chaque itération, soustraire les volumes requis de A et B.
* S’arrêter lorsque l’un des réactifs n’est plus suffisant.

**Exemple d’exécution :**
```
Quantité de A disponible (en mL) : 10
Quantité de B disponible (en mL) : 25

La réaction a eu lieu 5 fois.
Il reste 0 mL de A et 15 mL de B.
```

## Exercice 2 – Détection de mutation (compteur)

Vous êtes en train d'examiner une longue série d'échantillons au microscope. Chaque échantillon peut être sain (`0`) ou muté (`1`). Vous devez saisir les résultats un à un.

Demander à l’utilisateur combien d’échantillons il va analyser. Ensuite, lui demander un à un les résultats (0 ou 1) et **compter** combien d’échantillons sont mutés. À la fin, afficher le **pourcentage d’échantillons mutés**.

* Utiliser une boucle `for` basée sur le nombre total d’échantillons.
* Demander à chaque itération : "Échantillon X : sain (0) ou muté (1)?"
* Accumuler le nombre de mutations.
* Calculer et afficher le pourcentage.

**Exemple d’exécution :**
```
Combien d’échantillons vas-tu analyser? 4
Échantillon 1 : sain (0) ou muté (1)? 0
Échantillon 2 : sain (0) ou muté (1)? 1
Échantillon 3 : sain (0) ou muté (1)? 1
Échantillon 4 : sain (0) ou muté (1)? 0

2/4 échantillons sont mutés.
Pourcentage de mutation : 50.0 %
```

---

## À faire avant le prochain cours

> **RAPPEL**: Semaine prochaine c'est le **premier examen** (20%)

1. Lire la prochaine leçon : [6. Listes, chaines et visualisation des données](../semaine6/)
2. Faire les exercices de la [prochaine leçon :](../semaine6/#exercices)

