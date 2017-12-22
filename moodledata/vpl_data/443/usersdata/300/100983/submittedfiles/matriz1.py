# -*- coding: utf-8 -*-
n = int(input('Digite o número de linhas: '))
m = int(input('Digite o número de colunas: '))
a = []
for i in range(0,m,1):
    l = []
    for j in range(0,n,1):
        l.append(int(input('Digite um elemento da matriz: ')))
    a.append(l)
b = []
for p in range(m,0,-1):
    z = []
    for h in range(n,0,-1):
        z.append(l[m])
    b.append(z)
print(b)    
    
    
