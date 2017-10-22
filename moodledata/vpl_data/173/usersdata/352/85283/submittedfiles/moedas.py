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

if (cont==0):    
    j=0
    cont=0
    #i=c//a
    i = c//b
    while i>=0:
    
        if ((i*b) +(a*j))==c:
            cont2=cont2+1
            break
        i=i-1
        j=j+1
    if cont2==0:
        print('N')
    else:
        print(i)
        print(j)
else:
    print(i)
    print(j)