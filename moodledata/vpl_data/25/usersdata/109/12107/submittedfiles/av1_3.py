# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite a:')
b=input('Digite b:')
cont=0
c=0

if a>b:
    while c>0:
        c=a%b
        a=b
        b=c
        cont=cont+1
   
   