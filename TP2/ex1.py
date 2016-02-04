# -*- coding: utf-8 -*-
import string
import codecs
from pprint import pprint
import math
import re 

def encode(msg, key):
    """
    Encode a message with a substitution cipher.
    Parameters
    ----------
    - msg, a string
    the message to encode
    - key, a string of 27 characters
    the i-the character of the alphabet is replaced by the i-th
    character of the key
    """
    key = key + key.upper()
    return msg.translate(msg.maketrans(string.ascii_letters, key))


# simple shift cipher
text = "I’m sorry Dave, I’m afraid I can’t do that"
key = string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
print(encode(text, key))


def probaNGram(file_name) :
    dico1Gram = {}
    dico2Gram = {}
    
    with codecs.open(file_name, "r", encoding="utf8") as myfile:
        countTotal = 0
        
        for line in myfile:
            line = line.strip() #Remove the \n
            mots = line.split()
            if len(mots) == 2 :
                #On a un 1-gram
                mot = mots[0]
                count = int(mots[1])
                if mot not in dico1Gram :
                    dico1Gram[mot] = count
                    countTotal += count
                    
            elif len(mots) == 3 :
                mot = mots[0]
                mot2 = mots[1]
                count = int(mots[2])
                if mot not in dico2Gram :
                    dico2Gram[mot] = {mot2 : count}
                else :
                    dico2Gram[mot][mot2] = count
                                    
    if len(mots) == 2 :
        for mot in dico1Gram :
            dico1Gram[mot] /= countTotal
        return dico1Gram
    else :
        for mot in dico2Gram :
            sumN = sum(dico2Gram[mot].values())
            for mot2 in dico2Gram[mot] :
                dico2Gram[mot][mot2] /= sumN
        return dico2Gram

    
    

result1 = probaNGram("./count_1w.txt")
result2 = probaNGram("./count_2w.txt")
                

'''
Question 2 : Il faut faire le produit des probabilités
'''

# Question 3
text1 = "I love probabilities very much"
text2 = "I love probabilities " + "very " * 100 + "much"
text3 = "I ’m sorry Dave, I’m afraid I can’t do that."
text4 = "fbeel Qnir"


def proba3_1gram(phrase):

    motsReplace = phrase.replace(",", " ,").replace(".", " .").replace("!", " !").replace("?", " ?").lower().split()
    res = 1.0

    for word in motsReplace :
        if word in result1 :
            res *= math.log10(float(result1[word]))
            #res *= float(result1[word])
        else :
            result1[word] = 1.0 /len(result1) #   1 / N où N = taille du vocabulaire
            res *= math.log10(float(result1[word]))

    return res

#print("1-gram || 1ere phrase", proba3_1gram(text1))
#print("1-gram || 2eme phrase", proba3_1gram(text2))
#print("1-gram || 3eme phrase", proba3_1gram(text3))
#print("1-gram || 4eme phrase", proba3_1gram(text4))

def proba3_2gram(phrase) :
    motsReplace = phrase.replace(",", " ,").replace(".", " .").replace("!", " !").replace("?", " ?").lower().split()

    #motsReplace = re.split(r'[,;?!\']+', phrase)

    #Mot précédent
    historique = motsReplace[0]
    # On calcul la proba du mot
    if historique in result1.values() : 
        res = result1[historique]
    else :
        result1[historique] = 1.0 / len(result1)
        res = result1[historique]
    for word in motsReplace[1:] :
        if historique in result2 :
            if word in result2[historique] : 
                #On multiplie par la proba du mot suivi par le mot précédent
#                res *= math.log10(result2[historique][word])
                #                print("res = ", res)
                res *= result2[historique][word]
                
                historique = word
            else :
                result2[historique][word] = 1.0 / len(result2[historique]) #On fait un lissage, on a donc 1 / N si jamais on a jamais vu le 2ème mot 
                #res *= math.log10(result2[historique][word])
                res *= result2[historique][word]
        else :
            result2[historique] = {}
            
            # On refait un lissage mais cette fois on le fait si on n'a jamais vu le 1er mot dans le dico, dans ce cas, la proba de voir le 2nd mot à la suite du 1er mot est de 1 car c'est le 1er mot que l'on voit
#            result2[historique][result1[word]]
            result2[historique][word] = 1.0
            
            #res *= math.log10(result2[historique][word])
                
            res *= result2[historique][word]
        
    return res


#print("2-gram, text1", proba3_2gram(text1))
#print("2-gram || 100 fois le même mot", proba3_2gram(text2))

#print("result2 avec and & union", result2 ["and"]["union"])
#print("2-gram", proba3_2gram("trade and union"))


def decode(sentence) :
    probaMax = 0
    
    return proba3_2gram(sentence)

print(decode("V'z fbeel Qnir, V'z nsenvq V pna'g qb gung"))


