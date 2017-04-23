# -*- coding: utf-8 -*-
dia1=int(input('Dia 1: '))
mes1=int(input('Mês 1: '))
ano1=int(input('Ano 1: '))
dia2=int(input('Dia 2: '))
mes2=int(input('Mês 2: '))
ano2=int(input('Ano 2: '))
if ano1>ano2:
    print('DATA 1')
elif mes1>mes2:
    print('DATA 1')
elif dia1>dia2:
    print('DATA 1')
elif ano1=ano2 and mes1=mes2 and dia1=dia2:
    print('IGUAIS')
else:
    print('DATA 2')