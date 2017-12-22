# -*- coding: utf-8 -*-
m = int(input('Digite o número de linhas: '))
n = int(input('DIgite o número de colunas: '))
matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        linha.append(float(input('Digite o elemento %d de %d: ' %((j+1),(i+1)))))
    matriz.append(linha)
print(matriz)
a = 0
b = 0
c = []
for j in range(0,n-1,1):
    a = 0
    b = 0
    for i in range(0,m,1):
        if a < b:
            c.append(a)
        else:
            a.append(b)
d = 0
for i in range(len(c)-1):
    if c[i] < c[i+1]:
        d = c[i]
    else:
        d = c[i+1]
print(d)
        

        


        
        
        
