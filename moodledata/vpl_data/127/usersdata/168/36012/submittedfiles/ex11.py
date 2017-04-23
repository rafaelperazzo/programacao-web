# -*- coding: utf-8 -*-
d1=int(input('Digite o primeiro dia: '))
m1=int(input('Digite o primeiro mês: '))
a1=int(input('Digite o primeiro ano: '))
d2=int(input('Digite o segundo dia: '))
m2=int(input('Digite o segundo mês: '))
a2=int(input('Digite o segundo ano: '))
if a1>a2:
    print('Primeira data')
elif a1<a2:
    print('Segunda data')
else:
    if m1>m2:
        print('Primeira data')
    elif m1<m2:
        print('Segunda data')
    else:
        if d1>d2:
            print('Primeira data')
        elif d1<d2:
            print('Segunda data')
        else:
            print('Datas iguais')
            


