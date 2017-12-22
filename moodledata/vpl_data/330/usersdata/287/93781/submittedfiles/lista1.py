# -*- coding: utf-8 -*-
lista=[]
n=int(input('digite a quantidade de elementos: '))
for i in range (0,n,1):
    lista.append(float(input('digite o valor do elemento%d:' % (i+1))))
im=0
par=0
im=[]
par=[]
for i in range (0,n,1):
    if lista[i]%2 != 0:
        im+=lista[i]
print(im)

for i in range (0,n,1):
    if lista[i]%2 ==0:
        par+=lista[i]
print(par)

for i in range(0,n,1):
    if [lista[i]]%2 != 0:
print([lista[i]])
    
    
        



