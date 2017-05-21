# -*- coding: utf-8 -*-
p=int(input('digite o valor do menor número:'))
q=int(input('digite o valor do maior número:'))
n=p
el=0
while (n%10)>0:
    el=el+1
    n=n//10
print(el)