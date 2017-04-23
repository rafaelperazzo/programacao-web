# -*- coding: utf-8 -*-
ano1=int(input('digite o ano da primeira data:'))
mes1=int(input('digite o mês da primeira data:'))
dia1=int(input('digite o dia da primeira data:'))
ano2=int(input('digite o ano da primeira data:'))
mes2=int(input('digite o mês da primeira data:'))
dia2=int(input('digite o dia da primeira data:'))
data1=(ano1*100000)+(mes1*1000)+(dia1)
data2=(ano2*100000)+(mes2*1000)+(dia2)
if data2<data1:
    print('DATA1')
elif data1<data2:
    print('DATA2')
else:
    print('iguais')
