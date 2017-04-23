# -*- coding: utf-8 -*-
a1=int(input('digite pessoa 1:'))
m1=int(input('digite pessoa 1:'))
d1=int(input('digite pessoa 1:'))

a2=int(input('digite pessoa 2:'))
m2=int(input('digite pessoa 2:'))
d2=int(input('digite pessoa 2:'))

if(a1>a2):
    print('pessoa 1')
elif(a1<a2):
    print('pessoa 2')
else:
    if(m1>m2):
        print('pessoa 1')
    elif(m1<m2):
        print('pessoa 2')
    else:
        if(d1>d2):
            print('pessoa 1')
        elif(d1<d2):
            print('pessoa 2')
        else:
            print('datas iguais')

