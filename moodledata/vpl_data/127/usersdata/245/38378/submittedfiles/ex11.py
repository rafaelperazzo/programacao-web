# -*- coding: utf-8 -*-
a1=int(input('Digite o ano 1:'))
m1=int(input('Digite o mes 1:'))
d1=int(input('Digite o dia 1:'))
a2=int(input('Digite o ano 2:'))
m2=int(input('Digite o mes 2:'))
d2=int(input('Digite o dia 2:'))
if a1>a2:
    print('%d%d%d'%(d1,m1,a1))
elif a1<a2:
    print('%d%d%d'%(d2,m2,a2))
else:
    if m1>m2:
        print('%d%d%d'%(d1,m1,a1))
    elif m1<m2:
        print('%d%d%d'%(d2,m2,a2))
    else:
        if d1>d2:
            print('%d%d%d'%(d1,m1,a1))
        elif d1<d2:
            print('%d%d%d'%(d2,m2,a2))
        else:
            print('IGUAIS')