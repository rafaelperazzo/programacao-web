# -*- coding: utf-8 -*-
dia1=int(input('Informe o dia 1:'))
mes1=int(input('Informe o mes 1:'))
ano1=int(input('Informe o ano 1:'))
dia2=int(input('Informe o dia 2:'))
mes2=int(input('Informe o mes 2:'))
ano2=int(input('Informe o ano 2:'))

if (ano1==ano2)and (mes1==mes2)and(dia1==dia2):
    print('IGUAIS')
elif(ano1<=ano2)and(mes1<=mes2)and(dia1<=dia2):
    print('DATA 2')
else:
        print('DATA 1')
