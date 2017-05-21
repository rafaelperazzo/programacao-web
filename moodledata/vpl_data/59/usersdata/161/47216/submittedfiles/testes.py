# -*- coding: utf-8 -*-
f=float(input('informe f')):
L=float(input('L')):
q=float(input('q')):
deltaH=float(input('deltaH')):
v=float(input('v')):
g=9.81
e=0.000002
D=((8*f*L*(q**2))/((math.pi**2)*g*deltaH))**(1/5)
Rey=(4*Q)/(math.pi*D*V)
k=(0.25)/(math.log10((e/3.7*D)+(5.74/Rey**0.9)))**2
print('%.4f' %D)
print('%.4f' %Rey)
print('%.4f' %k)