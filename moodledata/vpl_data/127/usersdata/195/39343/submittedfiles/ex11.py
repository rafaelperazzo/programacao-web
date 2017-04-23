# -*- coding: utf-8 -*-
dia1=int(input('dia1:'))
mes1=int(input('mes1:'))
ano1=int(input('ano1:'))
dia2=int(input('dia2:'))
mes2=int(input('mes2:'))
ano2=int(input('ano2:'))
if a1>a2:
    print('DATA1')
elif a1<a2:
    print('DATA2')
else:
    if m1>m2:
        print('DATA1')
    elif m1<m2:
        print('DATA2')
    else:
        if d1>d2:
            print('DATA1')
        elif d1<d2:
            print('DATA2')
        else:
            print('IGUAIS')
