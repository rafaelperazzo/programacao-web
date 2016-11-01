# -*- coding: utf-8 -*-
from __future__ import division

b=input('Digite número binário: ')
cont=0
n=b
while n>1:
    cont=cont+1
    n=n/10
print(cont)