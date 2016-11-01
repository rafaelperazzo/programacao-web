# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite a: ')
b=input('Digite b: ')
c=input('Digite c: ')

q=c
i=0
cont=0
while q>0:
   
   q= (q//a)
   i=q*a
   if i==c:
       print q
   