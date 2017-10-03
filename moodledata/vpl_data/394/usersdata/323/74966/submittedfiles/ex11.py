# -*- coding: utf-8 -*-
Dia = int(input('Dia 1: '))
Mes = int(input('Mês 1: '))
Ano = int(input('Ano 1: '))
Dia2 = int(input('Dia 2: '))
Mes2 = int(input('Mês 2: '))
Ano2 = int(input('Ano 2: '))
if Ano==Ano2 and Mes==Mes2 and Dia==Dia2:
    print ('IGUAIS')
elif Ano>=Ano2 and Mes>=Mes2 and Dia>=Dia2:
    print('DATA 1')
else:
    print('Data 2')
