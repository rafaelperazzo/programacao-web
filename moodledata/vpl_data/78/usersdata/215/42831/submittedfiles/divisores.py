# -*- coding: utf-8 -*-
import math
n=int(input ('digite N:'))
a=int(input ('digite A:'))
b=int(input ('digite B:'))
i=0
a1=0
b1=0
for i in range(0,n):
   a1=a1+a
   b1=b1+b
   if a1<b1:
       print(a1)
    else:
       print(b1)
       
   i=i+1
   
