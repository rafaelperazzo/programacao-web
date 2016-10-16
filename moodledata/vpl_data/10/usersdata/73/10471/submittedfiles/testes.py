# -*- coding: utf-8 -*-
from __future__ import division
n=input ('digite n:')
cont=0
i=3
while i<=n:
    if n%i==0:
        cont=cont+1
    i=i+1
if cont==0:
    print n