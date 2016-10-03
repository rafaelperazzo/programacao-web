# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite a quantidade de números a serem mostrados:')
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
i=a
while i<=n:
    if i%a==0 or i%b==0:
        print(i)
    i=i-1
        
        