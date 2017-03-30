# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
f=float(input('digite um valor f'))
l=float(input('digite um valor l'))
q=float(input('digite um valor q'))
deltah=float(input('digite um valor deltah'))
v=float(input('digite um valor v'))
g=9.81
e=0.000002
d=((8*f*l*q*q)/(math.pi*math.pi*g*deltah))
print('%.4f'%d)

