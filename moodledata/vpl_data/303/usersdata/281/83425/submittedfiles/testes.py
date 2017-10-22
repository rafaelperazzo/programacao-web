# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite um número:'))
fatorial=1
while n<0:
    print('Número inválido!')
    n=int(input('Digite um número:'))

for n in range(n,0,-1):
    fatorial=fatorial*n
print(fatorial)  

    
    
    
    
