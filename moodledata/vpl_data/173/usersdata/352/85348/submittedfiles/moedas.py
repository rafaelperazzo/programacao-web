# -*- coding: utf-8 -*-

a=int(input('Digite o valor da moeda:'))
b=int(input('Digite o valor da moeda:'))
c=int(input('Digite o valor da cedula:')) 

i=c//a
cont=0
while i>0:
    troco=(c-(i*a))//b
    if ((i*a) + ((troco)*b))==c:
        cont=cont+1
        break
    i=i-1

if (cont==0):
    i=c//b
    cont2=0
    while i>0:
        troco2=(c-(i*b))//a
        if ((i*b) + ((troco)*a))==c:
            cont2=cont2+1
            break
    i=i-1
    if (cont2==0):
        print('N')
    else:
        print(i)
        print(troco2)
else:
    print(i)
    print(troco)

