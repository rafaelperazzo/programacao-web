# -*- coding: utf-8 -*-

n = int(input('digite algarismo de 8 digitos: '))
t = 10000000
soma = 0
if n>9999999 ande n<100000000:
    for i in range(0,8,1):
        soma = soma+(n//t)
        n=n%t
        t=t/10
        
else:
    print ('NAO SEI'))
    
print (soma)
        





















