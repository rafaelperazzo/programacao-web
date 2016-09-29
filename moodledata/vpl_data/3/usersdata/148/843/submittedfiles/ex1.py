# -*- coding: utf-8 -*-
from __future__ import division
a= input('Digite um valor:')
#PROCESSAMENTO
if a<0 :
    a = (a**2)
    print('%.2f' %a)
elif a>=0 :
    a = (a**(1/2))
    print('%.2f' %a)
    