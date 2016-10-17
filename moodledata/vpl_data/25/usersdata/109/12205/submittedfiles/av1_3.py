# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite a:')
b=input('Digite b:')
cont=0

if a>b:
    while True:
        c=a%b
        a=b
        b=c
        cont=cont+1
        if c==0:
            break
print a
print cont   
   