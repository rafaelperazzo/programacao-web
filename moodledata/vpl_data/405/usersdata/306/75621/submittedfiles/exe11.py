# -*- coding: utf-8 -*-
a=int(input("Digite o número: "))

b=a/100000000
c=a/10000000
d=(c-10000000)/1000000
e=(d-10000000)/1000000
f=(e-10000000)/1000000
g=(f-10000000)/1000000
h=(g-10000000)/1000000
i=(h-10000000)/1000000

if b>=1/10 and b<=1:
    print("OK")
else:
    print("NAO SEI")

print("%.d"%c)
print("%.d"%d)
print("%.d"%e)
print("%.d"%f)
print("%.d"%g)
print("%.d"%h)
print("%.d"%i)

