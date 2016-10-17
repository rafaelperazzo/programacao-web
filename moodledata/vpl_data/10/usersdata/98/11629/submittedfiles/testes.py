# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
n=input('Digite o valor de n: ')
i=input('Digite o valor de i: ')
j=input('Digite o valor de j: ')
cont=0
a=0
while True:
    if a%i==0 or a%j==0:
        print(a)
        cont=cont+1
    a=a+1
    
    if cont==n:
        break
    
    