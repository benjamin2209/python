# -*- coding: utf-8 -*
import random
def temoin( a, n):
    m = n-1
    y = 1
    b = 0
    while (m != 0):
        if (m%2 == 1) :
            y = (a*y) % n
            m = m-1
        else :
             b = a
        a = (a*a) % n

        if (a==1 and b!=1 and b!=n-1) :
          # b est une racine carre non triviale de 1
          return True        # n est composé
        m = m/2

    if (y != 1) :
        return True            # n est composé
    else :
        return False
    

def millerRabin(n):
    if n < 3:
        return True
    for i in range(0, 50) :
        a = random.randint(2,n-1)
        if (temoin(a,n)) :
            return True          # n est composé
    return False             # n est probablement premier

def generateNumber(size):
    p = "2"
    while millerRabin(int(p)):
        p = ""
        for i in range(size):
            p = p + str(random.randint(0,9))
    return p