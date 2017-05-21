n=float(input('digite n: '))
n=int(n)
exp=0
s=0
r=0
while n//2!=0:
    r=n%2
    s=s+r*(10**exp)
    n=n//2
    exp=exp+1
print(s)