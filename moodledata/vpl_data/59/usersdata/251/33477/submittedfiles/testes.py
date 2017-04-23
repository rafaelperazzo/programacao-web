# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input('Digite um numero qualquer: '))
decisao = 0
i = 2

while i<n:
    if n%i=0:
        decisao = decisao+1
        print('%d'%i)
        
    i=i+1
    
    
if decisao==0:
    print('Primo')
    
else:
    print('Não primo')