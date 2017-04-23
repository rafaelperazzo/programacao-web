# -*- coding: utf-8 
dia1=int(input('dia 1'))
mes1=int(input('mês 1'))
ano1=int(input('ano 1'))
dia2=int(input('dia 2'))
mes2=int(input('mês 2'))
ano2=int(input('ano 2'))
if ano1>ano2:
    print(data1)
elif ano2>ano1:
    print(data2)
else:
    if mes1>mes2:
        print(data1)
    elif mes2>mes1:
        print(data2)
    else:
        if dia1>dia2:
            print(data1)
        elif dia2>dia1:
            print(data2)
        else:
            print(iguais)