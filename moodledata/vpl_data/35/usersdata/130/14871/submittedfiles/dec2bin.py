# -*- coding: utf-8 -*-
from __future__ import division
p=input('Digite o valor de p:')
q=input('Digite o valor de q:')
s=1
while True:
    if p//10!=0:
        s=s+1
    p=p//10
    if p//10==0:
        break
while True:
    if (q%(10**s))==p:
        