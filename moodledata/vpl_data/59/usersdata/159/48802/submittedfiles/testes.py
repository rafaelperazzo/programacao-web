# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
a=int(input('Digite a:'))
b=int(input('Digite b:'))
i=1
while i<=n:
    if i%a==0:
        print(i)
    else i%b==0:
        print(i)
    i=i+1    
       