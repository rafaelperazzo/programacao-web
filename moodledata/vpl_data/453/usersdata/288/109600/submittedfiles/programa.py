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


for i in range (0,n,1):
    soma_linha=0
    for j in range (0):
        soma_linha+=m[0][j]
        
for j in range (0,n,1):
    soma_coluna=0
    for i in range(0):
        soma_coluna+=m[i][0]
        
peso=0
    
    
soma_total=soma_linha+soma_coluna-(2*(m[i][j]))
for i in range (0,n,1):
    if soma_total>peso:
        soma_total=peso
print (peso)
    
    
    
