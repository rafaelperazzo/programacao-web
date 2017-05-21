# -*- coding: utf-8 -*-
p=int(input('Digite número inteiro positivo p: '))
q=int(input('Digite número inteiro positivo q: '))
cont=0
temp=p
while p>0:
    cont=cont+1
    temp=temp//10
cont2=0
while q<0:
    n=q%(10**cont)
    if n==p:
        cont2=cont2+1
    q=q+1
if cont2>0:
    print('S')
else:
    print('N')

