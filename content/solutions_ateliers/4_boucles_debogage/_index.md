+++
pre = "4."
title = " Boucles de débogage simple"
weight = 304
+++


## Exercice 1 : Réaction chimique

```python
# Réaction : 1 mL de A + 2 mL de B

a_dispo = int(input("Quantité de A disponible (en mL) : "))
b_dispo = int(input("Quantité de B disponible (en mL) : "))

nb_reactions = 0

while a_dispo >= 1 and b_dispo >= 2:
    a_dispo -= 1
    b_dispo -= 2
    nb_reactions += 1

print("La réaction a eu lieu", nb_reactions, "fois.")
print("Il reste", a_dispo, "mL de A et", b_dispo, "mL de B.")
```


## Exercice 2 : Détection de mutation

```python
nb_total = int(input("Combien d’échantillons vas-tu analyser? "))

nb_mutations = 0

for i in range(1, nb_total + 1):
    reponse = int(input(f"Échantillon {i} : sain (0) ou muté (1)? "))
    if reponse == 1:
        nb_mutations += 1

pourcentage = (nb_mutations / nb_total) * 100

print(f"{nb_mutations}/{nb_total} échantillons sont mutés.")
print(f"Pourcentage de mutation : {pourcentage:.1f} %")
```

