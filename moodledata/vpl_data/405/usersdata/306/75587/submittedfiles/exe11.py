# -*- coding: utf-8 -*-
a=int(input("Digite o número: "))

b=a/100000000
c=a/10000000
d=c/1000000

if b>=1/10 and b<=1:
    print("OK")
else:
    print("NAO SEI")

print("%.d"%c)
print("%.d"%d)
