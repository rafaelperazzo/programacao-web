# -*- coding: utf-8 -*-
p=int(input('Digite um número:'))
q=int(input('Digite um número:'))

cont=0
t=p
cont2=0 
n=0

while t>0:
    cont=cont+1
    p=t//10
    t=p
    
   
while q>0:
    n=q%(10**cont)
    if n==p:
        print('S')


      


