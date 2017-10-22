# -*- coding: utf-8 -*-
x=int(input("digite um numero de 8 algarismos: "))
while 10000000>x<100000000 :
    print('NAO SEI')
    x=int(input("digite um numero de 8 algarismos: "))
a=x//10000000
r=x%10000000
b=r//1000000
t=r%1000000
c=t//100000
u=t%100000
d=u//10000
v=u%10000
e=v//1000
w=v%1000
f=w//100
x=w%100
g=x//10
y=x%10
soma=a+b+c+d+e+f+g+y
print('%d'%soma)