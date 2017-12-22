# -*- coding: utf-8 -*-
n=int(input('digite um numero maior ou igual a um: '))
while n<1:
    print('digite um numero maior ou igual a um: ')
ct=0
while ct<=n:
    ct=ct+1
    if ct==n:
        al=n
        print(al)
    else:
        ct=ct+1
        al=n//ct
        print(al)