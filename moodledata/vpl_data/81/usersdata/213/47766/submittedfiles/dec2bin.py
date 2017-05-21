# -*- coding: utf-8 -*-
p=int(input('Informe o 1° número: '))
q=int(input('Informe o 2° número: '))

x=q
quantDigitos=0
while x>0:
    x=x//10
    quantDigitos=quantDigitos+1
print(quantDigitos)

