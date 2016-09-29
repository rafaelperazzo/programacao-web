# -*- coding: utf-8 -*-
from __future__ import division

peso=input('digite seu peso:')
altura=input('digite sua altura em metros:')

IMC=(peso)/((altura)**2)

if IMC<20:

    print('abaixo')

elif 20<=IMC<=25:

    print('normal')
 
elif 25<IMC<=30:
    
    print('sobrepeso')

elif 30<IMC<=40:

    print('obesidade')

elif IMC>40:

    print('obesidade grave')
    
    
