# -*- coding: utf-8 -*-
while True:
    m = int(input('Digite numero de linhas: '))
    if m>=2 and m<=1000:
        break
    
while True:
    n = int(input('Digite numero de linhas: '))
    if n>=2 and n<=1000:
        break

matriz = []

for i in range (0,m,1):
    v = []
    for j in range(0,n,1):
        v.append(int(input('Digite: ')))
    matriz.append(v)
print (sum(matriz[0]))









