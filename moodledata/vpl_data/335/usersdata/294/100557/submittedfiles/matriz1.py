# -*- coding: utf-8 -*-
a=[]
m= int(input(' '))
n= int(input(' '))
for i in range (0,m,1):
    linha= []
    for j in range (0,n,1):
        linha.append(int(input(' ')))
    a.append(linha)
    
c=[]
for i in range (0,m,1):
    if sum(a[i])>1:
        c.append(i)
        break
for i in range (m-1,-1,-1):
    if sum(a[i])>=1:
        c.append(i)
        break

lat= []
for i in range (0,m,1):
    for j in range (0,n,1):
        if a[i][j]==1:
            lat.append(j)
lat= sorted(lat)

c1=int(c[0])
c2=int(c[1])
x1= int(lat[0])
x2= int(lat[len(lat)-1])

n=[]
for i in range (c1,c2+1,1):
    for j in range (x1,x2+1,1):
        n.append(a[i][j])
print(n)
