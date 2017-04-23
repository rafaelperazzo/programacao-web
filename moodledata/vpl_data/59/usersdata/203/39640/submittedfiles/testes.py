n=int(input('n: '))
a1=1
a2=1
for i in range(1,n+1,1):
    prox=a1+a2
    a1=a2
    a2=prox
if a1>a2:
    print(a1)
else:
    print(a2)