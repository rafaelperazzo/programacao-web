# -*- coding: utf-8 -*-
n=int(input("Digite um número com 8 algarismos: "))
if n//10**7 >0:
    a=n//(10**7)
    r1=n%10**7
    b=((r1*10)//10)
    r2=((r1*10)%10)
    c=((r2*10)//10)
    r3=((r2*10)%10)
    d=((r3*10)//10)
    r4=((r3*10)%10)
    e=((r4*10)//10)
    r5=((r4*10)%10)
    f=((r5*10)//10)
    r6=((r5*10)%10)
    g=((r6*10)//10)
    r7=((r6*10)%10)
    h=((r7*10)//10)
    print(a+b+c+d+e+f+g+h)
else:
    print("NAO SEI")