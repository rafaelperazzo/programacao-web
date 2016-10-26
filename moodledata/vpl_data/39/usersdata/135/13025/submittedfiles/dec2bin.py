# -*- coding: utf-8 -*-
from __future__ import division

b=int(input("Entre com o numero: "))
d=int(b/2)
r=int(b%2)
f=r

while d!=0:
    b=d
    d=int(b/2)
    r=int(b%2)
    f=r+f

print f
    

