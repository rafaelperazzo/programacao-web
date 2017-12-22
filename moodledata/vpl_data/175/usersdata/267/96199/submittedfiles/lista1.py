# -*- coding: utf-8 -*-

n=int(input('Tamanho da lista: '))
a=[]
par=[]
impar=[]
for i in range(0,n,1):
    a.append(input('Digite o elemento: '))
    if a[i]%2==0:
        par.append(a[i])
    else:
        impar.append(a[i])
print(a)
print('Par: ')
print(par)
print('Ímpar: ')
print(impar)



