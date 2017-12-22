# -*- coding: utf-8 -*-
matriz=[]
a=[]
m=int(input('Digite a quantidade de linhas (m): '))
n=int(input('Digite a quantidade de colaunas (n): '))
for i in range (0,m,1):
    linha=[]
    for j in range (0,n,1):
        linha.append(int(input('Digite um binario[0,1] : ')))
    matriz.append(linha)
    
for i in range (0,m,1):
    if sum(matriz[i])>=1:
        a.append(i)
        break
for i in range (m-1,-1,-1):
    if sum (matriz[i])>=1:
        a.append(i)
        break
lat=[]
for i in range (0,m,1):
    for j in range (0,n,1):
        if matriz[i][j]==1:
            lat.append(j)
            
x=sorted(lat)
a1=int(a[0])
a2=int(a[1])
x1=int(x[0])
x2=int(x[len(x)-1])
n=[]
for i in range (a1,a2+1,1):
    for j in range (x1,x2+1,1):
        n.append(matriz[i][j])
print (n)
