# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input("digete n:"))
a=int(input("digite a:"))
b=int(input("digite b"))
i=1
cont=1
while cont<=n:
    if i%a==0 or i%b==0:
        cont=cont +1
        print i
    i=i+1
    

