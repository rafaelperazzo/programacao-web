# -*- coding: utf-8 -*-
matriz=[]
M=int(input("Digite o número M de quadras no sentido Norte/Sul:"))
N=int(input("Digite o número N de quadras no sentido Leste/Oeste:"))
for i in range (0,M,1):
    m=[]
    for j in range (0,N,1):
        m.append(int(input("valor da quadra: ")))
    matriz.append(m)
print(matriz)
c=[]
for j in range (0,N,1):
    soma=0
    for i in range (0,M,1):
        soma += matriz[i][j]
print(soma)
        
        
        
    
    
        
    