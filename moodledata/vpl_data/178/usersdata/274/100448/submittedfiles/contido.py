# -*- coding: utf-8 -*-
n = int(input("Digite um valor: "))
m = int(input("Digite outro valor: "))

a = []
b = []

for i in range (0,n,1):
    va = float(input(" Digite o elemento da primeira lista: "))
    a.append (va)

for i in range (0,n,1):
    vb = float(input(" Digite o elemento da segunda lista: "))
    b.append (vb)

k=0
c=0

while (k<n):
    for i in range (0,m,1):
        if (a[k] == b[i]):
            c=c+1
    k=k+1

print (c)   
        
        
    
    