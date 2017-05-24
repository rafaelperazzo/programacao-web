a=int(input('numero:'))
xc=int(input('xc'))
yc=int(input('yc'))
x=0
for i in range(0,a,1):
    x=int(input('x'))
    y=int(input('y'))
    d=abs(x-xc)+abs(y-yc)
    if d<x:
       x=d
print(d)       