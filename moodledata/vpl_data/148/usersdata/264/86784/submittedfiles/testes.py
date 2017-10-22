# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n= int(input('Digite o numero:'))
expoente=0
soma=0
while n/2>0:
    resto= n%2
    soma= soma  + (resto*(10**expoente))
    expoente= expoente+1
print(soma)