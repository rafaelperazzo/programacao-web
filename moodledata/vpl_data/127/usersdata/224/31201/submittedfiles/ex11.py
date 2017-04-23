# -*- coding: utf-8 -*-
d1=int(input('Digite o primeiro dia: '))
m1=int(input('Digite o primeiro mês: '))
a1=int(input('Digite o primeiro ano: '))
d2=int(input('Digite o segundo dia: '))
m2=int(input('Digite o segundo mês: '))
a2=int(input('Digite o segundo ano: '))
if a1>a2:
    print('%d/%d/%d'%(d1,m1,a1))
elif a1<a2:
    print('%d/%d/%d'%(d2,m2,a2))
else:
    if (m1>m2):
        print('%d/%d/%d'%(d1,m1,a1))
    elif m1<m2:
        print('%d/%d/%d'%(d2,m2,a2))
    else:
        if d1>d2:
            print('%d/%d/%d'%(d1,m1,a1))
        elif d1<d2:
            print('%d/%d/%d'%(d2,m2,a2))
        else:
            print('São Iguais')