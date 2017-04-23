# -*- coding: utf-8 -*-

d1=float(input('(DATA 1)Digite o dia: '))
m1=float(input('(DATA 1)Digite o mês: '))
a1=float(input('(DATA 1)Digite o ano: '))
d2=float(input('(DATA 2)Digite o dia: '))
m2=float(input('(DATA 2)Digite o mês: '))
a2=float(input('(DATA 2)Digite o ano: '))
if(a1>a2):
    print('DATA 1")
elif(a1<a2):
    print('DATA 2")
elif(a1==a2)and(m1>m2):
    print('DATA 1")
elif(a1==a2)and(m1<m2):
    print('DATA 2")
elif(a1==a2)and(m1==m2)and(d1>d2):
    print('DATA 1")
elif(a1==a2)and(m1==m2)and(d1<d2):
    print('DATA 2")
else:
    print('IGUAIS')