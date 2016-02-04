from string import ascii_letters
from pprint import pprint
from collections import Counter
from math import pow

import matplotlib.pyplot as plt

def probaLettre(size):
    size = int(size)
    text = open("./english.txt")

    
    corpus = (l.lower() for l in "".join(text))
    list_corpus = list(corpus) # On transforme corpus en List car à la base corpus est un générator et du coup on ne peut pas le parcourir à l'aide de corpus[:size]
    counts = Counter(l for l in list_corpus[:size] if l in ascii_letters)
    n = sum(counts.values())
    proba = {l: counts[l] / n for l in counts}
    pprint(proba)

    return proba['a']

#probaLettre(10**3)


def drawProba():
    x = [100,200,300, 400, 500, 750, 10**3, int(1.5*10**3), 2*10**3, 5*10**3, 8*10**3, 10**4, 5*10**4, 10**5, 10**6, 10**7, 10**8 ]

    y = []

    for i in x :
        y.append(probaLettre(i))
    plt.semilogx(x,y,"x-")
    plt.savefig("plot.png")

drawProba()

    

