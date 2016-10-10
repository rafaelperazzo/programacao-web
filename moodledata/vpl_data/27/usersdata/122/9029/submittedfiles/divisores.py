# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite o valor de n:')
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
i=2
cont=1

while cont<=n:
    if i%a==0 or i%b==0:
        cont=cont+1
        print i
    i=i+1