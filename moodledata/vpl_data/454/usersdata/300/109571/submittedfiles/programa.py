# -*- coding: utf-8 -*-
C = int(input('Digite o número de consultas ao estoque: '))
a = []
for i in range(0,C,1):
    a.append(int(input('Digite o comprimento do taco desejado: ')))
cont = 0    
for i in range(1,C,1):
        if a[i] != a[i-1]:
            cont = cont + 1
r = cont*2
print(r)
    
