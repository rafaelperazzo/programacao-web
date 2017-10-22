# -*- coding: utf-8 -*-
import math

a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))

lista1=[]
k1=1
while k1<=a:
    if (a%k1)==0:
        lista=lista+[k1]
    k1=k1+1

lista2=[]
k2=1
while k2<=b:
    if (b%k2)==0:
        lista=lista+[k2]
    k2=k2+1
    
listafinal=[i for i in lista1 if i in lista2]
mdc=listafinal[len(listafinal)-1]