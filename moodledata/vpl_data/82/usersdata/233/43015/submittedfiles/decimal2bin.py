# -*- coding: utf-8 -*
binario=int(input('Digite um número binário: '))
soma=0
i=0
while binario>0:
    binario=binario%10
    soma=soma+n*2**i
    binario=binario//10
    i=i+1
print(soma)