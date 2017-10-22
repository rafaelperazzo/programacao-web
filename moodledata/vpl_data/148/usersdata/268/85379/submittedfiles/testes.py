# -*- coding: utf-8 -*-
d2=float(input('Digite o valor do d : '))
m2=float(input('Digite o valor d m : '))
a2=float(input('Digite o valor d a : '))

d1=float(input('Digite o valor do d : '))
m1=float(input('Digite o valor d m : '))
a1=float(input('Digite o valor d a : '))

if a1>a2:
    print(d1)
    print(m1)
    print(a1)
if a1<a2:
    print(d2)
    print(m2)
    print(a2)
if a1==a2:
    if (m1>m2):
         print(d1)
         print(m1)
         print(a1)
    if (m1<m2):
         print(d2)
         print(m2)
         print(a2)
    if m1==m2:
            if (d1>d2):
                 print(d1)
                 print(m1)
                 print(a1)
            if (d1<d2):
                 print(d2)
                 print(m2)
                 print(a2)
            if (d1==d2):
                print('IGUAIS')
        
        