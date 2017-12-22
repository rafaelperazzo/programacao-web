# -*- coding: utf-8 -*-
matriz=[]
n=int(input(''))
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    matriz.append(linha)
    
x=0
cont=0
for i in range(0,n,1):
    for j in range(0,n,1):
        x+=int(matriz[i][j])
    if int(matriz[i][i])>(x-int(matriz[i][i])):
        cont+=1
    else:
        cont+=0
        
if cont==n:
    print('SIM')
else:
    print('NÃO')
            
        