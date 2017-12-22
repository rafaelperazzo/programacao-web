# -*- coding: utf-8 -*-
n= int(input('Digite a ordem da matriz nXn: '))
c= int(input('Digite a quantidade de cidades dos itinerários: '))
while c<2:
    c= int(input('Digite a quantidade de cidades dos itinerários: '))
m=[]
l=[]
for i in range (0,n,1):
    linha=[]
    for j in range (0,n,1):
        linha.append(int(input('Digite o elemento %d: ' %(i+1))))
    m.append(linha)
for i in range (0,c,1):
    l.append(int(input('Digite o elemento %d do itinerário: ' %(i+1))))
for i in range (0,c,1):
    l[i]=i
    l[i+1]=j
    