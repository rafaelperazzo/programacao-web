# -*- coding: utf-8 -*-
import math
#COMECE A PARTIR DAQUI!
sb = float(input('digite o valor de sb: '))
Ir = 0.11*sb
print('%.2f' %Ir)
INSS = 0.08*sb
print('%.2f' %INSS)
Sind = 0.05*sb
print('%.2f' %Sind)
sl = (sb - (Ir + INSS + Sind))
print('%.2f' %sl)