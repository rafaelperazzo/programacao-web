# -*- coding: utf-8 -*-
while True:
    n=int(input('Digite um valor: '))
    if n>=1:
        break
soma=0
resto=0
while resto<=n:
    resto=n%10
    soma=soma+resto
print(soma)


    
    
