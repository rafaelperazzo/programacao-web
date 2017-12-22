# -*- coding: utf-8 -*-
import numpy as k


n=int(input("Digite a dimensão da matriz: "))
matriz= k.empty([n,n])
for i in range (n):
    for j in range (n):
        matriz[i][j]=int(input("Digite um elemento para sua matriz:"))
        


#verificando se é um quadrado mágico 
a=[]
#soma das linhas
for p in range(n):
    ls=sum(matriz[p])
    a.append(ls)


#soma das colunas
w=0
for i in range (n):
    for j in range (n):
        w=(matriz[j][i])+w
    a.append(w)

#soma da diagonal
q=0
for i in range (n):
    for j in range (n):
        if i==j:
            q=(matriz[i][j]) + q
            
a.append(q)

#soma diagonal secundária

u=0
for i in range (n):
    for j in range (n):
        if (i+j)==(n-1):
            u=(matriz[i][j])
a.append(q)


l=len(a)
e=0
for t in range(l-1):
    if a[t]==a[t+1]:
        e=1
    else:
        e=2
    
if e==1:
    print("S")
else:
    print("N")
    















