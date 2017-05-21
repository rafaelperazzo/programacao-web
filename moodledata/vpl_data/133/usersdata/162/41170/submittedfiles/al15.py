# -*- coding: utf-8 -*-
for i in range(1000,10000,1):
    i1=(i)**(1/2)
    i2=i//100
    i3=i%100
    i4=i2+i3
    if i1==i4:
        print(i)