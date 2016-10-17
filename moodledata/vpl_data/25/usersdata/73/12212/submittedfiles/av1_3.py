# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input ('digite a:')
b=input ('digite b:')
i=1
mdc=1
cont=1
while i<b:
    if a%i!=0 or b%i!=0:
        cont=cont+1
    if a%i==0 and b%i==0:
        mdc=i
    i=i+1
print mdc
print cont

    
        


