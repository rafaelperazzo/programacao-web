# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite a:')
b=input('digite b:')
n=input('digite n:')
cont=1
i=1
while cont<=n:
    if i%a==0 and i%b==0:
        print i
        cont=cont+1
    i=i+1