# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
i=1
while i>=n:
    if n%i==0 and n%(i+1)==0 and n%(i+2)==0:
        print('é triangular')
    else:
        print('Não é triangular')
    i=i+1
    