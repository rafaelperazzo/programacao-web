# -*- coding: utf-8 -*-
peso=float(input('Digite o peso em kg:'))
altura=float (input('Digite a altura em metros :'))

IMC=(peso)/(altura * altura)

if IMC<20:
    print('Abaixo')
    
if    20<=IMC<=25:
        print('Normal')
        
if    25<IMC<=30:
        print('Sobrepeso')
        
if    30<IMC<=40:
        print('obesidade')
        
if       IMC>40:
        print('Obesidade Grave')
        


