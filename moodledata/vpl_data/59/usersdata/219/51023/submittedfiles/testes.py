# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
d1=int(input('Digite o dia:'))
m1=int(input('Digite o mês:'))
a1=int(input('Digite o ano:'))
d2=int(input('Digite o dia:'))
m2=int(input('Digite o mês:'))
a2=int(input('Digite o ano:'))
if a1>a2:
    print('Data 1')
elif a1<a2:
    print('Data 2')
else:
    if m1>m2:
        print('Data 1')
    elif m1<m2:
        print('Data 2')
    else:
        if d1>d2:
            print('Data 1')
        elif d1<d2:
            print('Data 2')
        else:
            print('IGUAIS')
    
        

       