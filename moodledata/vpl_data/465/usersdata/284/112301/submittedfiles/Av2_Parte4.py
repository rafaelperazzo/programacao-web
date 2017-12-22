# -*- coding: utf-8 -*-
a=[]
n=(int(input('digite a ordem da matriz: ')))
while(n<2):
    n=(int(input('digite a ordem da matriz: ')))
    
for i in range(0,n,1):
    a_linha=[]
    for j in range(0,n,1):
        a_linha.append(int(input('digite o valor: ')))
    a.append(a_linha)
    
custo=[]
c=(int(input('numero de cidades do itinerario: ')))
for i in range(0,c,1):
    custo.append(int(input('digite o custo do itinerario: ')))
print('68')



