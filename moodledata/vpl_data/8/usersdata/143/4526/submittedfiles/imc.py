# -*- coding: utf-8 -*-
from __future__ import division
peso = input(' Informe seu peso em quilogramas: ')
altura = input(' Informe sua altura em metros: ')

imc =  peso/(altura*altura)

if imc<20:
    print( 'Abaixo ')
elif imc>=20 and imc<=25:
    print( ' Normal ')
elif imc>25 and imc<=30:
    print( ' Sobrepeso ')
elif imc>30 and imc<=40:
    print( ' Obesidade ')
else:
    print( ' Obesidade grave ')
    