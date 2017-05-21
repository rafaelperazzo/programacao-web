# -*- coding: utf-8 -*-
n=int(input('Digite um número: '))
cont=0
a=0
for i in range (2, n, 1):
    if (n%i==0):
        a=n//i
        print(i)
        cont=cont+1
if (cont==0):
    print('PRIMO')
else:
    print('NÃO PRIMO')