# -*- coding: utf-8 -*-
C = int(input('Digite o número de consultas ao estoque: '))
cont=C*2
lista=[]
for i in range (0,C,1):
    lista.append(int(input('Digite a medida do taco%.d: ' %(i+1))))
for i in range (0,C,1):
    for j in range (0,C,1):
        if i==j:
            continue
        if i!=j:
            if lista[i]!=lista[j]:
                continue
            if lista[i]==lista[j]:
                cont-=1
if C==1:
    print(2)
if C!=1:
    if cont<0:
        print(cont*(-1))
    if cont>0:
        print(cont)
    
