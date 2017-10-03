# -*- coding: utf-8 -*-
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: ')) 
c = int(input('Digite o valor de c: '))
if a > b > c or b > a > c:
    print('%d' %c)
elif a > c > b or c > a > b:
    print('%d' %b)    