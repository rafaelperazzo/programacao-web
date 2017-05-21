import math
n=int(input('digite n: '))
x=int(input('digite x: '))
I=0
exp=1
for i in range(0,n,1):
    if i%2==0:
        I=I+(x**exp)/(exp*math.factorial(i))
    else:
        I=I-(x**exp)/(exp*math.factorial(i))
    exp=exp+2
print(I)