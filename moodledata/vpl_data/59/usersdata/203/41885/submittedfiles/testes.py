n=float(input('digite n: '))
exp=0
while r!=0:
    r=n%2
    s=s+r*10**exp
    n=n//2
print(s)