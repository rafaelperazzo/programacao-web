# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI

s = int(input('digite valor que deseja sacar:'))

#cedulas disponíveis
cedula1=20
cedula2=10
cedula3=5
cedula4=2
cedula5=1

saq1= s/cedula1
saq2= saq1/cedula2 
saq3= saq2/cedula3
saq4= saq3/cedula4
saq5= saq4/cedula5
print ('%.i' %saq1)
print ('%.i' %saq2)
print ('%.i' %saq3)
print ('%.i' %saq4)
print ('%.i' %saq5)
