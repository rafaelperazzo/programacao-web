# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
V=int(input('Digite um valor a ser sacado: '))
cedula1=int(V/20)
resto1=(V-(cedula1*20))
if resto1==0:
    cedula2=0
else:
    cedula2=(resto1/10)
    resto2=(resto1-(cedula2*10))
if resto2==0:
    cedula3=0
else:
    cedula3=(resto2/5)
    resto3=(resto2-(cedula3*5))
if resto3==0:
    cedula4=0
else:
    cedula4=(resto3/2)
    resto4=(resto3-(cedula4*2))
if resto4==0:
    cedula5=0
else:
    cedula5=(resto4/1)
    resto5=(resto4-(cedula5*1))
print cedula1
print cedula2
print cedula3
print cedula4
print cedula5