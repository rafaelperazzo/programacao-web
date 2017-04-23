# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
delta=(b*b)-4*a*c
if delta>=0:
    x1=(-b+(delta**1/2))/2*a
    print('x1 é %'%x1)
    x2=(-b-(delta**1/2))/2*a
    print('x2 é %'%x2)
if delta!=0 or delta<=0:
    print('srr')