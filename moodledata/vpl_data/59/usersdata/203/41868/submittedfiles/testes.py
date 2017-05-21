import math
a=float(input('digite a: '))
a=int(a)
b=float(input('digite b: '))
b=int(b)
x=a
while x<=b:
    if (math.cos(x)-math.exp(x))>0:
        print('crescente')
    x=x+0.01