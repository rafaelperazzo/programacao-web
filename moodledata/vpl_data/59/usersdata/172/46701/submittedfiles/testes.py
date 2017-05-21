# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('n:'))
a=int(input('a:'))
b=int(input('b:'))
i=1
while i<=n:
    if i%a==0 or i%b==0:
        print(i)
        i=i+1
   