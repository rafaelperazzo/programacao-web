# -*- coding: utf-8 -*-
peso=float(input('Digite seu peso: '))
altura=float(input('Digite sua altura: '))
IMC=peso/altura*2
if IMC <20:
    print('Baixo')
elif IMC>=20 and IMC <=25:
    print('Normal')
elif IMC>25 and IMC<=30:
    print('Sobrepeso')

