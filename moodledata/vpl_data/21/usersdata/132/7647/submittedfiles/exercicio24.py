# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input(' digite um valor:')
b=input(' digite um valor:')
c=input(' digite um valor:')
if a>b and a>c:
    maior=a
if b>a and b>c:
    maior=b
if c>b and c>b:
    maior=c
if a<b and a<c:
    menor=a
if b<a and b<c:
    menor=b        
if c<b and c<a:
    menor=c
print(maior,menor)    