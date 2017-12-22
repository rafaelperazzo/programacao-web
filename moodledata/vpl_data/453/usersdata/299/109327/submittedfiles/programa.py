# -*- coding: utf-8 -*-
n=int(input(''))
while n<3:
    print('erro')
    n=int(input(''))
matriz=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    matriz.append(linha)
        
