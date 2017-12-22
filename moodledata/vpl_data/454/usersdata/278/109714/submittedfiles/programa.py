# -*- coding: utf-8 -*-
cont=0
C = int(input('Digite o número de consultas ao estoque: '))
for i in range (0,C,1):
    lista=[]
    lista.append(int(input('Digite a medida do taco%.d: ' %(i+1))))
for i in range (0,C,1):
    for j in range (0,C,1):
        if i==j:
            continue
        if i!=j:
            if j+1<C:
                if lista[i]!=lista[j+1]:
                    cont+=2
                if lista[i]==lista[j+1]:
                    continue
            else:
                continue
print(cont)
