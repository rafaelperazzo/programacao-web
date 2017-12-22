# -*- coding: utf-8 -*-
n= int(input('digite a dimensao do quadradro:'))
while not n>=3:
    n=int(input('digite a dimensao do quadrado: '))
matriz=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite os elementos: ')))
    matriz.append(linha)
soma_l=[]
for i in range(0,n,1):
    soma_l.append(sum(matriz[i]))
soma_c=[]
for j in range (0,n,1):
    c=0
    for j in range(0,n,1):
        c=c+matriz[i][j]
    soma_c.append(c)
b=[soma_l[0]]
ct=0
k=0
valorerraddo=0
valorcorreto=0
for i in range(0,n,1):
    if soma_l[i] in b:
        continue
    else:
        ct=ct+1
        k=i
if ct==1:
    valorerrado=soma_l[k]
    valorcorreto=soma_l[0]
if ct!=1:
    valorerrado=soma_l[k]
    valorcorreto=soma_l[1]
    k=0
b1=[soma_c[0]]
cont2=0
K1=0
valorerrado1=0
for i in range(0,n,1):
    if soma_c[i] in b1:
        continue
    else:
        cont2=cont2+1
        k1=i
if cont2==1:
    valorerrado1=soma_c[k1]
if cont2!=1:
    valorerrado1=soma_c[0]
    k1=0
    
original=valorcorreto-(valorerrado-matriz[k][k1])
posterior=matriz[k][k1]
print(original)
print(posterior)