# -*- coding: utf-8 -*-
n=int(input('digite um numero maior ou igual a um: '))
while n<1:
    print('digite um numero maior ou igual a um: ')
ct=0
while ct<=n:
    if n<9:
        print(n)
        break
    else:
        for i in range(0,n,1):
            soma=i%n
           
        
        