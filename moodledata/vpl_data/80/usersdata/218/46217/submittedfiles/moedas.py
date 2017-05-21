# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor a ser trocado:'))
while i<=c:
    nvalor=c-(a*i)
    if nvalor%b==0:
        e=nvalor//b
        print(i)
        print(e)
i=i+1    