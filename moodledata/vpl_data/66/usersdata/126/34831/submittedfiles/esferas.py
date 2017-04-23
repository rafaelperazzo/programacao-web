# -*- coding: utf-8 -*-

a= float(input(' digite o peso da esfera 1:'))
b= float(input(' digite o peso da esfera 2:'))
c= float(input(' digite o peso da esfera 3:'))
d= float(input(' digite o peso da esfera 4:'))

if a==b+c+d and b+c==d and b==c:
    print('S')
else:
    print('N')

