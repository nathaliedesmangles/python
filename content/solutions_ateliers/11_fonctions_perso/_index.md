+++
pre = "<b>11.</b>"
title = " Fonctions personnalisées"
weight = 311
+++


### Exercice : Calcul de dilution (C₁V₁ = C₂V₂)

```python
# Fonction qui lit les données d'entrée (sans paramètres)
def lire_donnees():
    print("--- Programme de dilution ---")
    
    # Lecture de la concentration de la solution mère
    C1 = float(input("Concentration de la solution mère (mol/L) : "))
    
    # Lecture de la concentration finale souhaitée
    C2 = float(input("Concentration finale souhaitée (mol/L) : "))
    
    # Lecture du volume final
    V2 = float(input("Volume final de la solution (L) : "))
    
    return C1, C2, V2


# Fonction qui calcule V1 à partir de C1, C2 et V2 (avec paramètres, retourne un résultat)
def calculer_v1(C1, C2, V2):
    # Formule : V1 = (C2 × V2) / C1
    V1 = (C2 * V2) / C1
    return V1


# Fonction qui affiche le résultat (avec paramètre, ne retourne rien)
def afficher_resultat(V1):
    # Arrondi à 2 décimales
    V1_arrondi = round(V1, 2)
    print(f"Il faut prélever {V1_arrondi} L de solution mère pour préparer la solution diluée.")


# Programme principal
def main():
    # Étape 1 : Lire les données
    C1, C2, V2 = lire_donnees()
    
    # Étape 2 : Calculer le volume à prélever
    V1 = calculer_v1(C1, C2, V2)
    
    # Étape 3 : Afficher le résultat
    afficher_resultat(V1)

# Exécution du programme
main()
```

---

### Exemple de sortie (si l’utilisateur entre 2.0, 0.5, 1.0) :

```
--- Programme de dilution ---
Concentration de la solution mère (mol/L) : 2.0
Concentration finale souhaitée (mol/L) : 0.5
Volume final de la solution (L) : 1.0
Il faut prélever 0.25 L de solution mère pour préparer la solution diluée.
```