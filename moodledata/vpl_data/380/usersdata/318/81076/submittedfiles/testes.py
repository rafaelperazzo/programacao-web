# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

#ENTRADA
a = float(input('Digite valor de a:'))
b = float(input('Digite valor de b:'))
c = float(input('Digite valor de c:'))

#PROCESSAMENTO
Delta = ((b**2) - (4*a*c))

x1 = (-b) + ((Delta)**(1/2.0))/(2*a)
x2 = (-b) - ((Delta)**(1/2.0))/(2*a)

#SAIDA
if Delta<0:
    print('SRR')
else:
    Delta>=0
    print('x1:' + x1)
    print('x2:' + x2)