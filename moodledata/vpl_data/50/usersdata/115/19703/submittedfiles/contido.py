# -*- coding: utf-8 -*-
from __future__ import division

def contagem_igual(a,b):
    c=0
    for i in range(0,len(a),1):
        for h in range(0,len(b),1):
            if (a[i]==b[h]):
                c=c+1
    return c
def colocar_numero(lista,n):
    for i in range(0,n,1):
        lista.append(input('insira o elemento:'))
    return lista
n1=input('quantidade de elementos presentes em a:')
n2=input('quantidade de elementos presentes em b:')
a=[]
b=[]
print('preencha a')
a=colocar_numero(a,n1)
print('preencha b')
b=colocar_numero(b,n2)
c=contagem_igual(a,b)
print(c)