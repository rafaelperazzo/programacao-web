# -*- coding: utf-8 -*-
n= int(input('Digite a dimensão do quadrado:'))
while not n>=3:
    n= int(input('Digite a dimensão do quadrado:'))
matriz=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('Digite um valor para cada elemento:')))
    matriz.append(linha)
soma_Linha=[]
for i in range(0,n,1):
    soma_Linha.append(sum(matriz[i]))
soma_Coluna=[]
for j in range (0,n,1):
    C=0
    for i in range(0,n,1):
        C=C+matriz[i][j]
    soma_Colna.append(C)
b=[soma_Linha[0]]
ct=0
k=0
valorerrado=0
valorcorreto=0
for i in range(0,n,1):
    if soma_Linha[i] in b:
        continue
    else:
        ct=ct+1
        k=i
if ct==1:
    valorerrado=soma_Linha[k]
    valorcorreto=soma_Linha[0]
if ct!=1:
    valorerrado=soma_Linha[k]
    valorcorreto=soma_Linha[1]
    k=0
b1=[soma_Coluna[0]]
cont2=0
k1=0
valorerrado1=0
for i in range(0,n,1):
    if soma_Coluna[i] in b1:
        continue
    else:
        cont2=cont2+1
        k1=i
if cont2==1:
    valorerrado1=soma_Coluna[k1]
if cont2!=1:
    valorerrado1=soma_Coluna[0]
    k1=0
    
original= valorcorreto-(valorerrado-matriz[k][k1])
posterior= matriz[k][k1]
print(original)
print(posterior)

