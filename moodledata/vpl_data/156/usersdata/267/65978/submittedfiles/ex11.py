# -*- coding: utf-8 -*-
#ENTRADA
print('Informe od dados da primeira data:')
dia1 = int(input('Dia: '))
mes1 = int(input('Mês: '))
ano1 = int(input('Ano: '))
print()
print('Informe od dados da segunda data:')
dia2 = int(input('Dia: '))
mes2 = int(input('Mês: '))
ano2 = int(input('Ano: '))
#PROCESSAMENTO
data1 = dia1+mes1*30+ano1*365
data2 = dia2+mes2*30+ano2*365
if data1==data2:
    print('IGUAIS')
elif data1>data2:
    print('DATA 1')
else:
    print('DATA 2')
