# -*- coding: utf-8 -*-
a1=int(input('Digite o ano 1:'))
m1=int(input('Digite o mes 1:'))
d1=int(input('Digite o dia 1:'))
a2=int(input('Digite o ano 2:'))
m2=int(input('Digite o mes 2:'))
d2=int(input('Digite o dia 2:'))
data1=('%d%d%d'%((d1)(/),(m1)(/),(a1)))
data2=('%d%d%d'%((d2),(m2),(a2)))
if a1>a2:
    print(data1)
elif a1<a2:
    print(data2)
else:
    if m1>m2:
        print(data1)
    elif m1<m2:
        print(data2)
    else:
        if d1>d2:
            print(data1)
        elif d1<d2:
            print(data2)
        else:
            print('IGUAIS')