# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:')
cont=0
i=c//a
x=0
while i>=0:
    troco=c-i*a
    if troco%b==0:
        x=troco//b
        cont=cont+1
        break
    else:
        i=i-1
if cont>0:
    print(i)
    print(x)
else:
    print('não')