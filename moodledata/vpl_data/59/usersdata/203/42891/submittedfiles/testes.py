n=float(input('digite n: '))
exp=0
s=0
r=n%2
while r!=0:
    r=n%2
    s=s+r*(10**exp)
    n=n//2
    exp=exp+1
print(s)