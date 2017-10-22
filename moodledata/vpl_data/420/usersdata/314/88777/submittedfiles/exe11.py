# -*- coding: utf-8 -*-
soma=0

n=int(input('Digite um numero com 8 digitos: '))
while(n<=99999999 and n>=10000000):
    n=n%10%10
    print(n)
   