# -*- coding: utf-8 -*-
npessoas=int(input('Digite o número de pessoas detectadas pelo sensor: '))
soma=0
soma1=0
soma2=0
for i in range(0,npessoas,1):
    instante=float(input('Digite o instante em que a pessoa foi detectada: '))
    soma=soma1-soma
    soma1=instante
    soma2=soma2+soma
print (soma2+10)