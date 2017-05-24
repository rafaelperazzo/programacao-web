# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))
d=int(input('digite o valor de d:')) 

if (a==b+c+d) and (b+c==d) and (b==c):
    print('S')
else:
    print('N')