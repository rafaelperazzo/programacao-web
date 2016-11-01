# -*- coding: utf-8 -*-
from __future__ import division
a=input('valor de moeda disponivel: ')
b=input('Valor de moeda disponivel: ')
c=input('valor da cedula')

na=c//a
r=c%a
nb=r//b

if r%b!=0:
    print('N')
else:
    print(na)
    print(nb)

    
    
