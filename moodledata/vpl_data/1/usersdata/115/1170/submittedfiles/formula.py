# -*- coding: utf-8 -*-
from __future__ import division

p= input('Digite um valor para p: ')
i= input('Digite um valor para i: ')
n= input('Digite um valor para n: ')

v= (p)*((((1+i)**n)-1)/i)
print('%.2f'%v)