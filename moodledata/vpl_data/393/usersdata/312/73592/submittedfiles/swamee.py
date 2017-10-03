# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
F=float(input('valor de F'))
L=float(input('valor de L'))
Q=float(input('valor de Q'))
DeltaH=float(input('valor de DeltaH'))
V=float(input('valor de V'))
g=('9.81')
D=math.sqrt((8*F*L*Q**2)/(math.pi**2*g*DeltaH))
print=('%.f2'%(D))