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
d=((8*l*f*q*q)**1/5)/((pi*pi*g*deltah)**1/5)
print('%.4f'%d)