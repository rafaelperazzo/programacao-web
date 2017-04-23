n=int(input('n: '))
a1=1
a2=1
for i in range(3,n+1,1):
    prox=a1+a2
    a1=a2
    a2=prox
print(prox)