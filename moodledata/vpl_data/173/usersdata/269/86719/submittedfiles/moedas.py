# -*- coding: utf-8 -*-
a=int(input('digite: '))
b=int(input('digite: '))
c=int(input('digite: '))


for qa in range (0,c,1):
    if (((c-(qa*a))%b)==0):
        print(qa)
        qb=(c-(qa*a))//b
        print(qb)
        break
    else:
        print('N')
    
