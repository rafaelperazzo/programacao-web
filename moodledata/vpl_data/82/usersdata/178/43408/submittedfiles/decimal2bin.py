# -*- coding: utf-8 -*-

b=int(input('Digite o num binario:'))

soma=0
i=0
while b>0:
    resto=b%10
    soma=soma+(2**i)*resto
    b=b//10
    i=i+1
print (soma)


