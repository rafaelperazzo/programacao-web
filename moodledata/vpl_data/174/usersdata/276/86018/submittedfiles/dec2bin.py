# -*- coding: utf-8 -*-
p = int(input('Digite o valor do numero menor: '))
q = int(input('Digite o calor do numero maior: '))

p1 = p

cont = 0
while (p>0):
    cont = cont + 1
    p = p//10
    
i = 0
while (q>0):
    if (q%(10**cont) == p1):
        i = 0
    else:
        i = i + 1
    q = q//10


if (i!=0):
    print ('N')
elif (i==0):
    print ('S')

    