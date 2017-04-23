# -*- coding: utf-8 -*-
Dia1=int(input('digite dia1:'))
Mes1=int(input('digite mes1:'))
Ano1=int(input('digite ano1:'))
Dia2=int(input('digite dia2:'))
Mes2=int(input('digite mes2:'))
Ano2=int(input('digite ano2:'))
if Dia1>Dia2:
    print('DATA 1')
elif Dia1<Dia2:
    print('DATA 2')
else:
    if Mes1>Mes2:    
        print('DATA 1')
    elif Mes1<Mes2:
        print('DATA 2')
    else: 
        if Ano1>Ano2:
            print('DATA 1')
        elif Ano1<Ano2:
            print('DATA 2')
        else:
            print('IGUAIS')