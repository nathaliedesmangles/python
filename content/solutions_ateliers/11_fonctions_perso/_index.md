+++
pre = "<b>11.</b>"
title = " Fonctions personnalisées"
weight = 311
draft = false
+++


## Exercice : Calcul de dilution (C₁V₁ = C₂V₂)

```python
def lire_donnees():
    """
    Lit les données nécessaires au calcul d’une dilution.

    Cette fonction demande à l’utilisateur :
      - la concentration de la solution mère (C1, en mol/L),
      - la concentration finale souhaitée (C2, en mol/L),
      - le volume final de la solution (V2, en L).

    Returns:
        tuple: Un triplet (C1, C2, V2) contenant les valeurs saisies par l’utilisateur.

    Exemple :
        >>> C1, C2, V2 = lire_donnees()
        --- Programme de dilution ---
        Concentration de la solution mère (mol/L) : 1.0
        Concentration finale souhaitée (mol/L) : 0.2
        Volume final de la solution (L) : 0.5
        # Retourne (1.0, 0.2, 0.5)
    """

    print("--- Programme de dilution ---")
    C1 = float(input("Concentration de la solution mère (mol/L) : "))
    C2 = float(input("Concentration finale souhaitée (mol/L) : "))
    V2 = float(input("Volume final de la solution (L) : "))
    return C1, C2, V2


def calculer_v1(C1, C2, V2):
    """
    Calcule le volume de solution mère à prélever pour réaliser une dilution.

    Utilise la formule : V1 = (C2 × V2) / C1

    Args:
        C1 (float): Concentration de la solution mère (mol/L).
        C2 (float): Concentration finale souhaitée (mol/L).
        V2 (float): Volume final de la solution (L).

    Returns:
        float: Le volume de solution mère à prélever (V1, en L).

    Exemple :
        >>> calculer_v1(1.0, 0.2, 0.5)
        0.1
    """

    V1 = (C2 * V2) / C1
    return V1


def afficher_resultat(V1):
    """
    Affiche le volume de solution mère à prélever.

    La valeur est arrondie à deux décimales pour plus de clarté.

    Args:
        V1 (float): Volume calculé de solution mère à prélever (en L).

    Affiche :
        Un message indiquant le volume nécessaire pour préparer la solution diluée.

    Exemple :
        >>> afficher_resultat(0.1)
        Il faut prélever 0.1 L de solution mère pour préparer la solution diluée.
    """

    V1_arrondi = round(V1, 2)
    print(f"Il faut prélever {V1_arrondi} L de solution mère pour préparer la solution diluée.")


# Programme principal

# Étape 1 : Lire les données
C1, C2, V2 = lire_donnees()
    
# Étape 2 : Calculer le volume à prélever
V1 = calculer_v1(C1, C2, V2)
    
# Étape 3 : Afficher le résultat
afficher_resultat(V1)
```


## Exemple de sortie (si l’utilisateur entre 2.0, 0.5, 1.0) :

```
--- Programme de dilution ---
Concentration de la solution mère (mol/L) : 2.0
Concentration finale souhaitée (mol/L) : 0.5
Volume final de la solution (L) : 1.0
Il faut prélever 0.25 L de solution mère pour préparer la solution diluée.
```