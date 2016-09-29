# -*- coding: utf-8 -*-
from __future__ import division
p = ('Digite o peso: ')
h = ('Digite a altura: ')
IMC = (p)/(h**2)
if IMC < 20:
    print('ABAIXO')
    elif 20 <= IMC <= 25:
        print('NORMAL')
        elif 25 <= IMC <= 30:
            print('SOBREPESO')
            elif 30 <= IMC <= 40:
                print('OBESIDADE')
                elif IMC > 40:
                    print('OBESIDADE GRAVE')