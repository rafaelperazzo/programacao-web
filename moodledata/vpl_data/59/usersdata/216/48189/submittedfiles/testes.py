# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
a=2
b=5
c=101
troco=0
qa=c//a
while qa>=0:
    troco=c%a
    if troco%a==0:
        print(qa)
    if troco%b==0:
        qb=troco//b
        break
    if troco%b==1:
        qa=qa-1
        
