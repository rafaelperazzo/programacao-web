import math
a=float(input('digite a: '))
a=int(a)
b=float(input('digite b: '))
b=int(b)
contador=0
x=a
while x<=b:
    if (math.cos(x)-math.exp(x))<0:
        contador=contador+1
    x=x+0.01
if contador==0:
    print('crescente')
else:
    print('não')