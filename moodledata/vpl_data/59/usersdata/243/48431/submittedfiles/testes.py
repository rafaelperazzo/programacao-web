# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
p=float(input('digite o peso:'))
a=float(input('digite a altura:'))

IMC=p/a**a

if IMC<20:
    print('abaixo')
elif 20<=IMC<=25:
    print('normal')
elif 25<IMC<=30:
    print('sobrepeso')
elif 30<IMC<=40:
    print('obsidade')
else:
    print('obsidade grave')