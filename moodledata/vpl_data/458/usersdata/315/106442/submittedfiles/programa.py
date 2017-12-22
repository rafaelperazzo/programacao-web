# -*- coding: utf-8 -*-
while True:
    m = int(input('Digite quant linhas: '))
    if m>=2:
        break

while True:
    n = int(input('Digite quant colunas: '))
    if n>=2:
        break


matriz = []
for i in range(m):
    v = []
    for j in range(n):
        v.append(int(input('Digite valor: ')))
    matriz.append(v)
    








