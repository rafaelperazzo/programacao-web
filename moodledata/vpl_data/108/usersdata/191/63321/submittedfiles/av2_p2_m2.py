# -*- coding: utf-8 -*-
def vidas(lista,x1,x2):
    vidas=0
    for i in range(x1,x2+1,1):
        vidas=vidas+lista[i]
    return vidas
n=int(input('digite o numero de salas:'))
a=[]
for i in range(0,n,1):
    c=int(input('numero de vidas:'))
    a.append(c)
j=int(input('entrada:'))
l=int(input('saida:'))
print(vidas(a,j,l))

