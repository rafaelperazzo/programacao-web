# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de linhas: "))
n=int(input("Digite a quantidade de colunas: "))
matriz=[]
for i in range (0,n,1):
    linha=[]
    linha.append(int(input("Digite um valor para a quadra: ")))
matriz.append(linha)
soma_coluna=[]
for j in range (0,n,1):
    c=0
    for i in range (0,m,1):
        c=c+(matriz[j][i])
    soma_coluna.append(c)
valor=n*1000    
for i in range (0,n,1):
    if soma_coluna[i]<valor:
        valor=soma_coluna
print (valor)
        
        
