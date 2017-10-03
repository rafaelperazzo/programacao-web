# -*- coding: utf-8 -*-
dia01=int(input('Digite o dia 01: '))
mes01=int(input('Digite o mes 01: '))
ano01=int(input('Digite o ano 01: '))
dia02=int(input('Digite o dia 02: '))
mes02=int(input('Digite o mes 02: '))
ano02=int(input('Digite o ano 02: '))

Data 01=(dia01/365.0)+(mes01/12.0)+ano01
Data 02=(dia02/365.0)+(mes02/12.0)+ano02

if Data 01>Data 02:
    print ('DATA 01')
elif Data 02>Data 01:
    print ('DATA 02')
else :
    print ('IGAUAL')

