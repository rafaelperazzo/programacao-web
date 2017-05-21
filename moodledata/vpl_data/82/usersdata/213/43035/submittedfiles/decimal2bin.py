# -*- coding: utf-8 -*-
numero=int(input('Informe um número binário: '))
i=0
soma=0
while numero>0:
    m=numero%10
    soma=soma+m*(2**i)
    numero=numero//10
    i=i+1
print(soma)

