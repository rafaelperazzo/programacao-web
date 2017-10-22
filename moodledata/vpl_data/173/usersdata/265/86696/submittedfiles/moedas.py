# -*- coding: utf-8 -*-
a = int(input('digite o valor de a: '))
b = int(input('digite o valor de b: '))
c = int(input('digite o valor de c: '))
for qa in range (0,c,1):
    if (((c-(qa*a))%b==0):
        print(qa)
        qb=(c-(qa*a))//b
        print(qb)
        break
    else:
        print('N')