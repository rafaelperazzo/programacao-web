# -*- coding: utf-8 -*-

p1= float(input(' digite o peso da criança da esquerda:'))
c1= float(input(' digite o cumprimento da gangorra da esquerda:'))
p2= float(input(' digite o peso da criaça da direia:'))
c2= float(input(' digite o cumprimento da gangorra da direita:'))

if (p1*c1)==(p2*c2):
    print('0')
elif (p1*c1)>(p2*c2):
    print('-1')
elif (p1*c1)<(p2*c2):
    print('1')
