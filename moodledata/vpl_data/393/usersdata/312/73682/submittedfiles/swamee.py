# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
F=float(input('valor de F'))
L=float(input('valor de L'))
Q=float(input('valor de Q'))
DeltaH=float(input('valor de DeltaH'))
V=float(input('valor de V'))
g=('9.81')
e=('0.000002')
D=((8*F*L*Q**2)/(math.pi**2*g*DeltaH)**(1/5)
Rey=(4*Q)/(math.pi*D*V)
K=0.25/(math.log10(e/(3.7*D)+5.74/(Rey**0.9)))**2




print('%.f2'%(K))