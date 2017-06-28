def degrau(b):
    a=[]
    for i in range(0,len(a)-1,1):
        diferença=bs(a[i]-a[i+1])
        a.append(diferença)
    return(a)

def mmaior(b):
    c=degrau(b)
    maior=c[0]
    for i in range(0,len(c),1):
        if c[i]>maior:
            maior=c[i]
    return (maior)

m=int(input('m: '))
b=[]
for i in range(1,m+1,1):
    y=int(input('y: '))
    b.append(y)

print(mmaior(b))