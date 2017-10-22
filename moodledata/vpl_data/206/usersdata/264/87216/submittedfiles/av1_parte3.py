# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n= int(input('Digite o valor de n:'))
i=3
soma=0
contador=0
x=1
while (n<=contador):
    if (x%2)!=0:
        soma= soma+(12**0.5)* (1) - (1)/i*(3**x)
    if (x%2)==0:
        soma= soma+(12**0.5)* (1) + (1)/i*(3**x+1)
    contador= contador+1
    x= x+1
    i= i+2
print (soma)