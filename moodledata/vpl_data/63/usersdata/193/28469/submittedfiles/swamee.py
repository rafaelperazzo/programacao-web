# -*- coding: utf-8 -*-
import math
f=float(input('Digite f:'))
l=float(input('Digite l:'))
q=float(input('Digite q:'))
deltah=float(input('Digite deltah:'))
v=float(input('Digite v/;'))
g=9.81
e=0.000002
d=((8*f*l*((q)**2))/(((math.pi)**2*g*deltah))**(1/5)
rey=(4*q)/((math.pi*d*v))
k=0.25/(math.log10((e/(3.7*d))+(5.74/(rey**0.9))))**2
print('%.4f'%d)
print('%.4f'%rey)
print('%.4f'%k)
