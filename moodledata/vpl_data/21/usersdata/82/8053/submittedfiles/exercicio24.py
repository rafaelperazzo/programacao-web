# -*- coding: utf-8 -*-
from __future__ import division
import math

a= int(input('Digite o valor de a:'))
b= int(input('Digite o valor de b:'))
while (a<0) or (b<0):
    a= int(input('Digite o valor de a:'))
    b= int(input('Digite o valor de b:'))
i=1
produto=1
    if (i%a==0) and (i%b==0):
        produto = produto*i
        print (i)  
    i=i+1

    