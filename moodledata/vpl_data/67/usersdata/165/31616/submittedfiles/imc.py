# -*- coding: utf-8 -*-
peso=float(input('digite um peso em kilos:'))
altura=float(input('digite uma altura em metros:'))
imc=peso/(altura**2)
if 20<=imc<=25:
    print('normal')
if 25<imc<=30:
    print('sobrepeso')
if 30<imc<=40:
    print('obesidade')
if imc>40:
    print('obesidade')



