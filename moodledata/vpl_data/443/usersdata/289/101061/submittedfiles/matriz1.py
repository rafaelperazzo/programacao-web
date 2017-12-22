# -*- coding: utf-8 -*-
m=int(input("Digite o número de linhas: "))
n=int(input("Digite o número de colunas: "))
matriz=[]
for i in range (0,m,1):
    lista=[]
    for j in range (0,n,1):
           lista.append(int(input("Digite o elemento%.d da matriz: " %(i+1))))
    matriz.append(lista)
for i in range(m-1,-1,-1):
    matriz1=[]
    for j in range(n-1,-1,-1):
       lista.append(matriz[i][j])
    matriz1.append(lista)
print(matriz1)
           
 

    
    
    

