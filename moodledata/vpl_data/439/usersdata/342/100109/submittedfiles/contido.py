# -*- coding: utf-8 -*-
n = int(input('insira a quantidade de elementos de A:'))
m = int(input('insira a quantidade de elementos de B:'))

a = []
b = []

for i in range (0,n,1):
    a.append(int(input('digite o %d° elemento de A:' %(i+1))))
for i in range (0,m,1):
    b.append(int(input('digite o %d° elemento de B:' %(i+1))))
    
c = []
for k in range (0,n,1):
    for i in range (0,m,1):
        if (a[k]==b[i]):
            c.append(a[k])
            

ambas = len(c)
print (ambas)
            







