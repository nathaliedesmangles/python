#!/bin/bash

# Boucle sur les semaines de 1 à 15
for i in {1..15}; do
    # Définition du chemin du fichier _index.md
    FILE="content/semaine$i/atelier/_index.md"
    
    # Vérifier si le fichier existe
    if [ -f "$FILE" ]; then
        echo "Modification de $FILE"
        # Ajouter le contenu au début du fichier (en le réécrivant)
        { 
            echo "+++"
            echo "title = \"ATELIER #$i: Titre\""
            echo "weight = $((i * 2))"
            echo "+++"
            echo ""
            echo "## Objectif de l'atelier"
            echo ""
            echo "Cet atelier a pour but de vous familiariser avec ."
            echo ""
            echo "# Atelier"
            echo ""
            echo "## Exercice 1 : Titre"
            echo ""
            cat "$FILE"
        } > "$FILE.tmp" && mv "$FILE.tmp" "$FILE"
    else
        echo "Fichier $FILE introuvable, passage à la semaine suivante."
    fi
done

echo "Mise à jour terminée."
