# -*- coding: utf-8 -*-
n=float(input('digite seu nùmero na base binária'))
n=int(n)
decimal=0
elevado=0
while (n//10)>0:
    q=n%10
    decimal=decimal+(2**elevado)*q
    n=n//10
    elevado=elevado+1
print(decimal)
