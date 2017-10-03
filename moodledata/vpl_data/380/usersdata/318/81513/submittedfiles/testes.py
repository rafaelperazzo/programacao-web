# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

#ENTRADA
h = float(input('Digite sa altura: '))
kg = float(input('Digite seu peso: '))

imc = kg/(h**2)

if imc<17:
    print('%.2f' % imc 'MUITO ABAIXO DO PESO')
if imc>=17 and imc<18.5 :
    print('%.2f' % imc 'ABAIXO DO PESO')
if imc>=18.5 and imc<25 :
    print('%.2f' % imc 'PESO NORMAL')
if imc>=25 and imc<30 :
    print('%.2f' % imc 'ACIMA DO PESO')
if imc>=30 and imc<35 :
    print('%.2f' % imc 'OBESIDADE I')
if imc>=35 and imc<40 :
    print('%.2f' % imc 'OBESIDADE II (SEVERA)')
if imc>=40 :
    print('%.2f' % imc 'OBESIDADE III (MÓRBIDA)')