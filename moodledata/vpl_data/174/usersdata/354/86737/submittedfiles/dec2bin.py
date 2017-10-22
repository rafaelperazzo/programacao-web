# -*- coding: utf-8 -*-

p=int(input('digite o valor do menor numero: '))
q=int(input('digite o valor do maior numero: '))
z=p
cont=0
while (p>0):
     cont = cont +1
     p=p//10
i=0
while (q>0):
    if(q%(10**cont)==z):
        i=0
        break
    else:
        i=i+1
    q=q//10
if(i!=0):
    print('N')
else:
    print('S')
