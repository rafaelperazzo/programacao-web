n=input('digite n:')
L=[]
for i in range(1,n+1,1):
    L.append(input('digite um valor:'))
for i in range(0,n,1):
    if L[i]>5:
        print (L[i])