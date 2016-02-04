# coding=utf-8
import matplotlib.pyplot as plt
from scipy.special import binom
import math
import numpy as np
from pprint import pprint


"""

Deuxième Partie

L'expérience désigne la pièce !!

Hdelta(x) = log2 (|Sdelta|)

"""
N = 20
delta = np.arange(0, 1, 0.01)
p = 0.1 # Proba d'avoir un 1.

# On doit calculer delta, delta = P(x € Sdelta) >= 1 - delta
#There is a built-in command binomcdf (binomial cumulative density function) that can be used to quickly determine "at most".

res = []

for d in delta :
    r = N - 1 # Quand r = N -> La proba d'avoir des 1 est de 1, donc c'est useless
    prob = binom.cdf(r, N, p)
    while prob > 1 - d and r > 1 :
        r -= 1
        prob = binom.cdf(r, N, p)
    r += 1 #On incrémente le r car on s'arrête une fois que la proba n'est plus > 1 - d et du coup il faut prendre le r précédent.

    
