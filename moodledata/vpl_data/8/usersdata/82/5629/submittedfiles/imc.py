# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA
peso = input ('Digite o peso em kg:')
altura = input ('Digite a altura em metros:')

#PROCESSAMENTO E SAIDA
IMC== (peso)//((altura)**2)

if IMC<20:
    print ('ABAIXO')
else:
    if 20<=IMC<=25:
        print ('NORMAL')
    else:
        if 25<IMC<=30:
            print ('SOBREPESO')
        else:
            if 30<IMC<=40:
                print ('OBESIDADE')
            else:
                if IMC>40:
                    print ('OBESIDADE GRAVE')
                
    
