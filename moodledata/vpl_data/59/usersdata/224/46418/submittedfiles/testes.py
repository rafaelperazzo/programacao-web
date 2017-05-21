# -*- coding: utf-8 -*-
n=int(input('Digite o valor n: '))
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor b: '))
cont=0
i=0
cont1=0
for i in range(1,n+1,1):
    cont=a*i
    cont1=b*i
        if cont!=cont1:
           print(cont)
           print(cont1)
        else:
            print(cont)
        cont=cont+1
        cont1=cont1+1