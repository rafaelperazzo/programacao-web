# -*- coding: utf-8 -*-
num=int(input("Número: "))
k=7
l=8
m=0
sum=0
if num <= 9999999 or num > 99999999:
    print ("NAO SEI")
else:
    for i in range (0,8,1):
        n=(num//(10**k)) - ((num//(10**l))*(10))
        sum = sum + n
        k = k - 1
        l = l - 1
        print (n)
        print (sum)
        print ("---------------")