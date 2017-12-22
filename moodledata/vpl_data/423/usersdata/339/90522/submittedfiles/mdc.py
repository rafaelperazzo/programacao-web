# -*- coding: utf-8 -*-
import math

n1=int(input('n1: '))
n2=int(input('n2: '))


while n1%2==0 or n2%2==0 :
    n1 = n1/2
    n2 = n2/2
    print(n1 , n2)
    if n1%2!=0:
        break
    while n1%3==0 or n2%3==0 :
        n1 = n1/3
        n2 = n2/3
        print(n1 , n2)
        if n1%3!=0:
            break
        while n1%5==0 or n2%5==0 :
                n1 = n1/5
                n2 = n2/5
                print(n1 , n2)
                if n1%5!=0:
                    break





