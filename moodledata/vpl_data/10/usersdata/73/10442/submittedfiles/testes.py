# -*- coding: utf-8 -*-
from __future__ import division
a=input ('digite a:')
i=1
while i<=a:
    if a==(i*(i+1)*(i+2)):
        print ('sim')
        break
    if (i*(i+1)*(i+2))>a:
        print ('nao')
        break
    i=i+1
    