# -*- coding: utf-8 -*-
n= int(input('Valor de n: '))
a= []


for i in range(n):
    par=[]
    impar= []
    if i % 2 == 0:
        par.append(i)
    elif i % 2 != 0 :
        impar.append(i)
    a.append(int(input('Valor%d: ' % i)))        
        












print(a)
print(par)
print(impar)