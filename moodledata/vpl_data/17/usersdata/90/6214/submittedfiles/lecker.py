# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite aqui o primeiro valor a:')
b=input('Digite aqui o primeiro valor b:')
c=input('Digite aqui o primeiro valor c:')
d=input('Digite aqui o primeiro valor d:')

if a<b<c<d or a>b>c>d or a<b>c>d or a>b<c<d:
    print ('S')
else:
    print ('N')


