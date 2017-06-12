# -*- coding: utf-8 -*-
from __future__ import division

def lecker(a):
    i=0
    cont=0
    for i in range(0,len(a),1):
        if i==0:
            if a[i]>a[i+1]:
                con=cont+1
            elif i==len(a)-1:
                if a[i]>a[i-1]:
                    cont=cont+1
            else:
                if a[i]>a[i+1] and a[i]>a[i-1]:
                    cont=cont+1
    if cont==1:
        return(True)
    else:
        return(False)

n=int(input('digite o número:'))
a=[]
for i in range(0,n,1):
    valor1=int(input('digite os elementos lista 1:'))
    a.append(valor1)
if lecker(a):
    print('Sim')
else:
    print('Não')

b=[]
for i in range(0,n,1):
    valor2=int(input('digite os elementos da lista 2:'))
    b.append(valor2)

if lecker(b):
    print('Sim')
else:
    print('Não')