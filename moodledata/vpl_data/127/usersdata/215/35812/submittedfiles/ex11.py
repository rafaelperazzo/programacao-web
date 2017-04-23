# -*- coding: utf-8 -*-
d1=int(input('digite o dia 1'))
m1=int(input('digite o mes 1'))
a1=int(input('digite o ano 1'))
d2=int(input('digite o dia 2'))
m2=int(input('digite o mes 2'))
a2=int(input('digite o ano 2'))
if a1==a2 and m1==m2 and d1==d2:
    print ('IGUAIS')
elif a1>a2 and m1>m2 and d1>d2:
    print ('DATA 1')
elif a1>a2 and m2>m1 and d1>d2:
    print ('DATA 1') 
elif a1>a2 and m2>m1 and d2>d1:
    print ('DATA 1')
else:
    print ('DATA 2')
