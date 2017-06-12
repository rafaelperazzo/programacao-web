# -*- coding: utf-8 -*-
def numero(n):
    for i in range (1,n+1,1):
        d1=i%100
        d2=i/100
        if (d1+d2)*(d1+d2)==i:
            print (i)