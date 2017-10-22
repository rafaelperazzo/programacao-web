# -*- coding: utf-8 -*-

p=int(input('Digite p: '))
q=int(input('Digite q: '))

digitos=p
cont=0
while (digitos>0):
    digitos=digitos//10
    cont=cont+1
print(cont)