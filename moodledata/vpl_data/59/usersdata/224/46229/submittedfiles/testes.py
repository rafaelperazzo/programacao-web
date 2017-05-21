# -*- coding: utf-8 -*-
a=float(input('Digite o valor peso: '))
b=float(input('Digite o valor altura: '))  
imc=a/(b*b)
if imc<20:
    print('baixo')
if 20<=imc<=25:
    print('medio')
if 25<imc<=30:
    print('sobrepeso')
if 30<imc<=40:
    print('obesidade')
if imc>40:
    print('og')