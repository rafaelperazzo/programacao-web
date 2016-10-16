# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite a:')
i=2
cont=0
while i<a:
    if a%i==0:
        cont=cont+1
    i=i+1
if cont==0:
    print ('primo')
else:
    print ('n primo')

        