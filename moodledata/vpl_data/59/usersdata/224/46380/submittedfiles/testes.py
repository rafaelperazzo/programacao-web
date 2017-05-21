# -*- coding: utf-8 -*-
d1=intt(input('Digite o valor d1: '))
m1=int(input('Digite o valor m1: '))  
a1=int(input('Digite o valor a1: '))  
d2=intt(input('Digite o valor d2: '))
m2=int(input('Digite o valor m2: '))  
a2=int(input('Digite o valor a2: '))  
if a1>a2:
    print('%d/%d/%d'%(d1,m1,a1))
elif a2>a1:
    print('%d/%d/%d'%(d2,m2,a2))
else:
    if m1>m2:
        print('%d/%d/%d'%(d1,m1,a1))
    elif m2>m1:
        print('%d/%d/%d'%(d2,m2,a2))
    else:
        if d1>d2:
            print('%d/%d/%d'%(d1,m1,a1))
        elif d2>d1:
            print('%d/%d/%d'%(d2,m2,a2))
            else:
                print('São Iguais')