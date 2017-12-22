# -*- coding: utf-8 -*-
C = int(input('Digite o número de consultas ao estoque: '))
a = []
for i in range(0,C,1):
    a.append(int(input('Digite o comprimento do taco desejado: ')))
cont = 0    
for i in range(0,C,1):
    for j in range(0,C,1):
        if a[i] == a[j]:
            cont = cont + 1
q = cont - C
r = (C*2) - q
print(r)
    
