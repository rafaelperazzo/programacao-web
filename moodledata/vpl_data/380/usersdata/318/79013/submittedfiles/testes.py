# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

#ENTRADA
f = float(input('Digite valor para o f :'))
L = float(input('Digite valor para o L :'))
Q = float(input('Digite valor para o Q :'))
deltaH = float(input('Digite valor para o deltaH :'))
v = float(input('Digite valor para o v :'))
g = 9.81
e = 0.000002
r = math.pi

#PROCESSAMENTO
D = ((8*f*L(Q**2))/((r**2)g*deltaH))**(1/5.0)
Rey = (4*Q)/(r*D*v)
k = (0.25)/(math.log10((e/(3.7*(D)))+((5.74)/((Rey)**0.9)))**2)

#SAIDA
print('%.4f' % D)
print('%.4f' % Rey)
print('%.4f' % k)