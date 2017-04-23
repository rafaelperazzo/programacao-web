# -*- coding: utf-8 -*-
p1=float(input('digite o peso da crianca da esquerda:'))
c1=float(input('digite o comprimento da gangorra do lado esquerdo:'))
p2=float(input('digite o peso da crianca da direito:'))
c2=float(input('digite o comprimento da gangorra do lado direito:'))
a=p1*c1
b=p2*c2

if(a==b):
    print('0')
elif(a>b):
    print('-1')
else:
    print('1')
    


