# -*- coding: utf-8 -*-
n=int(input('Digite o valor n: '))
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor b: '))
cont=0
i=0
for i in range(1,n+1,1):
    if (a*i)==(b*i):
        cont=cont+1
    else:
        cont=cont+2
    print(cont)