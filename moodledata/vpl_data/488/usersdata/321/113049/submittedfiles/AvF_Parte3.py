# -*- coding: utf-8 -*-
n= int(input('Valor de n: '))
a= []
par=[]
impar= []

for i in range(n):
    a.append(int(input('Valor%d: ' % i)))
    if i % 2 != 0:
        par.append(i)
    else:
        if i % 2 == 0 :
            impar.append(i)
        












print(a)
print(par)
print(impar)