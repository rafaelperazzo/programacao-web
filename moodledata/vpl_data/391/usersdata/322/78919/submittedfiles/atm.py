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
print('%.i' %saq1)
saqa=(s%cedula1)
print('%.i' %saqa)
