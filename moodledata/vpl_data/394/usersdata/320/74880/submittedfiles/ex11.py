# -*- coding: utf-8 -*-

dia1 = int(input('Digite dia1: '))
mes1 = int(input('Digite mes1: '))
ano1 = int(input('Digite ano1: '))
dia2 = int(input('Digite dia2: '))
mes2 = int(input('Digite mes2: '))
ano2 = int(input('Digite ano2: '))

data1 = (dia1/365.0) + (mes1/12.0) + ano1
data2 = (dia2/365.0) + (mes2/12.0) + ano2

if data1>data2:
    print ('DATA 1')
elif data1<data2:
    print('DATA 2')
else:
    print('IGUAIS')