# -*- coding: utf-8 -*-
n=int(input('Digite a dimensao do quadrado: '))
while not n>=3:
    n=int(input('Digite a dimensao do quadrado: '))
matriz=[]
for i in range (0,n,1):
    linha=[]
    for j in range (0,n,1):
        linha.append(int(input('Digite um valor para o elemento da linha: ')))
        matriz.append(linha)
soma_L=[]
for i in range(0,n,1):
    soma_L.append(sum(matriz[i]))
soma_C=[]
for j in range (0,n,1):
    C=0
    for i in range(0,n,1):
        C= C + matriz[i][j]
    soma_C.append(C)
b=[soma_L[0]]
ct=0
k=0
valorerrado=0
valorcorreto=0
for i in range (0,n,1):
    if soma_L[i] in b:
        continue
    else:
        ct=ct+1
        k=i
if ct==1:
    valorerrado=soma_L[k]
    valorcorreto=soma_L[0]
if ct!=1:
    valorerrado=soma_L[0]
    valorcorreto=soma_L[1]
    k=0
b1=[soma_C[0]]
cont2=0
k1=0
valorerrado1=0
for i in range(0,n,1):
    if soma_C[i] in b1:
        continue
    else:
        cont2= cont2+1
        k1=i
if cont2==1:
    valorerrado1=soma_C[k1]
if cont2 !=1:
    valorerrador1=soma_C[0]
    k1=0

original = valorcorreto - (valorerrado-matriz[k][k1])
posterior = matriz[k][k1]
print(original)
print(posterior)