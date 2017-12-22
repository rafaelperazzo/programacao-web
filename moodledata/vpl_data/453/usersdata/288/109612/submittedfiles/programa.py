# -*- coding: utf-8 -*-
n=int(input("Digite a ordem da matriz:"))
while n<3:
    n=int(input("Digite a ordem da matriz:"))
m=[]
for i in range (0,n,1):
    l=[]
    for j in range (0,n,1):
        l.append (int(input("Digite um numero para a matriz:")))
    m.append (l)

soma_linha=[]
for i in range (0,n,1):
    cont=0
    for j in range (0,n,1):
        con+=m[i][j]
    soma_linha.append(cont)
    
soma+coluna=[]
for j in range (0,n,1):
    cont1=0
    for i in range (0,n,1):
        cont2+=m[i][j]
    soma_coluna.append(cont1)
    
peso=0
for i in range (0,n,1):
    for j in range (0,n,1):
        if soma_linha[i]+soma_coluna[j]-(2*(m[i][j]))>peso:
            peso=soma_linha[i]+soma_coluna[j]-(2*(m[i][j]))
print (peso)
    
    
    
