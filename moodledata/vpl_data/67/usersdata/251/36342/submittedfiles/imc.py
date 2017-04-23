# -*- coding: utf-8 -*-
peso = float(input('Digite o seu peso (em kg ): '))
altura = float(input('Digite sua altura (em metros ): '))
imc = (peso/(altura**2))
if imc<20:
    print('ABAIXO')

elif imc>=20 and imc<=25:
    print('NORMAL')
    
elif imc>=25 and imc<=30:
    print('SOBREPESO')
    
elif imc>=30 and imc<=40:
    print('OBESIDADE')    
    
else:
    print('OBESIDADE GRAVE')
