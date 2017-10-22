# -*- coding: utf-8 -*-

Número=int(input('Digite seu número inteiro com 8 algarismos: '))
if Número//10000000 < 1:
    print ('NÃO SEI')
soma=0

    
while Número>0:
    último= Número%10
    soma = soma + último
    Número = Número//10
print(soma)