# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de elementos das listas: '))

a=[]
b=[]
c=[]

while len(a) < n:
    a = a.append(input('Digite o elemento de a: '))
while len(b) < n:
    b = b.append(input('Digite o elemento de b: '))
while len(c) < n:    
    c = c.append(input('Digite o elemento de c: '))
for i in range(a[0],n-1, 1):
    if a[0] > a[i]:
        print('S')
    else:
        print('N')