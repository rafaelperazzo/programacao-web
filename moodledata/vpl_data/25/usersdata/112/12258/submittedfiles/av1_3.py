# -*- coding: utf-8 -*-
from __future__ import division
import math

novoc=0
novob=0
novoa=0
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=a%b
while c!=0:
    if b%c!=0:
        print(b%c)