# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import random
def Sorteio():
    k=range(1,1000000001)
    n=random.choice(k)
    print(n)
    if n%2==0:
        return "Humano"
    else:
        return "Computador"
