# -*- coding: utf-8 -*-
a=float(input('a:'))
b=float(input('b'))
c=float(input('c'))
delta=(b)**2-4*a*c
x1=(-b+(delta**(1/2)))/(2*a)
x2=(-b-(delta**(1/2)))/(2*a)
if delta>=0:
    print(x1,x2)
else:
    print('SRR',x1,x2)
