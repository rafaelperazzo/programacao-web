# -*- coding: utf-8 -*-
n= int(input('Digite o valor de n:'))
expoente=0
soma=0
while (n/2>0):
    resto= n%2
    soma= soma+(resto*(10**expoente))
    expoente= expoente+1
    n= n//2
print (soma)