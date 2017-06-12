# -*- coding: utf-8 -*-
i=1000
while (i<=9999):
    d1=i%100
    d2=i//100
    if (d1+d2)*(d1+d2)==i:
        print(i)
    i=i+1
