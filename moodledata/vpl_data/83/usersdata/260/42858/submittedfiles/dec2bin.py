# -*- coding: utf-8 -*-
n=float(input("digite um valor decimal"))
contador=0
soma=0
while n/2>0:
    resto=n%2
    soma=soma+resto*10**(contador)
    n=n//2
    contador=contador+1
print(soma)
