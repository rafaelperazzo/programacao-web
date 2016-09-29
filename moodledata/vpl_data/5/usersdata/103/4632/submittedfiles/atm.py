# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
v=input('Informe o valor a ser sacado em reais:')
N1=v//20
N2=(v%20)//10
N3=((v%20)%10)//5
N4=(((v%20)%10)%5)//2
N5=((((v%20)%10)%5)%2)//1
print('N1')
print('N2')
print('N3')
print('N4')
print('N5')