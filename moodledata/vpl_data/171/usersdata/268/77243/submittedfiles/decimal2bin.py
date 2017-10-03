# -*- coding: utf-8 -*-
n=int(input('Digite n : '))
i=0
soma=0
while (n>0):
    trans= n*2**i
    soma = soma + trans
    n=n//10
    i=i+1
print (soma)
    

