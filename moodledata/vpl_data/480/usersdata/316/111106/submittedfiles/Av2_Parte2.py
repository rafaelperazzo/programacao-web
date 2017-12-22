# -*- coding: utf-8 -*-
n=int(input('digite um numero maior ou igual a um: '))
while n<1:
    print('digite um numero maior ou igual a um: ')

while n>=1:
    if n<10:
        print(n)
        break
    elif n>=10 and n<=99:
        print('2')
    elif n>=100 and n<=999:
        print('3')
    elif n>=1000 and n<=9999:
        print('4')
    elif n>=10000 and n<=99999:
        print('5')
    elif n>=100000 and n<=999999:
        print('6')         
            
            
            
        
        
        