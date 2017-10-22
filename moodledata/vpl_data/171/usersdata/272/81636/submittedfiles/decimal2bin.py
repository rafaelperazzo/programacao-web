# -*- coding: utf-8 -*-

n= int(input('Digite o número binário: '))
cont=0
while ((n//10)>0):
    a=n%10
    b=a*(2**cont)
    cont=cont+1
    n=n//10
    print(b)