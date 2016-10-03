# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('n:')
a=input('a:')
b=input('b:')
cont=0
i=1
while True:
    if i%a==0 or i%b==0:
        print (i)
        cont=cont+1
    if cont==n:
        break
    i=i+1
    

    
