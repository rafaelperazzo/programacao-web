# -*- coding: utf-8 -*-
from __future__ import division

a= input('Digite um valor: ')

if a<0:
    a= (a)**(2)
    print('%.2f'%a)

else:
    a= (a)**(1/2)
    print('%.2f'%a)