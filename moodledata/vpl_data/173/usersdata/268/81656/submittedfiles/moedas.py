# -*- coding: utf-8 -*-
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor da cédula: '))
w=0
x9=0
while(w<c):
    duvida= a*w
    comprovacao= (c-a*w)
    if (comprovacao%b)==0:
        print(w)
        print(comprovacao/b)
        break
    else:
        x9=x9+1
        w=w+1

if(x9==c):
    print('N')
    