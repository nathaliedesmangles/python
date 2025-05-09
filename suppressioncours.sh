#!/bin/bash

# Boucle sur les semaines de 1 à 15
for i in {1..15}; do
    # Définition du chemin du répertoire "cours"
    DIR="content/semaine$i/cours"
    
    # Vérifier si le répertoire existe
    if [ -d "$DIR" ]; then
        echo "Suppression du répertoire $DIR"
        rm -rf "$DIR"
    else
        echo "Répertoire $DIR introuvable, passage à la semaine suivante."
    fi
done

echo "Suppression terminée."
