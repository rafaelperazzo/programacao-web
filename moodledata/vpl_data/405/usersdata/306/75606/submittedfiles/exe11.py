# -*- coding: utf-8 -*-
a=int(input("Digite o número: "))

b=a/100000000
c=a/10000000
d=(a-10000000)/1000000
e=(a-10000000)/100000
f=(a-10000000)/10000
g=(a-10000000)/1000
h=(a-10000000)/100
i=(a-10000000)/10

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

