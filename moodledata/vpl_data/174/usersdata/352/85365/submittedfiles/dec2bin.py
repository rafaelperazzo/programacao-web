# -*- coding: utf-8 -*-


p=int(input('Digite o numeros: '))
q=int(input('Digite o segundo numeros: '))

cont=0
valorp=p
cont2=0
while p>0:
    q=q//10
    cont=cont+1

while (q>0):
    if q%(10**cont)==valorp:
        cont2=cont2+1
    q=q//10
if cont2==0:
    print('N')
else:
    print('S')