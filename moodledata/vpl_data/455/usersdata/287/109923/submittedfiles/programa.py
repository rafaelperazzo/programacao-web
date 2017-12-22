# -*- coding: utf-8 -*-
n=int(input('digite a dimensãodo quadrado: '))
while not n>=3:
    n=int(input('digite a dimensão do quadrado: '))
matriz=[]
for i in range (n):
    linha=[]
    for j in range (n):
        linha.append(int(input('digite os valores: '))
    matriz.append(linha)
soma_L=[]
for i in range (n):
    soma_L.append(sum(matriz[i]))
soma_C=[]
for j in range (n):
    c=0
    for i in range (n):
        c+=matriz[i][j]
    soma_C.append(c)
b=[soma_L[0]]
ct=0
k=0
valorerrado=0
valorcorreto=0
for i in range (n):
    if soma_L[i] in b:
        conyinue
    else:
        ct+=1
        k=i
if ct== 1:
    valorerrado = soma_L[k]
    valorcorreto=soma_l[0]
if ct!= 1:
    valorerrado=soma_L[0]
    valorcorreto=soma_L[1]
    k=0
b1=[soma_C[0]]
cont2=0
kl=0
valorerrado1=0
for i in range (n):
    if soma_C[i] in b1:
        continue
    else:
        cont2 +=1
        k1=1
if cont2 == 1:
    valorerrado1 = soma_C[k1]
if cont2!=1:
    valorerrado1=soma_C[0]
    k1=0
    
original= valorcorreto- (valorerrado-matriz[k][k1])
posterior=matriz[k][k1]
print(original)
print(posterior)