# -*- coding: utf-8 -*-

for i in range(1000,9999+1,1):
    x=i//100
    y=i%100
    if ((i)**(1/2))==(x+y):
        print(i)
