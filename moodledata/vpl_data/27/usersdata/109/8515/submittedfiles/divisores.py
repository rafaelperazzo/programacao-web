# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite o valor de n:')
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
cont=0
x=1

while True:
    if (x%a)==0 or (x%b)==0:
        print x
        cont=cont+1
        if cont==n:
            break
    x=x+1