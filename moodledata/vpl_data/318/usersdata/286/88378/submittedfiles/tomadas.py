# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI

while (True) :

    t1 = int(input("Quantas tomadas tem a régua 1? "))

    if t1>1 :
        break
    else:
        print("\nVerifique se digitou o número de tomadas certo.\n")
        
while (True) :

    t2 = int(input("Quantas tomadas tem a régua 2? "))

    if t2>1 :
        break
    else:
        print("\nVerifique se digitou o número de tomadas certo.\n")
        
while (True) :

    t3 = int(input("Quantas tomadas tem a régua 3? "))

    if t3>1 :
        break
    else:
        print("\nVerifique se digitou o número de tomadas certo.\n")
        
while (True) :

    t4 = int(input("Quantas tomadas tem a régua 4? "))

    if t4>1 :
        break
    else:
        print("\nVerifique se digitou o número de tomadas certo.\n")
        
t = t1+t2+t3+t4-3

print("%i" % t)