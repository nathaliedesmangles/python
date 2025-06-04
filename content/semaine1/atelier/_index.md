+++
title = "Activité 1 – Questionnaire + Mini-lab en équipe"
weight = 14
+++

## Objectifs pédagogiques

* Identifier les connaissances préalables et les attentes des étudiants.
* Favoriser une première collaboration en équipe.
* Prendre contact avec l’environnement de développement (Anaconda et Jupyter Notebook).
* Manipuler des notions de base : variables, types de données, opérations simples.

---

## Questionnaire de départ (~15 minutes)

Répondre **individuellement** aux questions du quiz [Apprendre à se connaitre](https://forms.office.com/r/xCsCbJTy4e?origin=lprLink)

**Suivi** (~5 minutes) : 
1. Discussion en petits groupes (3-4 étudiants)
2. Mise en commun de quelques idées (question #9) à l’oral.

## Mini-lab – Découverte de Python (~1 h 30)

**En équipe** : 2 ou 3 étudiants

**Objectifs :**

* Comprendre la structure d’un script Python dans Jupyter
* Modifier des cellules et exécuter du code
* Manipuler des variables et des opérations de base
* Discuter et s’entraider au sein de l’équipe

**Titre :** Une calculatrice scientifique de base

**Matériel :**

* Jupyter Notebook prêt à remplir (Sur Moodle)
* Contient des cellules à compléter avec des instructions simples

<!--
* L’enseignante passe dans les équipes pour observer l’interaction et répondre aux questions.
-->

{{% notice style="green" title="Contenu du mini-lab" groupid="notice-toggle" expanded="false" %}}

```python
# Cellule 1 : Affiche ton nom et ton programme d’études
print("Nom : _______ - Programme : Sciences de la nature")

# Cellule 2 : Déclare une variable pour ta masse (en kg) et une pour la gravité (9.8 m/s^2)
masse = ___
gravite = 9.8

# Cellule 3 : Calcule ton poids en Newton
poids = masse * gravite
print("Ton poids sur Terre est :", poids, "N")

# Cellule 4 : Calcule la valeur d’une expression scientifique, par exemple : énergie cinétique
vitesse = 3.0  # m/s
energie = 0.5 * masse * vitesse ** 2
print("Énergie cinétique : ", energie, "J")
```
{{% /notice %}}


## Retour en groupe (~10 minutes)

* Discussion : qu’avez-vous appris aujourd’hui?
* Quels éléments vous ont surpris ou intéressés?


[Le notebook `.ipynb`](./Mini-lab1_Introduction_Python.ipynb)
