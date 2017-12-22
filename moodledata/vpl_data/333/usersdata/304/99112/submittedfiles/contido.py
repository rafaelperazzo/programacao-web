# -*- coding: utf-8 -*-
a = []
b = []
cont = 0
n_a = int(input('Na: '))
n_b = int(input('Nb: '))
for i in range (0,n_a,1):
    v_a = int(input('A: '))
    a.append(v_a)
for i in range (0,n_b,1):
    v_b = int(input('b: '))
    b.append(v_b)

for i in range(0,n_a,1):
    for j in range(0,n_b,1):
        if a[i] == b[j]:
            cont = cont+1
print(cont)
    
