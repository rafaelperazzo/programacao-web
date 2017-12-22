# -*- coding: utf-8 -*-
m=int(input("Digite o número de linhas: "))
n=int(input("Digite o número de colunas: "))
matriz=[]
for i in range (0,m,1):
    lista=[]
    for j in range (0,n,1):
           lista.append(int(input("Digite o elemento%.d da matriz: " %(i+1))))
    matriz.append(lista)
for i in range(m-1,0,1):
    for j in range(n-1,0,1):
        matriz[i][j]=matriz[i-(n-1)][j-(m-1)]
print(matriz)
           
 

    
    
    

