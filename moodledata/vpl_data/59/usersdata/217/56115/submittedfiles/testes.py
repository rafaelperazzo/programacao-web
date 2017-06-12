n=int(input('digite n:'))
a=[]
for i in range(1,n+1,1):
    a.append(input('digite um valor:'))
for i in range(0,n,1):
    if a[i]>5:
        print (a[i])