# -*- coding: utf-8 -*-
while True:
    m=int(input('Digite o numero de quadras no sentido Norte-Sul: '))
    if m>=2 and m<=1000:
        break
    if m<2:
        m=int(input('Digite o numero de quadras no sentido Norte-Sul: '))
    if m>1000:
        m=int(input('Digite o numero de quadras no sentido Norte-Sul: ')

while True:
    n=int(input('Digite o numero de quadras no sentido Leste-Oeste: '))
    if n>=2 and n<=1000:
        break
    if n<2:
        n=int(input('Digite o numero de quadras no sentido Leste-Oeste: '))
    if n>1000:
        n=int(input('Digite o numero de quadras no sentido Leste-Oeste: '))

mat=[]
for i in range (0, m, 1):
    linha=[]
    for j in range (0, n, 1):
        linha.append(int(input('Digite o valor da quadra: ')))
    mat.append(linha)

somas=[]
for i in range (0, n, 1):
    sum=0
    for j in range (0, m, 1):
        sum+=mat[j][i]
    somas.append(sum)

menor=somas[0]
for i in range (1, n, 1):
    if somas[i]<menor:
        menor=somas[i]

print(menor)