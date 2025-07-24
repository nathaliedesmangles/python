+++
pre = "<b>7.</b>"
title = " Listes, chaines de caractères et graphiques de base"
weight = 207
draft = false
+++

<!--

## Exercice 4 



But : simuler un test qui s’arrête dès qu’il y a une mauvaise réponse



```python

# On suppose que les bonnes réponses sont "A"

# et que l'étudiant fait une erreur à la 4e question



reponses = ["A", "A", "A", "B", "A", "A", "A", "A", "A", "A"]







for i in range(10):



&nbsp;   print("Question", i + 1)



&nbsp;   if reponses[i] != "A":



&nbsp;       print("Réponse incorrecte. Test terminé.")



&nbsp;       break



&nbsp;   else:



&nbsp;       print("Bonne réponse.")



```







### Ce que ça fait :







* Affiche les 3 premières bonnes réponses.



* À la 4e question, la réponse est fausse → le test s’arrête avec `break`.

-->
## Graphiques

### Exercice 7

### Exercice 8 Solution :

```python
import matplotlib.pyplot as plt

temp = [10, 20, 30, 40, 50]
attendu = [2.1, 3.8, 5.6, 7.3, 9.0]
mesure =  [2.0, 3.9, 5.2, 7.5, 8.8]

# Tracé des valeurs attendues (ligne)
plt.plot(temp, attendu, "o-k", label="Valeurs attendues")

# Tracé des valeurs mesurées (barres)
plt.bar(temp, mesure, width=3, alpha=0.5, label="Valeurs mesurées", color="blue")

# Mise en forme
plt.xlabel("Température (°C)")
plt.ylabel("Concentration (mg/L)")
plt.title("Concentration mesurée vs attendue")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
```