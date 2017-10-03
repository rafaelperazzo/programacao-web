# -*- coding: utf-8 -*-
Dia1 = int(input('Digite o primeiro dia: '))
Mes1 = int(input('Digite o primeiro mês: '))
Ano1 = int(input('Digite o primeiro ano: '))
print('\n')
Dia2 = int(input('Digite o segundo dia: '))
Mes2 = int(input('Digite o segundo mes: '))
Ano2 = int(input('Digite o segundo ano: '))
print('\n')
if Ano1>Ano2:   
    print('Data1')
elif Ano1<Ano2:
    print('Data2')
elif Ano1 == Ano2 and Mes1>Mes2:
    print('Data1')
elif Ano1 == Ano2 and Mes1<Mes2:
    print('Data2')
elif Ano1 == Ano2 and Mes1 == Mes2 and Dia1>Dia2:
    print('Data1')
elif Ano1 == Ano2 and Mes1 == Mes2 == Dia1<Dia2:
    print('Data2')
elif Ano1 == Ano2 and Mes1 == Mes2 == Dia1 == Dia2:
    print('Iguais')
           

