# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
import math
n=int(input('digite n: '))
num=2
den=1
pi=num/den
for i in range(1,n,2):
    den=den+i
    pi=pi*(num/den)
    num=num+i
    pi=pi*(num/den)
pi=pi/2
print('%.5f'%pi)