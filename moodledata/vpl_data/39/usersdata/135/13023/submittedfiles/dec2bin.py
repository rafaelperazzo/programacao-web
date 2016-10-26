# -*- coding: utf-8 -*-
from __future__ import division

b=int(input("Entre com o numero: "))
d=b/2
r=str(b%2)
f=r

while d!=0:
    b=d
    d=b/2
    r=str(b%2)
    f=r+f

print f
    

