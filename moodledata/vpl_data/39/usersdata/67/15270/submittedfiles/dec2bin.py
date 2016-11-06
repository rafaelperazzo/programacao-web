# -*- coding: utf-8 -*-
from __future__ import division

a=input("Digite o número na base decimal:")
c=a
d=a
f=0
while (c/2>0):
    d=d//2
    e=d%2
    f=e+f
print(f)
