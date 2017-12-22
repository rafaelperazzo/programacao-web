# -*- coding: utf-8 -*-
n=int(input('Digite um valor: '))
soma=0
while True:
    resto= n%10
    soma=soma+resto
    if resto==0:
        print(soma)
        break
    
    
