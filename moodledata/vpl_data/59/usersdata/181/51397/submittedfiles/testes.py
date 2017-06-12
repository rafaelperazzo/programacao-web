n=int(input('digite n:'))
x1=int(input('digite x1:'))
x2=int(input('digite x2:'))
y1=int(input('digite y1:'))
y2=int(input('digite y2:'))
if (x1<=(n/2) and x2>(n/2)) or (x2<=(n/2) and x1>(n/2)) or (y1<=(n/2) and y2>(n/2)) or (y2<=(n/2) and y1>(n/2)):
    print('S')
else:
    print('N')
