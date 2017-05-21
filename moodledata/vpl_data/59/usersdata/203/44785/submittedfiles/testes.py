import math
n=int(input('digite n: '))
x=int(input('digite x: '))
I=0
exp=1
for i in range(0,n+1,1):
    I=I+(x**exp)/(exp*math.factorial(i))
    if i%2==0:
        I=I*(-1)
    exp=exp+2
print(I)