# -*- coding: utf-8 -*-
for i in range(1000,10000,1):
    d1=i//100
    d2=i%100
    n=d1+d2
    if (n)**(1/2)==i:
        print(i)