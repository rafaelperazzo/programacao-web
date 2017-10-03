# -*- coding: utf-8 -*-
n=int(input("número com 8 algarismos: "))
if 0< n//10**7 <=9:
    a=n//10**7
    r1=n%10**7
    b=r1//10**6
    r2=r1%10**6
    c=r2//10**5
    r3=r2%10**5
    d=r3//10**4
    r4=r3%10**4
    e=r4//10**3
    r5=r4%10**3
    f=r5//10**2
    r6=r5%10**2
    g=r6//10
    r7=r6%10
    print(a+b+c+d+e+f+g+r7)
else:
    print('NAO SEI')