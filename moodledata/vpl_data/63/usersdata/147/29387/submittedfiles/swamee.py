# -*- coding: utf-8 -*-
import math
g=9.81
E=0.000002
f=float(input('digite f:'))
L=float(input('digite L:'))
Q=float(input('digite Q:'))
deltaH=float(input('digite deltaH:'))
v=float(input('digite v:'))
D=((8*f*L*Q*Q)/((math.pi*math.pi)*g*deltaH))**(1/5)
print('%.4f' %D)
Rey=(4*Q)/((math.pi)*D*v)
print('%.4f' %Rey)
k=0.25/(math.log10((E/(3.7*D))+(5.74/((Rey)**0.9))))**2
print('%.5f' %k)