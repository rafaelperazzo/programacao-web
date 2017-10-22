# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

n=int(input('n: '))
cont=0

for i in range(2,n,1):
    n+=cont
    if n%i==0:
        cont+=1
    
if cont>0:
    print ('%d Nao eh primo' %n)
else:
    print ('%d eh primo' %n)


