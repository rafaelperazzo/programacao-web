# -*- coding: utf-8 -*- 
n=int(input('Digite  um número inteiro: '))
cont=0
for i in range (2,n,1):
    if n%i==0:
        cont=cont+1
if cont==0:
    print('%.f'%primo')
else:
    print('Não primo')
    