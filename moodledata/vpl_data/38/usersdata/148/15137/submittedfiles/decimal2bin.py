# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite um numero inteiro binario:')
somadec=0
i=0

while n>-1:
    a=n%10
    dec=a*(2**i)
    i=i+1
    somadec=somadec+dec
    n=n//10
    print('%.f' %somadec)

