def degrau(b):
    a=[]
    for i in range(0,len(a)-1,1):
        diferença=bs(a[i]-a[i+1])
        a.append(diferença)
    return(a)
def maiordegrau(a):
    maior=a[0]
    for i in range(0,len(a)-1,1):
        if a[i]>maior:
            maior=a[i]
    return (maior)
m=int(input('m: '))
b=[]
for i in range(1,m+1,1):
    y=int(input('y: '))
    b.append(y)
print(maiordegrau(b))