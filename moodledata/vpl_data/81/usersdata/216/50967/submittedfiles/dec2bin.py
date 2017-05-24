# -*- coding: utf-8 -*-
p=int(input('Digite um número:'))
q=int(input('Digite um número:'))

cont=0

while p>0:
    cont=cont+1
    p=p//10

    
cont2=0    
while q>0:
    n=q%(10**cont)
    if n==p:
        cont2=cont2+1
        q=q//10
if cont2>0:
    print('S')
else:
    print('N')
      


