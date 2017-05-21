# -*- coding: utf-8 -*-
for i in range (1000,10000,1):
    a=(i)**0,5
    b=i//100
    c=i%100
    if b+c==a:
        print('%d'%i)