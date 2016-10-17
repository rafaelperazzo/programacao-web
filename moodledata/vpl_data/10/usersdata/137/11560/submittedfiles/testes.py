# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('digite n:'))
maiornota=0
menornota=10
for i in range (0,n+1,1):
    nota=input('digite a nota:')
    if nota>=maiornota:
        maiornota=nota
    if nota<=menornota:
        menornota=nota
print maiornota
print menornota
    