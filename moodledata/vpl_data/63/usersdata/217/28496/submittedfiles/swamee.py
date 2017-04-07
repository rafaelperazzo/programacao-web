# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('digite um valor f'))
l=float(input('digite um valor l'))
q=float(input('digite um valor q'))
deltah=float(input('digite um valor deltah'))
v=float(input('digite um valor v'))
g=9.81
e=0.000002
pi=math.pi

d=((8*l*f*q*q)**0.2)/((pi*pi*g*deltah)**0.2)
rey=(4*q)/(pi*d*v)
k=0.25/
print('%.4f'%d)
print('%.4f'%rey)
