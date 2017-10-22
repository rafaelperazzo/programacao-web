# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI

t1 = int(input("Quantas tomadas tem a régua 1? "))
t2 = int(input("Quantas tomadas tem a régua 2? "))
t3 = int(input("Quantas tomadas tem a régua 3? "))
t4 = int(input("Quantas tomadas tem a régua 4? "))

while (t1>1) :
    while (t2>1):
        while (t3>1):
            while (t4>1) :
                n = t1+t2+t3+t4-3
            break
        break
    break

print("Vocês dispõem de %s tomadas" % n)
    



