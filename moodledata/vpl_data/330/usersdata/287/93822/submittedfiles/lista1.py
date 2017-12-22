# -*- coding: utf-8 -*-
lista=[]
n=int(input('digite a quantidade de elementos: '))
for i in range (0,n,1):
    lista.append(float(input('digite o valor do elemento%d:' % (i+1))))
print(lista)
im=0
par=0
contim=0
contpar=0
for i in range (0,n,1):
    if lista[i]%2 != 0:
        im+=lista[i]
        contim+=1
print(im)
print(contim)
for i in range (0,n,1):
    if lista[i]%2 ==0:
        par+=lista[i]
        contpar+=1



    
        



