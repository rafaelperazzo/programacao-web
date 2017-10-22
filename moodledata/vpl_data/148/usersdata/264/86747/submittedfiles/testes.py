# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
b= int(input('Digite o número binário:'))
contador= 0
r=0
while b//10>0:
    r=r + b//10
    contador= contador +1
    b=r 
print (contador)