# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

n = int(input('Digite o valor de n: '))
soma = 0
while (n>0):
    ultimo = n%10
    soma = soma +ultimo
    n = n//10
    
print (soma)

