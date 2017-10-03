# -*- coding: utf-8 -*-
dia1= int(input('Digite o Dia:'))
mes1= int(input('Digite o Mes:'))
ano1= int(input('Digite o Ano:'))
dia2= int(input('Digite o Dia:'))
mes2= int(input('Digite o Mes:'))
ano2= int(input('Digite o Ano:'))
data1=dia1+(mes1*30)+ano1*365
data2=dia2+(mes2*30)+ano2*365
if(data1==data2):
    print('IGUAIS')
else:
    if (data1>data2):
        print('Data1')
    else:
        print ('Data2')
        