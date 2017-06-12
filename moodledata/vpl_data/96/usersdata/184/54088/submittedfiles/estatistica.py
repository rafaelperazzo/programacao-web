# -*- coding: utf-8 -*-
N=int(input('digite a quantidade de elementos:'))
x1=int(input('digite um número:'))
x2=int(input('digite um número:'))
x3=int(input('digite um número:'))
x4=int(input('digite um número:'))
x5=int(input('digite um número:'))
y1=int(input('digite um número:'))
y2=int(input('digite um número:'))
y3=int(input('digite um número:'))
y4=int(input('digite um número:'))
y5=int(input('digite um número:'))
media=(x1+x2+x3+x4+x5)/5
a1=(x1-media)**2
a2=(x2-media)**2
a3=(x3-media)**2
a4=(x4-media)**2
a5=(x5-media)**2
variancia=(a1+a2+a3+a4+a5)/4
desviopadrao=variancia**0.5
print('%.2f'%media)
print('%.2f'%desviopadrao)
media2=(y1+y2+y3+y4+y5)/5
b1=(y1-media2)**2
b2=(y2-media2)**2
b3=(y3-media2)**2
b4=(y4-media2)**2
b5=(y5-media2)**2
variancia2=(b1+b2+b3+b4+b5)/4
desviopadrao2=variancia**0.5
print('%.2f'%media2)
print('%.2f'%desviopadrao2)