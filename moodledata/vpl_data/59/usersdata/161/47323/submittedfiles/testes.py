# -*- coding: utf-8 -*-
d1=int(input('d1:'))
m1=int(input('m1:'))
ano1=int(input('ano1:'))
d2=int(input('d2:'))
m2=int(input('m2:'))
ano2=int(input('ano2:'))
if ano1<ano2:
    print(d2,m2,ano2)
elif ano1>ano2:
    print('data1')
else:
    if m1<m2:
        print('data2')
    elif m1>m2:
        print('data1')
    else:    
        if d1<d2:
            print('data2')
        elif d1>d2:
            print('data1')    
        else:
            print('iguais')