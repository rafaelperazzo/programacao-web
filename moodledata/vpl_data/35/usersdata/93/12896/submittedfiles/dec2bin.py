# -*- coding: utf-8 -*-
from __future__ import division
p=input('p')
q=input('q')
a=1
while p//10**a!=0:
    a=a+1
i=0
while True:
    if (q%10**(a+i))//10**i==p:
        print ('S')
        break
    i=i+1
    if 10**(a+i)>q*10:
        print('N')
        break


