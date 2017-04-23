# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input('Digite um numero inteiro qualquer: '))
i = 1
fatorial = 0
while i<n:
    if n%i==0:
        print('%d'%i)
        fatorial= fatorial*i
    i=i+1
    

    
