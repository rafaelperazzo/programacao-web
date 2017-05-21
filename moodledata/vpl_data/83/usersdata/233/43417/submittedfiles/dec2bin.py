# -*- coding: utf-8 -*-
numero=int(input('Digite um número ieirol na base decimal: '))
soma=0
i=0
while numero>0:
    m=numero%10
    soma=soma+m*10**i
    numero=numero//10
    i=i+1
print(soma)    
    

