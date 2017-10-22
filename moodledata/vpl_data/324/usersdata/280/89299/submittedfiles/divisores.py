# -*- coding: utf-8 -*-
import math
n=int(input("Digite n: "))
a=int(input("Digite a: "))
b=int(input("Digite b: "))
cont=0
for i in range (0,10000000000000,1):
    if i%a==0 ou i%b==0:
        print i
        cont=cont + 1
        if cont=n:
            break