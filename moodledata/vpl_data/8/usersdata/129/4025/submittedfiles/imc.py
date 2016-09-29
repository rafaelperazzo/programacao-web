# -*- coding: utf-8 -*-
from __future__ import division
import math
P= input('Digite o seu peso em kilos: ')
A= input('Digite a sua altura em metros: ')
IMC= P/(A**2)
if IMC<20:
    print ('ABAIXO')
elif 20<=IMC<=25:
    print ('NORMAL')
elif 25<IMC<=30:
    print ('SOBREPESO')
elif 30<IMC<=40:
    print ('OBESIDADE')
else :
    print ('OBESIDADE GRAVE')