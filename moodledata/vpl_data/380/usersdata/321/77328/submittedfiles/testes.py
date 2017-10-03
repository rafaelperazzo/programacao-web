# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a= float(input('Digite um número: '))
b= float(input('Digite outro número: '))
c= float(input('Digite outro número: '))
d= float(input('Digite outro número: '))

if a > b and a > c and a > d :
    print ('%.f é maior' % a)
else :
    print ('%.f é menor' % a)
    
if b > a and b > c and b > d :
    print('%.f é maior' % b)
else:
    print('%.f é menor' % b)
        
if c > a and c > b and c > d :
    print('%.f é maior' % c)
else :
    print('%.f é menor' % c)

if d > a and d > b and d > c :
    print('%.f é maior' % d)
else :
    print('%.f é menor' % d)