# -*- coding: utf-8 -*-
#ENTRADA
a = float(input('Peso: '))
b = float(input('Altura: '))
#PROCESSAMENTO
IMC=(a)/(b**2)
#SAIDA
if IMC<20:
    print ('ABAIXO')
elif  20<=IMC<=25:
    print ('NORMAL')
elif  25<IMC<=30:
    print ('SOBREPESO')
elif  30<IMC<=40:
    print ('OBESIDADE')
elif  IMC>40:
    print ('OBESIDAD GRAVE')

