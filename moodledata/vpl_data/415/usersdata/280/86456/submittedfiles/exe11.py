# -*- coding: utf-8 -*-
num=int(input("Número: "))
n=num
sum=0
k=7
l=0
kap=0
while n%10 != 0:
    n=(num//(10**k)) - (kap*(10**l))
    kap=n
    sum = sum + n
    k = k - 1
    l = l + 1
    print ("--------------")
    print (num)
    print (n)
    print (k)
    print (l)
    print (sum)
    print ("--------------")