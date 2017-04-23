# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
import math
n=int(input('digite n: '))
num=2
den=1
pi=num/den
for i in range(1,n-1,2):
    den=den+i
    pi=2*pi*(num/den)
    num=num+i
    pi=2*pi*(num/den)
print('%.5f'%pi)