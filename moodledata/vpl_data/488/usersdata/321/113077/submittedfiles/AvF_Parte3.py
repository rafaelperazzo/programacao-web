# -*- coding: utf-8 -*-
n= int(input('Valor de n: '))
a= []


for i in range(n):
    par=[]
    impar= []
    if i % 2 == 0:
        par.append(i)
        i+=1
    elif i % 2 != 0 :
        impar.append(i)
        i+=1
    a.append(int(input('Valor%d: ' % i)))        
        












print(a)
print(par)
print(impar)