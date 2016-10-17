# -*- coding: utf-8 -*-
from __future__ import division
import math

a= int(input('Digite o valor de a:'))
b= int(input('Digite o valor de b:'))
c= int(input('Digite o valor de c:'))
d= int(input('Digite o valor de d:'))
e= int(input('Digite o valor de e:'))

while (13<=a<=1) or (13<=b<=1) or (13<=c<=1) or (13<=d<=1) or (13<=e<=1):
     a= int(input('Digite o valor de a:'))
     b= int(input('Digite o valor de b:'))
     c= int(input('Digite o valor de c:'))
     d= int(input('Digite o valor de d:'))
     e= int(input('Digite o valor de e:'))
     
if (a<b<c<d<e):
    print ('C')
else:
    if (a>b>c>d>e):
        print ('D')
    else:
        print ('N')





