# -*- coding: utf-8 -*-
#COMECE AQUI ABAIX
import random
k=range(1,1000000001)
n=random.choice(k)
cont=0
while cont==0:
    if n%2==0:
        print("Humano")
    else:
        print("Computador")
