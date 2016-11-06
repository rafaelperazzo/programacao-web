# -*- coding: utf-8 -*-
from __future__ import division

a=input("Digite o número na base decimal:")
c=a
d=a
f=0
while (c//2!=0):
    e=d%2
    d=d//10
    f=e+f
    print(f)
    
