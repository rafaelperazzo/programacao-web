# -*- coding: utf-8 -*-

a=int(input('Digite o valor da moeda:'))
b=int(input('Digite o valor da moeda:'))
c=int(input('Digite o valor da cedula:')) 


j=0
cont=0
i=(c//a)+1
while (((i*a) + (b*j))==c):
    j=0
    while (((i*a) + (b*j))==c):
        j=j+1
        
    i=i-1    
    cont=cont+1
if cont>1:
    print(i)
    print(j)
else:
    print('N')
    