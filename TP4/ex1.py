# coding=utf-8
from __future__ import division
from pprint import pprint
import nltk


phrase = "abcdbdcabcdadddddddddd"



def proba(phrase) :
    dic = nltk.FreqDist(phrase)
    for elt in dic :
        dic[elt] /= len(phrase)
    return dic


pprint(proba(phrase))


