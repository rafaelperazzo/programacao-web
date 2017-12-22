# -*- coding: utf-8 -*-
m = int(input('Digite o número de quadras no sentido Norte-Sul: '))
while (m<2 or m>1000):
    m = int(input('Digite o número de quadras [2,1000] no sentido Norte-Sul: '))
n = int(input('digite o número de quadras no sentido Leste-Oeste: '))
while (n<2 or n>1000):
    n = int(input('digite o número de quadras [2,1000] no sentido Leste-Oeste: '))
valor = []
for i in range (0,m,1):
    for j in range (0,n,1):
        valor.append(int(input('Digite o valor de desapropriação da quadra%d%d: ' %(i+1,j+1))))
soma1=0
soma2=0
cont=0
for j in range (0,n,1):
    for i in range (0,m,1):
        while (cont<m):
            soma1+=valor[i][j]
            soma2+=valor[i][j+1]
            cont+=1
        if soma1<soma2:
            print(soma1)
        else:
            print(soma2)