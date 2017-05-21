# -*- coding: utf-8 -*-
num=int(input('digite num:'))
soma=0
i=0
while num>0:
    r=num%10
    soma=soma+r*2**i
    i=i+i
    num=num//10
print (soma)    



