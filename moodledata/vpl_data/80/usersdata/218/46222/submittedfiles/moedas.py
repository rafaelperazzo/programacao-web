# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor a ser trocado:'))
i=0
if a>=b:
    M=a
    m=b
else:
    M=b
    m=a
while i<=c:
    nvalor=c-(M*i)
    if nvalor%m==0:
        e=nvalor//m
        print(i)
        print(e)
        break
i=i+1    