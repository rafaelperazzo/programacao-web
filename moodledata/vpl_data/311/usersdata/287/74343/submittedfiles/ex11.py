# -*- coding: utf-8 -*-
d1= int(input('Digite o dia da primeira data: '))
m1= int(input('Digite o mês da primeira data: '))
a1= int(input('Digite o ano da primeira data: '))
d2= int(input('Digite o dia da segunda data: '))
m2= int(input('Digite o mês da segunda data: '))
a2= int(input('Digite o ano da segunda data: '))
if a1>a2:
    print('DATA 1')
if a1<a2:
    print('DATA 2')
if a1=a2 and m1>m2:
    print('DATA 1')
if a1=a2 and m1<m2:
    print('DATA 2')
if a1=a2 and m1=m2 and d1>d2:
    print('DATA 1')
if a1=a2 and m1=m2 and d1<d2:
    print('DATA 2')
if a1=a2 and m1=m2 and d1=d2:
    print('IGUAIS')
        
    


