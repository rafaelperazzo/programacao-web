# -*- coding: utf-8 -*-

a=int(input('Digite o valor da moeda:'))
b=int(input('Digite o valor da moeda:'))
c=int(input('Digite o valor da cedula:')) 


j=0
cont=0
#i=c//a
i = c//a
while i>=0:
    
    if ((i*a) +(b*j))==c:
        cont=cont+1
        break
    i=i-1
    j=j+1
    

if cont!=0:
    print(i)
    print(j)
else:
    print('N')
    