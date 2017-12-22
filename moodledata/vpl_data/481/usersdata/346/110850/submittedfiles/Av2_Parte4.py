# -*- coding: utf-8 -*-

n= int(input('Digite valor de n: '))

a=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(input('Valores da matriz: '))
    a.append(linha)

cont=0
som=0
for i in range(0,n,1):
    som= som + a[i][i]
    cont +=1
    
    

 