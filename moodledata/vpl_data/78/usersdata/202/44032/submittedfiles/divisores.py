# -*- coding: utf-8 -*-
import math
n=int(input('digite o valor de n:'))
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
multa=0
multb=0
cont=1
while cont<n:
    if multa<multb:
        print(multa)
        multa+=a
    elif multb<multa:
         print(multb)
         multb+=b
    else: multa==multb
    print(multb)
    multa+=a
    multb+=b
    cont+=1
