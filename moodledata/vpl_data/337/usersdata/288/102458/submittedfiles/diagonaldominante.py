# -*- coding: utf-8 -*-
n=int(input("Digite a ordem da matriz: "))
while n<2:
    n=int(input("Digite a ordem da matriz: "))

matriz=[]
for i in range (0,n,1):
    linha=[]
    for j in range (0,n,1):
        linha.append(int(input("Digite o %dº da linha da matriz: "%(i+1))))
    matriz.append(linha)
    
soma=0
for i in range (0,n,1):
    for j in range (0,n,1):
        if i==j:
            soma=matriz[i][j]+soma
            
cont=0
for i in range (0,n,1):
    if sum(matriz[i])>soma:
        con+=1
        
for i in range (0,n,1):
    soma_coluna=0
    for i in range (0,n,1):
        soma_coluna=matriz[i][j]+soma_coluna
    if soma_coluna>soma:
        cont+=1
        
if cont>0:
    print ("NAO")
else:
    print ("SIM")
    

