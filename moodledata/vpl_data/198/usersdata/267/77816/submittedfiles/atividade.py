# -*- coding: utf-8 -*-
n=int(input('Digite n: '))
cont=0
while n/10>=1 or n/10<=-1:
    n=n/10
    cont=cont+1
print(cont)