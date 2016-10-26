# -*- coding: utf-8 -*-
from __future__ import division
b=str(input("Entre com o numero: "))
s=0
k=1
while k<=len(b):
    s=s+int(b[-k])*2**(k-1)
    k=k+1
print s
