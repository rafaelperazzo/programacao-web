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
    for j in range(1,n,1):
        x+=(int(matriz[i][j-1]+matriz[i][j])-(int(matriz[i][i])))
    if int(matriz[i][i])>x:
        cont+=0
    else:
        cont+=1
        
if cont!=0:
    print('SIM')
else:
    print('NÃO')
            
        