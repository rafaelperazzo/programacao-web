# -*- coding: utf-8 -*-
dia1=int(input('Digite o primeiro dia: '))
mes1=int(input('Digite o primeiro mês: '))
ano1=int(input('Digite o primeiro ano: '))
dia2=int(input('Digite o segundo dia: '))
mes2=int(input('Digite o segundo mês: '))
ano2=int(input('Digite o segundo ano: '))
if ano1>ano2:
    print('data1')
elif ano1<ano2:
    print('data2')
else:
    if mes1>mes2:
        print('data1')
    elif mes1<mes2:
        print('data2')
    else:
        if dia1>dia2:
            print('data1')
        elif dia1<dia2:
            print('data2')
        else:
            print('Datas iguais')
            


