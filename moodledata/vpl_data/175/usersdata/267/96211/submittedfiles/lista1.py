# -*- coding: utf-8 -*-

n=int(input('Tamanho da lista: '))
a=[]
par=[]
impar=[]
for i in range(0,n,1):
    a.append(int(input('Digite o elemento: ')))
for i in range(0,len(a)-1,1):
    if a%2==0:
        print('par')
        #par.append(a[i])
    else:
        print('impar')
        impar.append(a[i])
print(a)
print('Par: ')
print(par)
print('Ímpar: ')
print(impar)



