# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('digite f:'))
L=float(input('digite L:'))
Q=float(input('digite Q:'))
DeltaH=float(input('digite DeltaH:'))
V=float(input('digite V:'))
g=9.81
E=0.000002
D=((8*f*L*(Q*Q))/((math.pi**2)*g*DeltaH))**1/5
Rey=(4*Q)/(math.pi*D*V)
K=0.25/(math.log10((E/(3.7*D))+(5.74/(Rey**0.9)))**2