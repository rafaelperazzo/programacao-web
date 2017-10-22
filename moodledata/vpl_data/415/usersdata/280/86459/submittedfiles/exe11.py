# -*- coding: utf-8 -*-
num=int(input("Número: "))
n=num
sum=0
k=7
l=0
kap=num//(10**l)
for i in range (0,8,1):
    n=(num//(10**k)) - kap
    kap=n
    sum = sum + n
    k = k - 1
    l = l + 1
    print ("--------------")
    print (num)
    print (n)
    print (kap)
    print (k)
    print (l)
    print (sum)
    print ("--------------")