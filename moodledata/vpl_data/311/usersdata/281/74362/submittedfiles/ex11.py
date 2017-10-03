# -*- coding: utf-8 -*-
dia1=int(input('Dia 1:'))
mes1=input('Mes 1:')
ano1=input('Ano 1:')
dia2=input('Dia 2:')
mes2=input('Mes 2:')
ano2=input('Ano 2:')
Data1=dia1+mes1+ano1
Data2=dia2+mes2+ano2
if Data1>Data2:
    print('DATA 1')
elif Data1<Data2:
    print('DATA 2')
else:
    print('Iguais')