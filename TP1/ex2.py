#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from pprint import pprint
import numpy as np
import codecs


def triplets(listW):

    res = []
    for i in range(len(listW) - 2):
        res.append((listW[i], listW[i+1], listW[i+2]))
#    pprint(res)
    
    return res

listWords = ["I", "love", "chocolate", "ice-cream", ".", "I", "really", "love", "chocolate", "ice-cream", "I", "might", "be", "addicted", "I", "might", "be", "addicted"]

#triplets(listWords)

def estimationProba(listW):
    occurences = {}

    
    for triplet in listW:
        ab = (triplet[0], triplet[1])
        c = triplet[2]
        
        #Si le triplet est dans les clés, on incrémente le compteur
        if ab not in occurences.keys() :
            occurences[ab] = {c : 1}
        else :
            if c not in occurences[ab].keys():
                occurences[ab][c] = 1
            else :
                occurences[ab][c] +=1
    
    #pprint(occurences)

    # Apres avoir calcule le nb d'occurences de chaque element, on calcule la proba que cet element soit present si il est suivi des deux autres elements le precedent.
    # Il faut egalement que la somme de toutes les proba soit 1


    proba = {}

    for ab in occurences.keys() :
        for c in occurences[ab].keys():
            if ab not in proba.keys() :
                proba[ab] = {c : occurences[ab][c] / sum(occurences[ab].values())}
                '''
                On divise par le nombre d'elements presents dans les valeurs de occurences[ab] ;
            Par exemple, on aura {"Chocolate", "ice-cream"} : {"I", 1/2", ".", 1/2} vu qu'il y a 2 elements
                '''
            else :
                proba[ab][c] = occurences[ab][c] / sum(occurences[ab].values())
#    pprint(proba)
    return proba
   
#pprint(estimationProba(triplets(listWords)))


def sample_from_discrete_distrib(distrib):
	words, probas = list(zip(*distrib.items()))
	return np.random.choice(words, p=probas)


def generation(texte):
    
    with codecs.open(texte, "r", encoding="utf8") as myfile:
        text = "".join(myfile)
        textReplace = text.replace(",", " ,").replace(".", " .").replace("?", " ?").replace("!", " !").split()
        # On appelle les deux fonctions !!!! 
        triplet = triplets(textReplace)
        proba = estimationProba(triplet)
    
        h = ('BEGIN','NOW')
        word = ""
        res = "BEGIN NOW"
        
        while not word == "END":
            if h not in proba.keys():
                break
            else :
                word = sample_from_discrete_distrib(proba[h])
                h = (h[1], word)
                res = res + " " + word
            
        return res
    
print(generation("./wine.txt"))
