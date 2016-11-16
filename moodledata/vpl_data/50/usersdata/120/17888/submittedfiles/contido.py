# -*- coding: utf-8 -*-
from __future__ import division
def contido(lista):
    cont=0
    for num in lista_b:
        for i in range(0,len(lista_a),1):
            if num==lista_a[i]:
                cont+=1
    if cont>=1: 
        return True
    else:
        return False
#entrada
a=[]
n=input('digite a quantidade de termos de a:')
for i in range(0,n,1):
    a.append(input('digite um elemento:'))
b=[]
n=input('digite a quantidade de termos de b:')
for i in range(0,n,1):
    b.append(input('digite um elemento:'))
#saida
if contido:
    print cont
else:
    print ('0')
    

    
