def cresc(a):
    cont=0
    for i  in range(0,len(a)/2+1,1):
        if a[i]<a[i+1]:
            cont=cont+1
        else:
            return False
    if cont==len(a)-1:
        return True
    else:
        return False
def decresc(a):
    cont=0
    for i in range(len(a)-1,-1,-1):
        if a[i]>a[i+1]:
            cont=cont+1
        else:
            return False
    if cont==len(a)-1:
        return True
    else:
        return False
n=int(input('n'))
a=[]
for i in range(1,n+1,1):
    x=float(input('Digite x: '))
    a.append(x)
if cresc(a) and decresc(a):
    print('S')
else:
    print('N')
