# -*- coding: utf-8 -*-
from __future__ import division
#Entrada
a=int(input('insira o valor da primeira moeda:'))
b=int(input('insira o valor da segunda moeda:'))
c=int(input('insira o valor da nota:'))
qa=0
qb=0
cont=0


#Processamento
while qa<c//a:
    qb=(c=qa*a)//b
    if qa*a+qb*b==c:
        cont+=1
        break
    else:
        qa+=1
if cont>0:
    print qa
    print qb
else:
    print ('N')