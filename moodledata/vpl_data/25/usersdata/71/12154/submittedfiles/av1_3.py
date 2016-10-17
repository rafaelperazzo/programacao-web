# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input("a: "))
b = int(input("b: "))

if a>b:
    n=a
    d=b
else:
    n=b
    d=a
    
resto=1
cont=0
mdc=d

while True:
    re=n%d
    cont=cont+1
    if re==0:
        print mdc
        print cont
        break
    else:
        n=d
        d=re
    mdc=re
