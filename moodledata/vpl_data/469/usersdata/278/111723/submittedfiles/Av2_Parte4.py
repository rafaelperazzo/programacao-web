# -*- coding: utf-8 -*-
m=int(input('Digite o número de quadras no sentido norte-sul: '))
while (m<2 or m>1000):
    m=int(input('Digite o número (2<=m<=1000) de quadras no sentido norte-sul: '))
n=int(input('Digite o número de quadras no sentido leste-oeste: '))
while (n<2 or n>1000):
    n=int(input('Digite o número (2<=n<=1000) de quadras no sentido leste-oeste: '))
matriz=[]
for i in range (0,n,1):
    lista=[]
    for j in range (0,m,1):
        lista.append(int(input('Digite o valor da quadra de linha%.d e coluna%.d: ' %(i,j))))
    matriz.append(lista)
soma_L=[]
for i in range (0,n,1):
    soma=0
    for j in range (0,m,1):
        soma+=matiz[i][j]
    soma_L.append(soma)
menor=soma_L[0]
for i in range (0,n,1):
    if menor>soma_L[i]:
        menor=soma_L[i]
print(menor)