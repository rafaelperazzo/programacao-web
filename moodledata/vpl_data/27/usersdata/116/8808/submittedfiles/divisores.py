# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input ('insira o valor de n:') 
a = input ('insira o valor de a:')
b = input ('insira o valor de b:')

j=1 
i=1
while j<=n:
    while i>=a:
        if i%a==0 and i%b==0:
            print i
        elif i%a==0 or i%b==0:
            print i
        
    