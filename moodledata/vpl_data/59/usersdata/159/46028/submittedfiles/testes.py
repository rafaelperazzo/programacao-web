# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
i=1
contador=0
while i<=n:
    if n%i==0:
        if n%(i+1)==0:
            if n%(n+2)==0:
                contador=contador+1
    i=i+1
if contador!=0:
    print('É triangular')
else:
    ('Não é triangular')
 

    