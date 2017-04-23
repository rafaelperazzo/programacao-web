# -*- coding: utf-8 -*-
d1=int(input('Digite o primeiro dia: '))
m1=int(input('Digite o primeiro mês: '))
a1=int(input('Digite o primeiro ano: '))
d2=int(input('Digite o segundo dia: '))
m2=int(input('Digite o segundo mês: '))
a2=int(input('Digite o segundo ano: '))
if a1>a2:
    print('Primeiro ano')
elif a1<a2:
    print('Segundo ano')
else:
    if m1>m2:
        print('Primeiro mês')
    elif m1<m2:
        print('Segundo mês')
    else:
        if d1>d2:
            print('Primeiro dia')
        elif d1<d2:
            print('Segundo dia')
        else:
            print('Datas iguais')
            


