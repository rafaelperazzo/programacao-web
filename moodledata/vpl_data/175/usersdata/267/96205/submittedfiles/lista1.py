# -*- coding: utf-8 -*-

n=int(input('Tamanho da lista: '))
a=[]
par=[]
impar=[]
for i in range(0,n,1):
    a.append(input('Digite o elemento: '))
for i in range(0,n,1):
    if (a[i]%2==0):
        print('ok')
        #par.append(a[i])
    else:
        print('ok')
        impar.append(a[i])
print(a)
print('Par: ')
print(par)
print('Ímpar: ')
print(impar)



