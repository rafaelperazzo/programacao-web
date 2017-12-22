# -*- coding: utf-8 -*-
n=int(input('Digite a dimensao da matriz: '))
while n<3:
    n=int(input('Digite a dimensao da matriz: '))
#casas da torre
a=[]
for i in range(0,n,1):
    b=[]
    for j in range(0,n,1):
        b.append(int(input('Digite  o valor da casa: ')))
    a.append(b)
#somando a coluna como linha
c=[]
for i in range (0,n,1):
    mat=[]
    for j in range (n):
        mat.append(a[j][i])
    c.append(mat)
total=0
for i in range (0,n,1):
    for j in range(0,n,1):
        if sum(a[i])-a[i][j] + sum(c[j])-c[j][i]) > total:
            total=(sum(a[i])-a[i][j] + sum(c[j])-c[j][i]))
print (total)
    
        
    
    
