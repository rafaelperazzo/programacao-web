# -*- coding: utf-8 -*-
dia1= int(input('Digite o Dia:'))
mes1= int(input('Digite o Mes:'))
ano1= int(input('Digite o Ano:'))
dia2= int(input('Digite o Dia:'))
mes2= int(input('Digite o Mes:'))
ano2= int(input('Digite o Ano:'))
data1=(dia1/365)+(mes1/365)+ano1
data2=(dia2/365)+(mes2/365)+ano2
if(data1==data2):
    print('IGUAIS')
else:
    if (data1>data2):
        print('Data1')
    else:
        print ('Data2')
        