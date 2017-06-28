# -*- coding: utf-8 -*-
def vidas(lista,i1,i2):
    vidas=0
    for i in range(i1,i2+1,1):
        vidas=vidas+lista[i]
    return vidas
n=int(input('Digite a quantidade de salas:'))
a=[]
for i in range(0,n,1):
    x=int(input('Digite a quantidade de vidas:'))
    a.append(x)
b=int(input('Digite a sala de entrada:'))
c=int(input('Digite a sala de saída'))
print(vidas(a,b,c))
    

