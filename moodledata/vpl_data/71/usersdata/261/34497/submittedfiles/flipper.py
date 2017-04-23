# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO AQUI
def fliper():
    p = int(input("Qual a posição da primeira porta? "))
    r = int(input("Qual a posição da segunda porta? "))
    if p == 1 and r == 1:
        print ("A")
    elif p == 1 and r == 0:
        print ("B")
    if p == 0 and r == 0:
        print ("C")
    