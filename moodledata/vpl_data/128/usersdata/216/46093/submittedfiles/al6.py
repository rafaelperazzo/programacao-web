# -*- coding: utf-8 -*-
n=int(int(input('Digite um número:'))
cont=0
for i in range(2,n,1):
    if n%i==0:
        cont=cont+1
        print(cont)
if cont==0:
    print('primo')
else:
    print('não primo')