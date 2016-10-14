# -*- coding: utf-8 -*-
from __future__ import division
import math
n = int (input ('insira n:'))

i=10
cont=1

while i<=n: 
    if n%i>=0:
        cont = cont+1
        i=i*10
print (cont)

