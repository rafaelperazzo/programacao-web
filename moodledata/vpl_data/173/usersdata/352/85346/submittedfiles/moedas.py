# -*- coding: utf-8 -*-

a=int(input('Digite o valor da moeda:'))
b=int(input('Digite o valor da moeda:'))
c=int(input('Digite o valor da cedula:')) 

i=c//a

while i>0:
    troco=(c-(i*a))//b
    if ((i*a) + ((troco)*b))==c:
        break
    i=i-1
print(i)
print(troco)