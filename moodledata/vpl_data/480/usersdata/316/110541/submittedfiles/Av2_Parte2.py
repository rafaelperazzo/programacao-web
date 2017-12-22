# -*- coding: utf-8 -*-
n=int(input('digite um numero maior ou igual a um: '))
while n<1:
    print('digite um numero maior ou igual a um: ')

while n>=1:
    if n<10:
        print(n)
        break
    else:
        ct=10
        al=n//ct
        if al>=10:
            ct=10
            al=n//ct
        else:
            print(al)
        
        
        