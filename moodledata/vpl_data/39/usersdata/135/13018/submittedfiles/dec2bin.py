# -*- coding: utf-8 -*-
from __future__ import division

b=input("Entre com o numero: ")
d=b/2
r=b%2
f=str(r)

while d!=0:
    b=d
    d=b/2
    r=b%2
    f=str(r)+f
f2=int(f)
print f2
