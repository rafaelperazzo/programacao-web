# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite o numero:'))
cont=0
n2=n
while n2!=0:
    cont=cont+1
    n2=n2//10
print(cont) 
n3=n
bin=0
while n3%10!=0:
    bin=bin+(n%10)*(10**cont)
    n3=n3//10
    cont=cont-1
print(bin)    

