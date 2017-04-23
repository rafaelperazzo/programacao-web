# -*- coding: utf-8 -*-
d1=int(input('Digita dia1 :'))
m1=int(input('Digita mes1 :'))
a1=int(input('Digita ano1 :'))
d2=int(input('Digita dia2 :'))
m2=int(input('Digita mes2 :'))
a2=int(input('Digita ano2 :'))
if a1>a2:
    print('%d/%d/%d'% (d1,m1,a1))
elif a1<a2:
    print('Data 2')
else:
    if m1>m2:
        print('Data 1')
    elif m1<m2:
        print('Data 2')
    else:
    if a1>a2:
        print('Data 1')
    elif a1<a2:
        print('Data 2')
    else print('iguais')
        
