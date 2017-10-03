# -*- coding: utf-8 -*-

p=float(input('valor de p'))
i=float(input('valor de i'))
n=float(input('valor de n'))

numerador = ((1+i)**n)-1
v = p*numerador/i

#v=p*(((1+i)**n)-1)/i
print('%.2f' % (v))