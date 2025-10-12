# -*- coding: utf-8 -*-
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Séance de démonstration — NumPy\n",
    "\n",
    "*NumPy* est une bibliothèque Python pour manipuler des données numériques sous forme de **tableaux (arrays)**.\n",
    "Elle permet de faire des **calculs rapides** sur plusieurs valeurs à la fois."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 🧩 Création de tableaux"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["import numpy as np"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["### 1. Avec np.array()"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["liste = [2, 4, 6]\n",
"t = np.array(liste)\n",
"print(t)  # Résultat : [2 4 6]"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["### 2. Avec np.arange()"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["t = np.arange(0, 5, 1)\n",
"print(t)  # Résultat : [0 1 2 3 4]"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["### 3. Avec np.linspace()"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["t = np.linspace(0, 10, 5)\n",
"print(t)  # Résultat : [0.  2.5  5.  7.5 10.]"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["### 4. Avec np.ones(n) et np.zeros(n)"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["print(np.ones(4))   # [1. 1. 1. 1.]\n",
"print(np.zeros(3))  # [0. 0. 0.]"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 🧮 Fonctions mathématiques"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["t = np.array([4, 9, 16])\n",
"print(np.sqrt(t))   # Racine carrée → [2. 3. 4.]\n",
"\n",
"t = np.array([27, 64, 216])\n",
"print(np.cbrt(t))   # Racine cubique → [3. 4. 6.]\n",
"\n",
"t = np.array([0, 1, 2])\n",
"print(np.exp(t))    # Exponentielle → [1. 2.71828183 7.3890561]\n",
"\n",
"t = np.array([1, np.e, np.e**2])\n",
"print(np.log(t))    # Logarithme naturel → [0. 1. 2.]\n",
"\n",
"t = np.array([1, 2, 4, 8])\n",
"print(np.log2(t))   # Log base 2 → [0. 1. 2. 3.]\n",
"\n",
"t = np.array([1, 10, 100, 0.1])\n",
"print(np.log10(t))  # Log base 10 → [0. 1. 2. -1.]\n"]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 📊 Fonctions statistiques"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["t = np.array([3, 7, 2, 9])\n",
"print(np.sum(t))     # Somme → 21\n",
"print(np.prod(t))    # Produit → 378\n",
"print(np.max(t))     # Max → 9\n",
"print(np.min(t))     # Min → 2\n",
"\n",
"t = np.array([80, 90, 100])\n",
"print(np.mean(t))    # Moyenne → 90.0\n",
"\n",
"t = np.array([1, 2, 3, 4])\n",
"print(np.median(t))  # Médiane → 2.5\n",
"print(np.var(t))     # Variance → 1.25\n",
"print(np.std(t))     # Écart-type → 1.118..."]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 📐 Fonctions trigonométriques"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": ["angles = np.array([0, np.pi/2, np.pi])\n",
"print(np.sin(angles))  # [0. 1. 0.]\n",
"print(np.cos(angles))  # [1. 0. -1.]\n",
"print(np.tan(angles))  # [ 0.00000000e+00  1.63312394e+16 -1.22464680e-16]\n",
"\n",
"t = np.array([1, -1, 0.1])\n",
"print(np.arcsin(t))    # [ 1.57 -1.57 0.10]\n",
"print(np.arccos(t))    # [0.   3.14 1.47]\n",
"print(np.arctan(t))    # [ 0.785 -0.785 0.099]\n",
"\n",
"t = np.array([90, 180, 270, 360])\n",
"print(np.deg2rad(t))   # [1.57 3.14 4.71 6.28]\n",
"\n",
"t = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])\n",
"print(np.rad2deg(t))   # [ 90. 180. 270. 360.]\n"]
  }],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
