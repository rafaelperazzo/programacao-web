def pico(a):
    a=(len(a)+1)//2
    for i in range(1,a,1):
        if a[i]>a[i+1]:
            return False
    for i in range(a-1,len(a)-1,-1):
        if a[i]<a[i+1]:
            return False
    return True
    
n=int(input('n'))
a=[]
for i in range(1,n+1,1):
    x=float(input('Digite x: '))
    a.append(x)
if pico(a):
    print('S')
else:
    print('N')
