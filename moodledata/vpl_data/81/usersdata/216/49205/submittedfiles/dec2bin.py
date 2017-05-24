# -*- coding: utf-8 -*-
p=int(input('Digite um número:'))
q=int(input('Digite um número:'))

cont=0
t=p


while t>0:
    p=t//10
    cont=cont+1

cont2=0
while q>0:
    n=q%(10**cont)
    q=q//10
if cont2>0:
    print('S')
else:
    print('N')
      


