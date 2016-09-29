# -*- coding: utf-8 -*-
from __future__ import division

M=input('digite o peso:')
H=input('digite a altura:')
IMC=(M)/(H**2)
if IMC<20:
    print('ABAIXO')
elif IMC>=20 and IMC<=25:
    print('NORMAL')
elif IMC>25 and IMC<=30:
    print('SOBREPESO')
elif IMC>30 and IMC<=40:
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE')
    

