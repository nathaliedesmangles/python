+++
pre = "**7.**"
title = " Listes, chaines de caractères et graphiques de base"
weight = 207
draft = true
+++





\## Exercice 4 Transférer dans S7 Listes



But : simuler un test qui s’arrête dès qu’il y a une mauvaise réponse



```python

\# On suppose que les bonnes réponses sont "A"

\# et que l'étudiant fait une erreur à la 4e question



reponses = \["A", "A", "A", "B", "A", "A", "A", "A", "A", "A"]







for i in range(10):



\&nbsp;   print("Question", i + 1)



\&nbsp;   if reponses\[i] != "A":



\&nbsp;       print("Réponse incorrecte. Test terminé.")



\&nbsp;       break



\&nbsp;   else:



\&nbsp;       print("Bonne réponse.")



```







\### Ce que ça fait :







\* Affiche les 3 premières bonnes réponses.



\* À la 4e question, la réponse est fausse → le test s’arrête avec `break`.

