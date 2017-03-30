# -*- coding: utf-8 -*- 
import math
G=9.81
E=0.000002
f=float(input('digite um valor para f:'))
L=float(input('digite um valor para L:'))
Q=float(input('digite um valor para Q:'))
deltaH=float(input('digite um valor para deltaH:'))
v=float(input('digite um valor para v:'))
D=(((8*f*L*(Q**2))/((math.pi**2)*G*deltaH)))**(1/5)
rey=(4*Q)/(math.pi*D*v)
n=E/(3.7*D)
m=5.74/(rey**0.9)
j=(math.log(n+m))**2
k=0.25/j
print('o valor de D: %.4f' %D)
print('o valor de rey:.4f' %rey)
print('o valor de k:.4f' %k)