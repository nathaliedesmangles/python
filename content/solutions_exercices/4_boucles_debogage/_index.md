+++

title = "A FAIRE 4-boucles et débogage simple"

weight = 204

+++





\### Exercice 1 - For ou While ?



Pour chacun des contextes suivants, avant d'écrire le code, répondez à la question: "Quelle boucle devriez-vous utiliser ?":



a. Afficher les nombres de 1 à 10  

b. Compter jusqu’à 100 par bonds de 10  

c. Simuler la chute d’un objet de 100 m (baisse de 10 m/s)  

d. Lire une température jusqu’à ce qu’elle soit < 0 (entrée utilisateur)  

e. Écrire un programme qui demande à l'utilisateur d'entrer un chiffre (1 à 10). Tant qu'il ne tape pas le chiffre `0`, le programme lui redemande d'entrer un chiffre (1 à 10) Sinon (i.e. il a tapé `0`) le programme s'arrête (Vous pouvez utiliser `break` et afficher un message).  





\### Exercice 2  – Table de multiplication



\* Écrire un programme qui affiche la table de multiplication d’un nombre donné par l’usager (entre 1 et 12), jusqu’à 12 × ce nombre.

\* utiliser une boucle `while` pour refaire une autre table tant que l’usager le souhaite.



\*\*Exemple de sortie :\*\*

```

Entrez un nombre entre 1 et 12 : 7

1 x 7 = 7

2 x 7 = 14

3 x 7 = 21

...

12 x 7 = 84

```



\### Exercice 3 – Utiliser `while` pour atteindre un objectif



Une température initiale est de 20 °C. Chaque heure, elle augmente de 1,5 °C.

Écrire un programme qui affiche l’évolution de la température \*\*jusqu’à ce qu’elle atteigne 30 °C\*\*.



1\. Crée une variable `temp` avec 20 comme valeur initiale.

2\. Utilise une boucle `while` pour vérifier si `temp` est inférieure à 30.

3\. À chaque tour, affiche la température.

4\. Augmente la température de 1.5.





\### Exercice 4 – Répéter une mesure fixe avec `for`



On veut afficher les numéros de 10 échantillons : `Échantillon 1`, `Échantillon 2`, ..., `Échantillon 10`.



1\. Utilise une boucle `for` avec `range(1, 11)`.

2\. À chaque tour, affiche `Échantillon` suivi du numéro.





\### Exercice 5 - Trouver les erreurs !



Corrige les erreurs dans ce programme pour qu’il fonctionne :



```python

nom = input("Quel est ton nom?")

print("Bonjour", name)



age = input("Quel âge as-tu?")

print("Dans 10 ans, tu auras" age + 10)

```



