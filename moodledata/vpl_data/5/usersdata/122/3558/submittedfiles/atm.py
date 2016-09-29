# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA

vs=int(input('digite o valor a ser sacado:'))

#PROCESSAMENTO

ceduladevinte=int(vs/20)
ceduladedez=int((vs%20)/10)
ceduladecinco=int(((vs%20)%10)/5)
ceduladedois=int((((vs%20)%10)%5)/2)
ceduladeum=int(((((vs%20)%10)%5)/2)/1)

#SAÍDA

print(ceduladevinte)
print(ceduladedez)
print(ceduladecinco)
print(ceduladedois)
print(ceduladeum)