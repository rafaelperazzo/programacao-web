# -*- coding: utf-8 -*-
cont=0
i= 2
n= int(input('Digite o valor: '))
while (i<n):
    
    if (n%i==0):
        print(i)
        cont=cont+1
        
    i=i+1
if (cont==0):
    print('PRIMO')
else:
    print('NÃO PRIMO')
