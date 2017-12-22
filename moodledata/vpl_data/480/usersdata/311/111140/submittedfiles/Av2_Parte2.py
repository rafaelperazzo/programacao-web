# -*- coding: utf-8 -*-
a=int(input('Digite o numero: '))
c=0
while a>0 :
    c=c+(a%10)
    a=a//10
print(c)
    