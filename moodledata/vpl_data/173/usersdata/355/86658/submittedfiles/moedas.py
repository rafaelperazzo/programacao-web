# -*- coding: utf-8 -*-
a=int(input('Digite o valor da moeda 1: '))
b=int(input('Digite o valor da moeda 2: '))
c=int(input('Digite o valor da cédula: '))

qa=0
x9=0

while qa<a:
    y= a*qa
    w=c-y
    if (w%b)==0:
        print(qa)
        print(w/b)
        break
    else:
        x9=x9+1
        qa=qa+1
if(x9==c):
    print('N')
    
        