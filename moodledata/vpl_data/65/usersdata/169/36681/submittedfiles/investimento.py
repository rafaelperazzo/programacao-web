 # -*- coding: utf-8 -*-
from __future__ import division
investimento=float(input('Digite o Valor do Investimento Inicial:'))
t=float(input('Digite a Taxa de Juros Anual:'))
M1=investimento*t+investimento
M2=M1*t+M1
M3=M2*t+M2
M4=M3*t+M3
M5=M4*t+M4
M6=M5*t+M5
M7=M6*t+M6
M8=M7*t+M7
M9=M8*t+M8
M10=M9*t+M9
print('%.2f' %M1)
print('%.2f' %M2)
print('%.2f' %M3)
print('%.2f' %M4)
print('%.2f' %M5)
print('%.2f' %M6)
print('%.2f' %M7)
print('%.2f' %M8)
print('%.2f' %M9)
print('%.2f' %M10)