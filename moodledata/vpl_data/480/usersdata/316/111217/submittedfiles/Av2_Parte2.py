# -*- coding: utf-8 -*-
n=int(input('digite um numero maior ou igual a um: '))
while n<1:
    print('digite um numero maior ou igual a um: ')

while n>=1:
    if n<10:
        print(n)
        break
    elif n==10:
        print(1)
        break
    else:
        al=n%10
        while al>=1:
            print(al)
            al=al%10
            print(al)
            
    
            
            
        
        
        