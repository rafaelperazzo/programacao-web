# -*- coding: utf-8 -*-
n=int(input('n:'))
if n%20==0:
    q=n//20
    print(q)
    print('0')
    print('0')
    print('0')
    print('0')
if n%20!=0:
    x=n%20
    print(n//20)
    if x%10==0:
        print(x//10)
        print('0')
        print('0')
        print('0')
    if x%10!=0:
        x=x%10
        print('0')
        
    

