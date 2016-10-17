# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
n=input('Digite o valor de n: ')
i=input('Digite o valor de i: ')
j=input('Digite o valor de j: ')
cont=0
a=1
while True:
    if a%i==0 and a%j==0:
        print(a)
    a=a+1
    cont=cont+1
    if cont==n:
        break
    
    