# -*- coding: utf-8 -*-
ano1=int(input('Informe o ano da primeira data'))
mes1=int(input('Informe o mes da primeira data'))
dia1=int(input('Informe o dia da primeira data'))
ano2=int(input('Informe o ano da segunda data'))
mes2=int(input('Informe o mes da segunda data'))
dia2=int(input('Informe o dia da segunda data'))

if ano1>ano2:
    print('DATA1')
elif ano1<ano2:
    print('DATA2')
else:
    if mes1>mes2:
        print('DATA1')
    elif mes1<mes2:
        print('DATA2')
    else:
        if dia1>dia2:
            print('DATA1')
        elif dia1<dia2:
            print('DATA2')
        else:
            print('IGUAIS')