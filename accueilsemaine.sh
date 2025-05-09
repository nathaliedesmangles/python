#!/bin/bash

# Boucle sur les semaines de 1 à 15
for i in {6..15}; do
    # Définition du chemin du fichier _index.md
    FILE="content/semaine$i/_index.md"
    
    # Vérifier si le fichier existe
    if [ -f "$FILE" ]; then
        echo "Modification de $FILE"
        # Ajouter le contenu au début du fichier (en le réécrivant)
        { 
            echo "+++"
            echo "chapter = true"
            echo "pre = \"<b>Semaine $i.</b>\""
            echo "title = \"Titre$i\""
            echo "weight = $i0"
            echo "+++"
            cat "$FILE"
        } > "$FILE.tmp" && mv "$FILE.tmp" "$FILE"
    else
        echo "Fichier $FILE introuvable, passage à la semaine suivante."
    fi
done

echo "Mise à jour terminée."
