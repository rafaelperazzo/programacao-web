# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite a:')
b=input('Digite b:')
s=0
cont=0

if a>b:
    for i in range (1,a+1,1):
        if i%a==0 and i%b==0:
            s=i
            cont=cont+1
    print s
    print cont
    
elif b>=a:
    for i in range (1,b+1,1):
        if i%a==0 and i%b==0:
            s=i
            cont=cont+1
    print s
    print cont