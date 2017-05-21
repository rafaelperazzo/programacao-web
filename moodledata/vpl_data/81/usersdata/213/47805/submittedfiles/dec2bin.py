# -*- coding: utf-8 -*-
p=int(input('Informe o 1° número: '))
q=int(input('Informe o 2° número: '))

x=p
quantDigitos=0
while x>0:
    x=x//10
    quantDigitos=quantDigitos+1

contador=0
while q>0:
    resto=q%10**(quantDigitos)
    if resto==p:
        contador=contador+1
    q=q//10

if contador!=0:
    print('S')
else:
    print('N')