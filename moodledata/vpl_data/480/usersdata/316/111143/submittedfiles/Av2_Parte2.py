# -*- coding: utf-8 -*-
n=int(input('digite um numero maior ou igual a um: '))
while n<1:
    print('digite um numero maior ou igual a um: ')

while n>=1:
    if n<10:
        print(n)
        break
    else:
        al=n//10
        if al//n==0:
            print('1')
        while al>=10:
            al=n//10
            print(al)
    
            
            
        
        
        