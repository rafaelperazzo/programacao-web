# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('Digite um valor para f'))
L=float(input('Digite um valor para L'))
Q=float(input('Digite um valor para Q'))
DeltaH=float(input('Digite um valor para DeltaH'))
v=float(input('Digite um valor para v')) 
g=9.81
E=0.000002
pi=math.pi
D=((8*f*L*(Q**2))/((pi**2)*g*DeltaH))**(1/5)
Rey=4*Q/(pi*D*v)
