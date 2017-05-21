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
        print(x//10)
        if x%5==0:
            print(x//5)
            print('0')
            print('0')
        if x%5!=0:
            x=x%5
            print(x//5)
            if x%2==0:
                print(x//2)
                print('0')
            if x%2!=0:
                x=x%2
                print(x//2)
                if x%1==0:
                    print(x//1)
                    print(22222222)
        
    

