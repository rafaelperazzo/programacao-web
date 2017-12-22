# -*- coding: utf-8 -*-

n=int(input('tamanho da matriz nxn: '))
m=[]
for i in range (n):
    lin=[]
    for j in range(n):
        lin.append(int(input('elementos da matriz: ')))
    m.append(lin)
sl=[]

for i in range (n):
    sl.append(sum(m[i]))
        
        

print(sl)