# -*- coding: utf-8 -*-

x=int(input('Digite a quantidade de elementos de A: '))
y=int(input('Digite a quantidade de elementos de B: '))
a=[]
b=[]
for i in range (0, x, 1):
    a.append(int(input('Digite o %dº elemento de A: ' %(i+1))))
for i in range (0, y, 1):
    b.append(int(input('Digite o %dº elemento de B: ' %(i+1))))
c=[]
for t in range (0, x, 1):
    for i in range (0, y, 1):
        if (a[t]==b[i]):
            c.append(a[t])
            
qua=len(c)
print (qua)

