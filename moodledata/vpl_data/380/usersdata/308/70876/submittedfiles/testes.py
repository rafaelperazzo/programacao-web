# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a1 = float(input('Digite o a: '))
b1 = float(input('Digite o b: '))
c1 = float(input('Digite o c: '))
a2 = float(input('Digite o a: '))
b2 = float(input('Digite o b: '))

b1 = b1 - a2
c1 = c1 - b2

x1 = (-b1+(b1**2 - 4*a1*c1)**0.5)/2
x2 = (-b1-(b1**2 - 4*a1*c1)**0.5)/2

print ('As raizes da equação são %.2f e %.2f' % (x1, x2))
