# -*- coding: utf-8 -*-

a=int(input('Digite o valor da moeda:'))
b=int(input('Digite o valor da moeda:'))
c=int(input('Digite o valor da cedula:')) 


j=0
cont=0
#i=c//a
while i>=0:
    i=c//a
    
    if ((i*a) +(b*j))==c:
        break
    i=i-1
    j=j+1
    cont=cont+1
if cont!=0:
    print(i)
    print(j)
else:
    print('N')
    