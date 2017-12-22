# -*- coding: utf-8 -*-
while True:
    n=int(input('Digite um valor: '))
    if n>=1:
        break
soma=0
resto=n%10
while resto>=0:
    soma=soma+resto
print(soma)
    
    
