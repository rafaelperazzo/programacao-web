# -*- coding: utf-8 -*-
n=int(input('Digite n: '))
cont=0
i=2
while i<n:
    v=n%i
    if v==0:
        cont=cont+i
    i=i+1
if cont!=n:
    print('n perfeito')
else:
    print('é perfeito' )