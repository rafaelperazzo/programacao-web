# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de elementos de n: '))
m = int(input('Digite a quantidade de elementos de m: '))
for i in range(0,n,1):
    n.append(int(input('Digite n%d: ' %(i+1))))
for i in range(0,m,1):
    m.append(int(input('Digite m%d: ' %(i+1))))
q = 0
if n > m:
    for i in range(0,n,1):
        if a[i] in b:
            q = q+1
    print(q)
    
