# -*- coding: utf-8 -*-
for i in range(1000,10000,1):
    b=i//100
    c=i%100
    if (i)**(1/2)==b+c:
        print(i)