# -*- coding: utf-8 -*-
n=int(input('Digite o Valor de N:'))
cont=0
for i in range(2,n,1):
    if n%i==0:
        cont=cont+1
        print(i)
if cont==0:
 print('primo')
else: 
   print('não primo')