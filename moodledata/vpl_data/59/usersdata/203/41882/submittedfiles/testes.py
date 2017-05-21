import math
a=float(input('digite a: '))
b=float(input('digite b: '))
n=int(input('digite n: '))
h=(b-a)/n
s=0
x=a+h
while x<=b-h:
    s=s+x**3-4*x-5
    x=x+h
I=(h/2)*((a**3-4*a-5) + (b**3-4*b-5) + (2*s))
print(I)