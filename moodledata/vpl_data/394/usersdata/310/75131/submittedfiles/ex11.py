# -*- coding: utf-8 -*-

dia1 = int(input('Digite o dia1: ' ))
mes1 = int(input('Digite o mes1: ' ))
ano1 = int(input('Digite o ano1: ' ))

dia2 = int(input('Digite o dia2: ' ))
mes2 = int(input('Digite o mes2: ' ))
ano2 = int(input('Digite o ano2: ' ))

if ano1 < ano2:
    print('DATA 2')
elif ano1 > ano2:
    print('DATA 1')
else :
    if mes1 < mes2:
        print('DATA 2')
    elif mes1 > mes2:
        print('DATA 1')
    else:
        if dia1 < dia2:
            print('DATA 2')
        elif dia1 > dia2:
            print('DATA 1')
        else:
            print('IGUAIS')