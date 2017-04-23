# -*- coding: utf-8 -*-
p1=float(input('Digite o peso da criança1:'))
c1=float(input('Digite o comprimento 1:'))
p2=float(input('Digite o peso da criança2:'))
c2=float(input('Digite o comprimento 2:'))

fator1=p1*c1
fator2=p2*c2

if fator1==fator2:
    print('0')
    
if fator1>fator2:
    print('-1')
    
if fator1<fator2:
    print('1')



