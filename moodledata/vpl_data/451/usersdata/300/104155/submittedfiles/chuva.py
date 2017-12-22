# -*- coding: utf-8 -*-
n = int(input('Digite o valor de n: '))
p = []
for i in range(0,n,1):
    p.append(int(input('Digite um valor: ')))
for i in range(1,n,1):
    cont = 0
    if p[0] < p[i]:
        cont = cont + 1
        break
if cont == 0:
    j = 0
    if p[0] == p[i]:
        j = i
    cont1 = 0    
    for i in range(1,j,1):
        cont1 = cont1 + 1 
    print(cont1)
if cont == 1:
    for i in range(2,n,1):
        if p[i-1] > p[i]:
            t = i
    for i in range(t,n,1):
        cont1 = 0
        if p[n-1] > p[i]:
            cont1 = cont1 + 1
            break
        if cont1 == 1:
            r = 0
            for i in range(t+1,n-1,1):
                r = r + 1
    for i in range(0,t,1):
        cont2 = 0
        if p[0] < p[i]:
            cont2 = cont1 + 1
            break
        if cont1 == 1:
            s = 0
            for i in range(1,t,1):
                s = s + 1
    g = s + r
    print(g)
                
        
    
       