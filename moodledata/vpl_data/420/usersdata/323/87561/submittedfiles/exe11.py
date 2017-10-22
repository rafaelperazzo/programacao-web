# -*- coding: utf-8 -*-

Numero=int(input(' '))
if Numero//10000000 < 1:
    print ('NAO SEI')
else:
    soma=0
    
    
    while Numero>0:
        ultimo= Numero%10
        soma = soma + ultimo
        Numero = Numero//10
    print(soma)