# -*- coding: utf-8 -*-

a=int(input('Digite a : '))
b=int(input('Digite b : '))
c=int(input('Digite c : '))
i=0
cont=0

if a>=b:
    p=a
    s=b
if a<b:
    s=a
    p=b

while (i<c):
    produto= i*p
    X9= c - (i*p)
    if X9%s==0:
        print(i)
        print(X9/s)
        cont=cont+1
        break
    else:
        i=i+1
if cont==0:
    print('N')
    


    