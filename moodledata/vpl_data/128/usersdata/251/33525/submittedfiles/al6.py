# -*- coding: utf-8 -*-
n = int(input('Digite um número qualquer: '))
decisao = 0
i = 2

while i<n:
    if n%i==0:
        decisao = decisao+1
        print('%d'%i)
    i=i+1
    
if decisao==0:
    print('primo')
    
else:
    print('Não primo')
    