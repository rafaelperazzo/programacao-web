# -*- coding: utf-8 -*-
n=int(input('digite o valor da dimensão:  '))
while not n>3:
    n=int(input('digite o valor da dimensão:  '))
matriz=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite os elementos da matriz: ')))
    matriz.append(linha)
somal=[]
for i in range (0,n,1):
    somal.append(sum(matriz[i]))
somac=[]
for j in range(0,n,1):
    c=0
    for i in range)0,n,1):
        c=c+ matriz[i][j]
    somac.append(c)
b=[somal[0]]
ct=0
k=0
valorerrado=0
valorcorreto=0
for i in range(0,n,1):
    if somal[i] in b:
        continue
    else:
        ct+=1
        k=i
if ct==1:
    valorerrado=somal[k]
    valorcorreto=somal[0]
    k=0
if ct!=1:
    valorerrado=somal[0]
    valorcorreto=somal[1]
    k=0
b1=[somac[0]]
cont2=0
k1=0
valorerrado1=0

    


