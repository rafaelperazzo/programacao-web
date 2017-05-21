# -*- coding: utf-8 -*-
for i in range (1000,10000,1):
    parte1=i//100
    parte2=i%100
    
    if i**0.5==parte1+parte2:
        print(i)
