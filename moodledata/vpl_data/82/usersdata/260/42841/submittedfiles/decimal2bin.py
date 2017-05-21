# -*- coding: utf-8 -*-
n=float(input("digite o valor de n:"))
contador=0
soma=0
    while n % 2 >0:
        resto=n%2
        soma=resto*(2**(contador))+soma
        n=n//2
        contador=contador+1
print(soma)
