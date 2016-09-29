# -*- coding: utf-8 -*-
#teste 1
from __future__ import division
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')

delta = ((b**2)-4*a*c)

if delta>=0:
    x1 = ((-b)+((delta)**0.5))/2*a
    x2 = ((-b)-((delta)**0.5))/2*a
    print ('O valor da primeira raiz é: %.1f'% x1)
    print ('O valor da segunda raiz é: %.1f'% x2)
else:
    print ('Essa equação não possui raizes reais.')

#teste 2

a= input('Digite um número "a":')

if a<0:
    QuadradoDeA = (a**2)
    print ('o quadrado de "a" é %.2f' % QuadradoDeA)
else:
    RaizDeA = a**0.5
    print ('A raiz de "a" é igual a %.2f' % RaizDeA)
