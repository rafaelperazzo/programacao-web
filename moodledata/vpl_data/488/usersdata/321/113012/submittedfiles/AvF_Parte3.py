# -*- coding: utf-8 -*-
n= int(input('Valor de n: '))
a= []


for i in range(n):
    a.append(int(input('Valor%d: ' % i)))
par=[]
impar= []
    
while True:
    if a[i] % 2 == 0:
        par.append(i)
        i+=1
    elif a[i] % 2 != 0 :
        impar.append(i)












print(a)
print(par)
print(impar)