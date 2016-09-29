# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:')
D=(b**2)-(4*a*c)
if D>=0:
    x1=((-b)+(D**0.5))/2*a

    x2=((-b)-(D**0.5))/2*a
    print('%.2f%'%x1)
    print('%.2f%'%x2)
else:
    print('não há raiz real')