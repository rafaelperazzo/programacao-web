# -*- coding: utf-8 -*-
dia1 = int(input('digite dia1'))
mes1 = int(input('digite mes1'))
ano1 = int(input('digite ano1'))
dia2 = int(input('digite dia2'))
mes2 = int(input('digite mes2'))
ano2 = int(input('digite ano2'))
if (dia1==dia2) and (mes1==mes2) and (ano1==ano2):
    print('IQUAIS')
elif (dia1<=dia2) and (mes1<=mes2) and (ano1<=ano2):
    print('DATA 2')
else:
    print('DATA 1')
