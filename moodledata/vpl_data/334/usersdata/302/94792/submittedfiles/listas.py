# -*- coding: utf-8 -*-
def degrau(a,n,b):
    for i in range(0,n,1):
        if i < n and i != 0:
            b.append(a[i-1]-a[i])
            if b[i-1] < 0:
                b[i-1] = -b[i-1]
b = sorted(b, reverse = True)
return print(b[0])
    
n = int(input('Digite o número de elementos da lista: '))
a = []
b = []
for i in range(0,n,1):
    a.append(int(input('Digite a%d: ' %(i+1))))
degrau(a,n,b)