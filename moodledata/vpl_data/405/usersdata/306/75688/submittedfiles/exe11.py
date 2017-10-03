# -*- coding: utf-8 -*-
a=int(input("Digite o número: "))

b=a/100000000



c=a//10**7
d=(a-(c*(10**7)))//10**6
e=(a-(c*(10**7)-(d*(10*6))))//10**5

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

