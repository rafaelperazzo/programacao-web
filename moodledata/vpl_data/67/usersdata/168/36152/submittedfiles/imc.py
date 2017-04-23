# -*- coding: utf-8 -*-
p=float(input('Digite o peso: '))
a=float(input('Digite a altura: '))
imc=p/(a**2)
if imc<20:
    print('Abaixo')
elif 20<=imc<=25:
    print('Normal')
elif 25<imc<=30:
    print('Sobrepeso')
elif 30<imc<=40:
    print('Obesidade')
elif imc>40:
    print('Obesidade grave')



