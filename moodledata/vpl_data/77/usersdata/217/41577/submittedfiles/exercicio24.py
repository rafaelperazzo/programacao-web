# -*- coding: utf-8 -*-
import math
n1=int(input('digite n1:'))
n2=int(input('digite n2:'))
if n1<n2:
    n1,n2=n2,n1
r1,mdc=n1%n2,n2
while r1!=0:
    r1,mdc=mdc%r1,r1
print('o mdc de (%d,%d) é:%d'%(n1,n2,mdc))

