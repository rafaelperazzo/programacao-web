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
        while al>9:
            al=n//10
            print(al)
    
            
            
        
        
        