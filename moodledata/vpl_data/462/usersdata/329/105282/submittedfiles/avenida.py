# -*- coding: utf-8 -*-
while True:
    m = int(input('digite o valor sul-leste'))
    if m>=2 and m<=1000:
        break
    
while True:
    n = int(input('digite o valor sul-leste'))
    if n>=2 and n<=1000:
        break
    
matriz = []

for i in range (0,m,1):
    v = []
    for j in range(0,m,1):
        v.append(int(input('digie: ')))
    matriz.append(v)
    
mt = []

for i in range(n):
    v = []
    for j in range(m):
        v.append(matriz[j][i])
    mt.append(v)
    
soma = 1000
for i in range(n):
    if sum(mt[i]) < som:
        som = sum(mt[i])
print (som)
    

