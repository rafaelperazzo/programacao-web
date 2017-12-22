# -*- coding: utf-8 -*-
n=int(input("Digite a ordem da matriz: "))
matriz=[]
for i in range (0,n,1):
    linha=[]
    for j in range (0,n,1):
        linha.append(int(input("Digite um numero da matriz: ")))
    matriz.append (linha)
    
soma_linha=[]
for i in range (0,n,1):
   soma_linha.append(sum(matriz[i]))
   
soma_coluna=[]
for j in range (0,n,1):
    c=0
    for i in range (0,n,1):
        c+=matriz[i][j]
    soma_coluna.append(c)
    
b=[soma_coluna[0]]
ct=0
k=0
errado=0
correto=0
for i in range (0,n,1):
    if soma_linha[i] in b:
        continue
    else:
        ct+=1
        k+=i
if ct==1:
    errado=soma_linha[k]
    correto=soma_linha[0]
if ct!=1:
    errado=soma_linha[0]
    correto=soma_linha[1]
    k=0
    
b1=[soma_coluna[0]]
ct1=0
k1=0
errado1=0
for i in range (0,n,1):
    if soma_coluna[i] in b1:
        continue
    else:
        ct1+=1
        k1+=i
if ct1==1:
    errado1=soma_coluna[k1]
if ct1!=1:
    errado1=soma_coluna[0]
    k1=0
    
original=correto-(errado-matriz[k][k])
posterior=matriz[k][k1]
print (original)
print (posterior)

