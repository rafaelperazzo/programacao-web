# -*- coding: utf-8 -*-
matriz=[]
m=int(input('digite a quantidade de linhas:'))
n=int(input('digite a quantidades de colunas: '))
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite os valores:')))
    matriz.append(linha)


#analisa superior e inferior
c=[]
for i in range(0,m,1):
    if sum(matriz[i])>=1:
        c.append(i)
        break
for i in range(m-1,-1,-1):
    if sum(matriz[i])>=1:
        c.append(i)
        break
    
#limites laterais
lat=[]
for i in range(0,m,1):
    for j in range(0,n,1):
        if matriz[i][j]==1:
            lat.append(j)
lat=sorted(lat)

#limites inteiros
c1=int(c[0])
c2=int(c[1])
x1=int(lat[0])
x2=int(lat[len(lat)-1])

#new matriz
n=[]
for i in range(c1,c2-1,1):
    for j in range(x1,x2-1,1):
        n.append(a[i][j])
        
print(n)