# -*- coding: utf-8 -*-
num=int(input("Número: "))
n=num
sum=0
k=7
while n%10 != 0:
    n=num//(10**k)
    sum = sum + n
    k = k - 1
    print (num)
    print (n)
    print (k)
    print (sum)