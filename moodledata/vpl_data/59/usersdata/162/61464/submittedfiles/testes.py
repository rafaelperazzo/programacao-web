def pico(a):
   v=(len(a)+1)//2
    for i in range(1,v,1):
        if a[i]>a[i+1]:
            return False
    for i  in range(v-1,len(a)-1,1):
        if a[i]<a[i+1]:
            return False
    return True
n=int(input('n: '))
h=[]
for i in range(1,n+1,1):
    x=int(input('x'))
    h.append(x)
if pico(h):
    print('S')
else:
    print('N')