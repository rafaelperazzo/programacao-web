# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
a=2
b=5
c=101
qa=c//a
while qa>0:
    troco=c%a
    if troco%b==0:
        qb=troco//b
        break
    else:
        qa=qa-1
print(qa)
print(qb)
