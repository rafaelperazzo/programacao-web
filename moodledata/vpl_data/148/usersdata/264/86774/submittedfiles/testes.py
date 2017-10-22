# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
b= int(input('Digite o número binário:'))
b=binario
contador= 0
r=0
while b//10>0:
    r=r + b//10
    contador= contador +1
    b=r 
a=0
soma=0
for i in range (0, contador+1, 1):
    a= binario//(10**contador)
    soma= soma+ a*(2**contador-1)
    binario= binario//(10**a)
    a=a-1
print (soma)