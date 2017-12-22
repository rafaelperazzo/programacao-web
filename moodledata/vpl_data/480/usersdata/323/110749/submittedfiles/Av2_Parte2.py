# -*- coding: utf-8 -*-
while True:
    n=int(input('Digite um valor: '))
    if n>=1:
        break
soma=0

for i in range(0,n,1):
    resto=n%10
    soma=soma+resto
print(soma)
    
    
