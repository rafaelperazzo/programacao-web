# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
p=float(input('Digite um valor:'))
a=float(input('Digite um valor:'))
imc=p/(a**2)
if imc<20:
    print('Abaixo')
if 20>=imc and imc<=25:
    print('Normal')
if 25<imc and imc<=30:
    print('Sobrepeso')
if 30<imc and imc<=40:
    print('Obesidade')
if imc>40:
    print('Mórbida')