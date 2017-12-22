# -*- coding: utf-8 -*-
while True:
    m=int(input('Digite o numero de quadras no sentido Norte-Sul: '))
    if m>=2 and m<=1000:
        break
    if m<2:
        m=int(input('Digite o numero de quadras no sentido Norte-Sul: '))
    if m>1000:
        m=int(input('Digite o numero de quadras no sentido Norte-Sul: ')

R = int(input('Digite o numero de quadras no sentido Leste-Oeste: '))
while R<2:
    R=int(input('Digite o numero de quadras no sentido Leste-Oeste: '))
while R>1000:
    R=int(input('Digite o numero de quadras no sentido Leste-Oeste: ')

mat=[]
for i in range (0, m, 1):
    linha=[]
    for j in range (0, n, 1):
        while True:
            valor=int(input('Digite o valor da quadra: '))
            if valor>=1 and valor<=100:
                break
            if valor<1:
                valor=int(input('Digite o valor da quadra: '))
            if valor>100:
                valor=int(input('Digite o valor da quadra: '))
        linha.append(valor)
    mat.append(linha)

somas=[]
for i in range (0, m, 1):
    sum=0
    for j in range (0, n, 1):
        sum+=mat[i][j]

menor=somas[0]
for i in range (1, m, 1):
    if somas[i]<menor:
        menor=somas[i]

print(menor)