# -*- coding: utf-8 -*-
import math
n1=int(input('digite o valor do primeiro número:'))
n2=int(input('digite o valor do segunda número:'))
if n1>=n2:
    ma=n1
    me=n2
else:
    ma=n2
    me=n1
cont=1
while ma%me!=0:
    cont=cont+1
    ma=me
    me=r
