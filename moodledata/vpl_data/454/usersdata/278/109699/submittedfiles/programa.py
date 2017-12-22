# -*- coding: utf-8 -*-
cont=0
C = int(input('Digite o número de consultas ao estoque: '))
for i in range (0,C,1):
    lista=[]
    lista.append('Digite a medida do taco%.d: ' %(i+1)
for i in range (0,C,1):
    if i+1<C:
        if lista[i]!=lista[i+1]:
            continue
        if lista[i]==lista[i+1]:
            cont+=2
    else:
        break
print(cont)
