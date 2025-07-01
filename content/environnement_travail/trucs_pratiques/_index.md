+++
title = "Trucs pratiques pour bien coder"
weight = 16
+++



Cette page rassemble une série de petits détails importants pour bien débuter en programmation. Ces astuces visent à rendre l'utilisation du clavier et de l'environnement plus fluide, surtout en contexte de cours avec Jupyter Notebook.

---

## Raccourcis clavier utiles

### Copier, couper, coller

- `Ctrl + C` : Copie la sélection. 
- `Ctrl + X` : Coupe la sélection (la sélection sera effacée, mais pourra être collée).
- `Ctrl + V` : Colle le contenu précédemment copié ou coupé.

{{%notice style="tip" title="Astuce"%}}
Si **aucun texte n’est sélectionné**, `Ctrl + C` ou `Ctrl + X` agit sur **toute la ligne courante**. Cela permet de déplacer rapidement du code sans avoir à sélectionner manuellement.
{{% /notice%}}

### Annuler et refaire

- `Ctrl + Z` : Annule la dernière action (effacement, erreur de frappe…).
- `Ctrl + Y` : Refait une action qui a été annulée (rétablir).



---

## Supprimer dans les deux directions

- `Retour arrière` (← ou Backspace) : Efface le caractère **à gauche** du curseur.
- `Suppr` (ou Delete) : Efface le caractère **à droite** du curseur.

{{%notice style="note" title="À retenir"%}}
La touche `Suppr` permet de corriger plus rapidement sans déplacer le curseur.
{{% /notice%}}

---

## Changer de fenêtre

- `Alt + Tab` : Permet de basculer rapidement d’une fenêtre ouverte à une autre (navigateur, Notebook, etc.).

{{%notice style="tip" title="Astuce"%}}
Tu peux garder `Alt` enfoncé et appuyer plusieurs fois sur `Tab` pour faire défiler les fenêtres disponibles.
{{% /notice%}}

---

## Diviser son écran de travail

Travailler avec deux fenêtres côte à côte facilite la lecture de consignes tout en codant.

### Avec le clavier :
- `Touche Windows + ←` ou `→` pour coller une fenêtre à gauche ou à droite.
- `Touche Windows + ↑` pour que la fenêtre prenne tout l'écran.
- `Touche Windows + ↓` pour décoller la fenêtre.

### Avec la souris :
- Clique sur la **barre de titre** de la fenêtre (le haut), puis **glisse-la vers le côté gauche ou droit** de l’écran. Elle s’alignera automatiquement pour occuper la moitié de l’écran.

{{%notice style="tip" title="Astuce"%}}
Tu peux ensuite sélectionner une autre fenêtre à mettre dans l’autre moitié de l’écran.
{{% /notice%}}

---

## Exécution d’un programme dans Jupyter Notebook

### Exécuter une cellule

- `Ctrl + Entrée` : Exécute la cellule actuelle, **sans passer à la suivante**.
- `Shift + Entrée` : Exécute la cellule, **puis passe à la suivante** (ou crée une nouvelle cellule si nécessaire).

{{%notice style="note" title="Différence entre les deux"%}}
- `Ctrl + Entrée` est utile pour **réexécuter plusieurs fois** une même cellule.
- `Shift + Entrée` permet d’**enchaîner l’exécution** de plusieurs cellules vers le bas.
{{% /notice%}}

---

### Arrêter un programme bloqué

Quand un programme tourne en boucle ou prend trop de temps à s’exécuter dans une cellule :

- Clique dans la cellule
- Appuie sur **le bouton "Stop" dans la barre du notebook** (généralement un carré noir)
- Ou utilise le menu `Kernel > Interrupt` ou `Interrompre`

{{%notice style="warning" title="Attention"%}}
N’essaie pas de recharger la page tout de suite : essaie d’abord d’interrompre l’exécution proprement.
{{% /notice%}}

---

## Trouver les symboles importants du clavier




En programmation, on utilise souvent des caractères spécifiques.  
Les images suivantes permettent de situer les touches pour obtenir ces carctères:


| Caractères | Emplacement sur le clavier |
|:-----------:|:----------------------------:|
| **`{ }`** | ![](images/clavier_accolade.png?width=20vw) |
| **`[ ]`** | ![](images/clavier_crochets.png?width=20vw) |
| **`:`** | ![](images/clavier_deux_points.png?width=20vw) |
| **`&`** | ![](images/clavier_eperluette.png?width=20vw) |
| **`+`** | ![](images/clavier_plus.png?width=20vw) |
| **`' '`** | ![](images/clavier_guillemets.png?width=20vw) |
| **`" "`** | ![](images/clavier_guillemets_doubles.png?width=20vw) |
| **`( )`** | ![](images/clavier_parenthese.png?width=20vw) |
| **`\|`** | ![](images/clavier_pipe.png?width=20vw) |
| **`/`** | ![](images/clavier_slash.png?width=20vw) |
| **`\`** | ![](images/clavier_backslash.png?width=20vw) |

---

## Résumé des raccourcis

| Action                              | Raccourci                | Détail                                                                 |
|-------------------------------------|--------------------------|------------------------------------------------------------------------|
| Copier                              | `Ctrl + C`               | Copie la sélection ou toute la ligne si rien n’est sélectionné        |
| Couper                              | `Ctrl + X`               | Coupe la sélection ou toute la ligne si rien n’est sélectionné        |
| Coller                              | `Ctrl + V`               | Colle le contenu copié ou coupé                                       |
| Annuler                             | `Ctrl + Z`               | Annule la dernière action                                             |
| Refaire                             | `Ctrl + Y`               | Refait une action annulée                                             |
| Supprimer à gauche                  | `Retour arrière`         | Efface le caractère précédent                                         |
| Supprimer à droite                  | `Suppr` (`Delete`)       | Efface le caractère suivant                                           |
| Changer de fenêtre                  | `Alt + Tab`              | Bascule d’une fenêtre à une autre                                     |
| Coller une fenêtre à gauche/droite | `Win + ←` / `Win + →`    | Organise les fenêtres sur l’écran                      |
| Exécuter une cellule (Jupyter)     | `Ctrl + Entrée`          | Exécute sans passer à la cellule suivante                             |
| Exécuter et avancer (Jupyter)      | `Shift + Entrée`         | Exécute et passe à la cellule suivante                                |
| Arrêter un programme               | Bouton "Stop" ou menu    | Interrompt un programme bloqué dans une cellule Notebook              |
