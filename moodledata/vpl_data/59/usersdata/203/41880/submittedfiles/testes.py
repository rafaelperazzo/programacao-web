import math
a=int(input('digite a: '))
b=int(input('digite b: '))
n=int(input('digite n: '))
h=(b-a)/n
s=a**3-4*a-5
for i in range(a,b+1,h):
    s=s+i**3-4*i-5
I=(h/2)*(a**3-4*a-5 + b**3-4*b-5 + 2*s)
print(I)