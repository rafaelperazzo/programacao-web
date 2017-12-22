# -*- coding: utf-8 -*-
n=int(input('digite dimensão: '))
while not n>=3:
    n=int(input('digite dimensão: '))
matriz=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite valor elemento linha: '))
    matriz.append(linha)
soma_l=[]
for i in range(0,n,1):
    soma_l.append(sum(matriz[i]))
soma_c=[]
for j in range (0,n,1):
    c=o
    for i in range(0,n,1):
        c=c+ matriz[i][j]
    soma_c.append(c)
b=[soma_l[0]]
ct=0
k=0
valorerrado=0
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
    
if ct!=:
    valorerrado=soma_l[0]
    valorcorreto=soma_l[1]
    k=0
b1=[soma_c[0]]
cont2=0
k1=0
valorerrado1=0
for i in range(0,n,1):
    if soma_c[i] in b1:
        continue
    else:
        cont2=cont2+1
        k1=i
if cont2==1:
    valorerrado1=soma_c[k]
    
if cont2 !=1:
    valorerrado1=soma_c[0]
    k1=0
    
u=valorcorreto- (valorerrado-matriz[k][k1])
p=matriz[k][k1]
print(u)
print(p)

