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
    if (numero%(10**cont)==p):
        print('S')
        break
    else:
        numero=numero//10
        