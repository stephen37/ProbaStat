import math
import random as rand
import pbm


def duplic(x,n):
    size  = len(str(x))
    x = str(x)
    dup = ""
    for i in range(0,size):
        for j in range(0,n):
            dup = dup + x[i]
    return dup


msg = duplic(110,3)
        
def canal(x,f):
    rand.seed()
    res = ""
    x = str(x)

    for element in x:
        if rand.random() > f:
            res = res + element
        else:
            if element == "0":
                res += "1"
            else:
                res += "0"
    return res

resCanal = canal(msg,0.2)


def decod(x,n):
    x = str(x)
    res  = ""
    
    i = 0

    while i < len(x):
        cpt1 = 0
        cpt0 = 0
        for j in range(i,i+n) :
            if x[j] == "0" :
                cpt0 += 1
            else :
                cpt1 += 1
        if cpt0 > cpt1 :
            res += "0"
        else :
            res += "1"
        i += n 
    return res

resDecod = decod(resCanal,3)
print("Msg initial : 110 \nMessage recu : " , resDecod)    


# Lit l'image
tab, dimX, dimY, typeImg = pbm.readpbm("./calvin.pbm")

def arrayToStr(array) :
    res = ""
    for i in array:
        res += str(i)
    return res
        
       
resArrayToStr = arrayToStr(tab)
res2 = duplic(resArrayToStr, 9)
res3 = canal(res2,0.3)
res4 = decod(res3, 9)

pbm.writepbm("./yolo.png", dimX, dimY, res4)

#duplic(tab,3)

