# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=float(input('digite n: '))
den=1
num=2
pi=num/den
for i in range (1,n-1,2):
    num=num+i
    den=den+i
    pi=pi*num/den
    print(pi)