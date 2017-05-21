# -*- coding: utf-8 -*-
n=int(input('escreva o valor de n:'))
cont=0
for i in range(1,n):
    if n%i==0:
        print(i)
        cont=cont+1
if cont==0:
    print('perfeito')
else:
    print('não perfeito')
