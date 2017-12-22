# -*- coding: utf-8 -*-
n= int(input('Valor de n: '))
a= []

for i in range(n):
    if i%2==0:
        a.append(int(input('Valor%d: ' % i)))
        par=[]
        impar= []
        par.append(i)
    elif i%2!=0:
        impar.append(i)













print(a)
print(par)
print(impar)