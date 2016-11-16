# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range(0,len(lista)-2,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
 n=input('Digite o valor de n:')
 a=[]
 for i in range(0,n,1):
    a.append(input('Digite um elemento:')
if crescente(a)==True:
    print('S')
else:
    print('N')




#escreva o programa principal
