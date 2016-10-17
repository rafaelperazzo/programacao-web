# -*- coding: utf-8 -*-
from __future__ import division
import math
zeta=0
tan=0
a=input('Digite o valor de a')
b=input('Digite o valor de b')
c=a%b
while a%b!=0:
    if b%c!=0:
        b=a
        c=b
    while a%b!=0:
        zeta=zeta+1
    print(zeta)