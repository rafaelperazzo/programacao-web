# -*- coding: utf-8 -*-
from __future__ import division
a= input('Digite um número "a":')

if a<0:
    QuadradoDeA = (a*a)
    print ('o quadrado de "a" é %.2f' % QuadradoDeA')
else:
    RaizDeA = a**0.5
    print ('A raiz de "a" é igual a %.2f' % RaizDeA )
