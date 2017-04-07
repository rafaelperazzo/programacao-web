# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
dia1=float(input('digite dia:'))
mes1=float(input('digite mes:'))
ano1=float(input('digite ano:'))
dia2=float(input('digite dia:'))
mes2=float(input('digite mes:'))
ano2=float(input('digite ano:'))
if dia1>dia2:
    dd=dia1
else: dd=dia2
if mes1>mes2 and dia1>dia2:
    mm=mes1
else: dd=mes2
if ano1>ano2 and dia1>dia2 and mes1>mes2:
    aa=ano1
else: dd=ano2
print(dd)
print(mm)
print(aa)
    
    