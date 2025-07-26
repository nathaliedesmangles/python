+++
pre = "**9.**"
title = " Tableaux NumPy"
weight = 209
+++





\## Exercice 1 – Solubilité d’un sel



\*\*Données\*\* :



```python

import numpy as np



sol = np.array(\[32.0, 35.5, np.nan, 37.2, 39.0])

```



\### 1. Affiche les valeurs



```python

print(f"Solubilités : {sol}")

```



\### 2. Moyenne sans la valeur manquante



```python

moyenne = np.nanmean(sol)

print(f"Moyenne (sans valeur manquante) : {moyenne:.2f} g/100mL")

```



\### 3. Écart type



```python

ecart = np.nanstd(sol)

print(f"Écart type : {ecart:.2f}")

```





\## Exercice 2 – Températures journalières



\*\*Données\*\* :



```python

temperatures = np.array(\[

&nbsp;   \[12.1, 17.3, 14.2],

&nbsp;   \[11.8, 16.9, 13.9],

&nbsp;   \[13.0, 18.1, 15.0],

&nbsp;   \[12.5, 17.5, 14.7],

&nbsp;   \[np.nan, 16.0, 14.0],

&nbsp;   \[13.2, 18.0, 15.2],

&nbsp;   \[12.0, 17.0, 14.5]

])

```



\### 1. Forme du tableau



```python

print(temperatures.shape)  # (7, 3)

```



\### 2. Moyenne journalière



```python

moyennes\_journalieres = np.nanmean(temperatures, axis=1)

print(f"Moyennes par jour : {moyennes\_journalieres}")

```



\### 3. Moyenne du matin (colonne 0)



```python

moy\_matin = np.nanmean(temperatures\[:, 0])

print(f"Moyenne du matin : {moy\_matin:.2f} °C")

```





\## Exercice 3 – Analyse d’ADN



\*\*Données\*\* :



```python

ech1 = np.array(\[3.2, 2.8, 4.1, 3.9, 2.5])

ech2 = np.array(\[2.9, 3.0, 4.2, 4.0, 2.7])

```



\### 1. Profil combiné



```python

profil = ech1 + ech2

print(f"Profil combiné : {profil}")

```





\### 2. Différence



```python

diff = ech2 - ech1

print(f"Différences (éch2 - éch1) : {diff}")

```





\### 3. Moyenne et écart type



```python

print(f"Moyenne éch1 : {np.mean(ech1):.2f}")

print(f"Écart type éch1 : {np.std(ech1):.2f}")



print(f"Moyenne éch2 : {np.mean(ech2):.2f}")

print(f"Écart type éch2 : {np.std(ech2):.2f}")

```





\## Exercice 4 – Pression dans un cylindre



\*\*Données\*\* :



```python

hauteur = np.linspace(0, 50, 6)  # \[0, 10, 20, 30, 40, 50]

pression = np.array(\[101.3, 100.0, 98.7, 97.5, 96.2, 95.0])

```



\### 1. Affichage



```python

print("Hauteurs :", hauteur)

print("Pressions :", pression)

```



\### 2. Variation de pression



```python

variations = pression\[:-1] - pression\[1:]

print(f"Chutes de pression entre tranches de 10 cm : {variations}")

```



\### 3. Moyenne



```python

print(f"Moyenne des pressions : {np.mean(pression):.2f} kPa")

```





\## Exercice 5 – Croissance d’une plante



\### 1. Taille pendant 10 jours, départ à 5 cm



```python

jours = np.arange(10)

taille = 5 + jours \* 2

print(f"Taille sans engrais : {taille}")

```



\### 2. Ajout de 1 cm par jour (engrais)



```python

taille\_engrais = taille + 1

print(f"Taille avec engrais : {taille\_engrais}")

```



\### 3. Moyennes



```python

print(f"Moyenne sans engrais : {np.mean(taille):.2f} cm")

print(f"Moyenne avec engrais : {np.mean(taille\_engrais):.2f} cm")

```

