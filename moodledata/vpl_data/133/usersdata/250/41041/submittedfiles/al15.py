# -*- coding: utf-8 -*-
for i in range (1000,10000,1):
    d1=i//100
    d2=i%100
    if (d1+d2)==i**(1/2):
        print('%d'%i)