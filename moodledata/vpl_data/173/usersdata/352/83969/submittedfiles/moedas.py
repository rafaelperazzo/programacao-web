# -*- coding: utf-8 -*-

a=int(input('Digite o valor da moeda:'))
b=int(input('Digite o valor da moeda:'))
c=int(input('Digite o valor da cedula:')) 


j=0
cont=0
while :
    i=c//a
    i=i-1
    j=j+1
    if ((i*a) +(b*j))==c:
        print(i)
        print(j)
    cont=cont+1
if cont==0:
    print('N')
