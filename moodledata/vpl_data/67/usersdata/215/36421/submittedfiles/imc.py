# -*- coding: utf-8 -*-
p=float(input( 'digite o peso:'))
a=float(input( 'digite a altura:'))
imc=p/a
if imc<20:
    print('ABAIXO')
if imc>=20 and imc<=25:
    print ('NORMAL')
    