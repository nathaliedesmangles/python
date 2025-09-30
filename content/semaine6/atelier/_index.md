+++
title = "Atelier - Version pas à pas"
weight = 106.1
+++


## Exercice 

Un chercheur a mesuré la **température moyenne (°C)** de quatre villes pendant une semaine. Les données sont regroupées dans une **liste de listes**. Vous devez analyser et représenter ces données.


### 1. **Les données**

* Créez une liste `temperatures` contenant les valeurs suivantes (une sous-liste par ville) :

	* Ville A : `[15, 16, 14, 14, 17, 18, 19]`
	* Ville B : `[22, 23, 21, 20, 24, 25, 26]`
	* Ville C : `[5, 7, 6, 6, 8, 9, 7]`
	* Ville D : `[10, 11, 12, 10, 13, 14, 15]`

* Créez aussi deux listes :

	* `villes = ["Ville A", "Ville B", "Ville C", "Ville D"]`
	* `jours = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]`


### 2. **Afficher les températures**

* À l’aide de **boucles imbriquées**, affichez les températures de chaque ville.

* Exemple attendu :

 ```
 Ville A : 15 16 14 14 17 18 19
 Ville B : 22 23 21 20 24 25 26
 ...
 ```


### 3. **Trouver les valeurs extrêmes**

**Étape 3a.** Prenez seulement la liste des températures de Ville A.

	* Utilisez `max()` pour trouver la température la plus élevée.
	* Utilisez `min()` pour trouver la température la plus basse.
	* Affichez les résultats avec des phrases complètes.

**Étape 3b.** Répétez la même chose manuellement pour Ville B, puis Ville C.

**Étape 3c.** Quand cela fonctionne, mettez le tout dans une **boucle** sur toutes les villes.

* Exemple :

 ```
 La température maximale de Ville A est 19 C
 La température minimale de Ville A est 14 C
 ```

### 4. **Classer les températures (pas à pas)**

**Étape 4a.** Prenez une température seule (par exemple `15`) et écrivez un `if / elif / else` qui affiche :

	* "Froide" si T < 10
	* "Douce" si 10 ≤ T ≤ 20
	* "Chaud" si T > 20

**Étape 4b.** Testez votre code avec plusieurs valeurs (7, 15, 23…).

**Étape 4c.** Appliquez maintenant ce code à **toutes les températures d’une seule ville** (par exemple Ville A).

* Affichez sous forme :

 ```
 Classification pour Ville A :
 15 => Douce
 16 => Douce
 ...
 ```


**Étape 4d.** Mettez le tout dans une boucle pour traiter toutes les villes.


### 5. **Tracer un graphique avec matplotlib**

* Utilisez une boucle pour tracer la courbe des températures de chaque ville (`plt.plot`).
* Ajoutez :

	* Un **titre** : `"Températures hebdomadaires"`
	* Les étiquettes des axes (`xlabel`, `ylabel`)
	* Une **grille** (`grid`)
	* Une **légende** (`legend`)

* Sauvegardez le graphique dans un fichier `"temperatures.png"` (`savefig`)
* Affichez-le (`show`).







