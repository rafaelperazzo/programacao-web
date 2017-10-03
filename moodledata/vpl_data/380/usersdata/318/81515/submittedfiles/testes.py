# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

#ENTRADA
h = float(input('Digite sa altura em metros: '))
kg = float(input('Digite seu peso em quilos: '))

imc = kg/(h**2)

if imc<17:
    print('MUITO ABAIXO DO PESO')
if imc>=17 and imc<18.5 :
    print('ABAIXO DO PESO')
if imc>=18.5 and imc<25 :
    print('PESO NORMAL')
if imc>=25 and imc<30 :
    print('ACIMA DO PESO')
if imc>=30 and imc<35 :
    print('OBESIDADE I')
if imc>=35 and imc<40 :
    print('OBESIDADE II (SEVERA)')
if imc>=40 :
    print('OBESIDADE III (MÓRBIDA)')