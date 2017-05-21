# -*- coding: utf-8 -*-

for i in range(1000,10000,1):
    parte1 = i//100
    parte2 = i%100
    #print (parte1,parte2)
    if i**(1/2)==parte1+parte2:
        print (i)
