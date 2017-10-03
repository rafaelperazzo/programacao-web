# -*- coding: utf-8 -*-
dia1=input('Digite o primeiro dia:')
mes1=input('Digite o primeiro mes:')
ano1=input('Digite o primeiro ano:')
dia2=input('Digite o segundo dia:')
mes2=input('Digite o segundo mes:')
ano2=input('Digite o segundo ano:')
Data1=dia1+mes1+ano1
Data2=dia2+mes2+ano2
if Data1>Data2:
    print('DATA 1')
elif Data1<Data2:
    print('DATA 2')
else:
    print('IGUAIS')



