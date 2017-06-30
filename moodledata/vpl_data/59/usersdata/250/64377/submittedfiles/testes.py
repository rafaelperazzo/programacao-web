# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('n:'))
a=[]
while n>0:
    if n>=10:
        digito=n%10
        a.append(digito)
    else:
        a.append(n)
    n=n//10
print(a)
    