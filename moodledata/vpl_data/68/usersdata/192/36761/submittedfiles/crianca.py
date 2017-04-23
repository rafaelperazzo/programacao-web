# -*- coding: utf-8 -*-

p1=float(input('digite peso do lado esquerdo:'))
c1=float(input('digite compriento da lado esquerdao:'))
p2=float(input('digite peso da lado direito:'))
c2=float(input('digite pesa do compimento:'))
if((p1*c1)>(p2*c2)):
    print('-1')
elif(p1*c2)<(p2*c2)):
    print('1')
else:
    print('0')
    