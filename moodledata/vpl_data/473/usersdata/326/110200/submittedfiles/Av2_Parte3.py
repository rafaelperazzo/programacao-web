# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de elementos das listas: '))

a=[]
b=[]
c=[]

while len(a) < n:
    a.append(input('Digite o valor: '))
while len(b) < n:
    b.append(input('Digite o valor: '))
while len(c) < n:    
    c.append(input('Digite o valor: '))
for i in range(a[0], a[n], 1):
    if a[i] > a[n]:
print('S')