# -*- coding: utf-8 -*-
matriz=[]
n= int(input('Digite o numero de linhas: '))
m= int(input('Digite o numero de colunas: '))
for i in range (0,m,1):
    linha=[]
    for j in range (0,n,1):
        linha.append(int(input('Digite o elemnto%.d :' %(i+1))))
    matriz.append(linha)
ld=0
le=0
ls=0
li=0
for j in range (0,n,1):
    for i in range (0,m,1):
        if linha[i][j]==1:
            ls+=1
print(ls)
    
        
        

