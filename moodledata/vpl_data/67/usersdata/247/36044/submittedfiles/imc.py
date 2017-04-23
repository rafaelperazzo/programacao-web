# -*- coding: utf-8 -*-
a=float(input('digite a altura: '))
p=float(input('digite a peso: '))
imc=a/p**2
if imc<20:
    print('BAIXO')
elif 20<=imv<=25:
    print('NORMAL')
elif 25<imc<=30:
    print('SOBREPESO')
elif 30<IMC<=40:
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE')
