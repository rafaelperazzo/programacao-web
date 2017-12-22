# -*- coding: utf-8 -*-

n=int(input('tamanho da matriz nxn: '))
m=[]
for i in range (n):
    lin=[]
    for j in range(n):
        lin.append(int(input('elementos da matriz: ')))
    m.append(lin)
sl=[]
sc=[]
for i in range (n):
    sl.append(sum(m[i]))
    for j in range (n):
        sc.append(sum(m[i][j]))
        
        

print(sc)