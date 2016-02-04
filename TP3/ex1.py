# coding=utf-8
import matplotlib.pyplot as plt
from scipy.special import binom
import math
import numpy as np
from pprint import pprint


def proba(p1,r) :
    return (p1 ** r) * ((1 - p1) ** (N - r))

N = 1000
p1 = 0.1
X = np.arange(0, N)

def draw():
    plt.semilogy(proba(p1, X))
    plt.show()

#draw()


"""
Binome de Newton :

binom(N, r)

"""

def binomNewton(r) :
    return binom(N, r)


def drawBinomNewton():
    plt.semilogy(binomNewton(X))
    plt.show()


#drawBinomNewton()

def probaBinomNewton(p1, r, n) :
    return (binom(n, r) * (p1 ** r) * ((1-p1) ** (n-r)))

def drawProbaBinomNewton() :
    listProbaBinomNewton = []
    for i in range(len(X)) :
        listProbaBinomNewton.append(probaBinomNewton(p1, i))
    plt.semilogy(listProbaBinomNewton)
    plt.show()
    mean = np.mean(listProbaBinomNewton)
    var = np.var(listProbaBinomNewton)
    print("mean", mean, "var", var)

    
#drawProbaBinomNewton()

# m = N * P1
# sigma ** 2 = N * p1 * (1 - p1)

# (sigma / m) = sqrt((1- p1) / p1) * 1 / sqrt(n)


def meanDivideVariance() :
    p0 = 0.9
    meanByVariance = []
    for n in range(1, 10 ** 6) :
        meanByVariance.append(np.sqrt(n) * np.sqrt(p1/p0))

    plt.plot(meanByVariance)
    plt.show()
#    pprint(listMeanByVariance)

meanDivideVariance()    





