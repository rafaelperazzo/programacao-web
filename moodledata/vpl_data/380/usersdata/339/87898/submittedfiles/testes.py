# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

x=int(input('x: '))
n=int(input('n: '))



def raiz(x,n):
    r=x**(1/float(n))
    return r
print(raiz(x,n))