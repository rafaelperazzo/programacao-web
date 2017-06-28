# -*- coding: utf-8 -*-

n=int(input('digite um numero de quatro digitos:'))
x=n//100
y=n%100
a=x//10
b=x%10
l=(b*10)+a
if (l*y)==a:
    print('Vampiro')
else:
    print('Não')
    