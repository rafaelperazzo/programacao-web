# -*- coding: utf-8 -*-
import math
f=float(input('digite f:'))
l=float(input('digite l:'))
q=float(input('digite q:'))
deltaH=float(input('digite deltaH:'))
v=float(input('digite v:'))
D=((8*f*l)*(q*q)/(math.pi*math.pi)*(9.81*deltaH))**(1/5)
print(' O valor de D é %.4f' %D)
rey=(4*q)/(math.pi*d*v)
print(' O valor de Rey é %.4f' %rey)
k=0.25/(math.log10((0.000002/(3.7*D))+(5.74/(rey**0.9)))**2
print(k)