# -*- coding: utf-8 -*-
import math


n=int(input('Digite o valor de n:'))
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))

i=0
mult=2
while i<n:
    if mult%a==0 or mult%b==0:
        print(mult)
        i=i+1
    mult=mult+1