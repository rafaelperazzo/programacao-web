# -*- coding: utf-8 -*-
matriz = []
m=(int(input()))  
n=(int(input())) 
matriz1=[]
for i in range (0,m,1) :
    lista=[]
    for i in range (0,n,1) :
        lista.append(int(input()))
    matriz.append(lista)
for i in range(0,m,1) :
    for j in range (0,n,1) :
     matriz1.append(matriz[m-i-1][n-j-1])
 
print(matriz1)

















