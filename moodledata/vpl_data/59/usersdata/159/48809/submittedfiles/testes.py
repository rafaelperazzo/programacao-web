# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
a=int(input('Digite a:'))
b=int(input('Digite b:'))
i=1
cont=0
while cont<=n:
    if i%a==0:
        print(i)
        cont=cont+1
    elif i%b==0:
        print(i)
        cont=cont+1
    i=i+1    
       