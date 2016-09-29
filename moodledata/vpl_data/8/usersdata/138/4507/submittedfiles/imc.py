# -*- coding: utf-8 -*-
from __future__ import division
p=input('digite seu peso:')
a=input('digite sua altura:')
imc=p/(a**2)
if imc<20:
    print('abaixo')
elif imc>20 and imc<=40:
    print('sobrepeso')
elif imc>30 and imc<=40:
    print('obesidade')
else:
    print('obesidade grave')
    

