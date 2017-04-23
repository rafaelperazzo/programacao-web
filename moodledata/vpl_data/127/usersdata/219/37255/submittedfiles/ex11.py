# -*- coding: utf-8 -*-
d1=int(input('dia1 :'))
m1=int(input('mes1 :'))
a1=int(input('ano1 :'))
d2=int(input('dia2 :'))
m2=int(input('mes2 :'))
a2=int(input('ano2 :'))
if a1>a2:
    print('%d/%d/%d'% (d1,m1,a1))
elif a1<a2:
    print('DATA 2')
else:
    if m1>m2:
        print('DATA 1')
    elif m1<m2:
        print('DATA 2')
    else:
         if d1>d2:
            print('DATA 1')
         elif d1<d2:
            print('DATA 2')
         else:
             print('IGUAIS')
        
