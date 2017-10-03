# -*- coding: utf-8 -*-
x=int(input('Digite 8 algarismos: '))
if x<10000000:
    print('NAO SEI')
elif x>=10000000:
    x1=x//10000000
    x2=x%10000000
    x3=x2//1000000
    x4=x2%1000000
    x5=x4//100000
    x6=x4%100000
    x7=x6//10000
    x8=x6%10000
    x9=x8//1000
    x10=x8%1000
    x11=x10//100
    x12=x10%100
    x13=x12//10
    x14=x12%10
    x15=x14//1
    print(x1+x3+x5+x7+x9+x11+x13+x15)