# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite n: '))
num=2
den=1
pi=1
for i in range(1,n+1,1):
    pi=pi*(num/den)
    den=den+2
    pi=pi*(num/den)
    num=num+2
pi=pi*2
print('%.5f'%pi)