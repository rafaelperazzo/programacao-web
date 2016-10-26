# -*- coding: utf-8 -*-
from __future__ import division

b=int(input("Entre com o numero: "))
d=b/2
r=b%2
f=str(r)

while d!=0:
    b=d
    d=b/2
    r=b%2
    f=str(r)+f

print int(f)
