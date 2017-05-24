# -*- coding: utf-8 -*-
p=int(input('digite p:'))
a=float(input('digite a:'))
imc=p/(a*a)
if imc<20:
    print('abaixo')
if 20>=imc<=25:
    print('normal')
if 25<imc<=30:
    print('sobrepeso')
if 30<imc<=40:
    print('obesidade')
if imc>40:
    print('obesidade grave')