# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
def quantidade(lista,x):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]==x:
            cont=cont+1
    return(cont)
n=int(input('digite numero de elementos da lista:'))
x=float(input('digite numero á ser inserido na lista:'))
a=[]
for i in range(0,n,1):
    numero=float(input('digite numero á ser inserido na lista:'))
    a.append(numero)
print (quantida(a,x))
