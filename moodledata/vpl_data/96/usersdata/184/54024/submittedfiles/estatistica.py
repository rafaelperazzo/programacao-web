# -*- coding: utf-8 -*-
x1=int(input('digite um número:'))
x2=int(input('digite um número:'))
x3=int(input('digite um número:'))
x4=int(input('digite um número:'))
x5=int(input('digite um número:'))
media=(x1+x2+x3+x4+x5)/5
a1=(x1-media)**2
a2=(x2-media)**2
a3=(x3-media)**2
a4=(x4-media)**2
a5=(x5-media)**2
variancia=(a1+a2+a3+a4+a5)/4
desviopadrao=variancia**0.5
print('%2f'%media)
print('%2f'%desviopadrao)