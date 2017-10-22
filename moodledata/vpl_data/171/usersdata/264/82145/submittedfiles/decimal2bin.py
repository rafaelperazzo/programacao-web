# -*- coding: utf-8 -*-
binario= int(input('Digite o número binario:'))
a=0
b= binario
while (binario>0):
    binario= binario//10
    a=a+1

a=a-1
soma=0
for i in range(0,a+1,1):
    algarismo= b//(10**a)
    soma= algarismo*(2**a)+soma
    b=b%(10**a)
    a=a-1
    
print (soma)