# -*- coding: utf-8 -*-
P = float (input ('DIGITE O VALOR DO PESO: '))
A = float (input ('DIGITE O VALOR DA SUA ALTURA: '))

imc = ((P)/(A*A))

if imc < 20 :
    print('ABAIXO')
elif 20<= imc <= 25 :
    print('NORMAL')
elif 25< imc <= 30 :
    print('SOBREPESO')
elif 30< imc <= 40 :
    print('OBESIDADE')
else :
    print('OBESIDADE GRAVE')
    

