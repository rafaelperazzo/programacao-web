# -*- coding: utf-8 -*-

p=int(input('Digite p: '))
q=int(input('Digite q: '))

digitos=p
cont=0
while (digitos>0):
    digitos=digitos//10
    cont=cont+1
    
numero=q
while (numero>0):
    if (numero==p):
        print('S')
    else:
        print('N')
    numero=numero%(10**cont)    