a=float(input('digite a'))
b=float(input('digite b'))
c=float(input('digite c'))
d=float(input('digite d'))
if a>b and a>c and a>d:
    print(a)
    if b<c and b<d:
        print(b)
elif c<b and c<d:
    print(c)
else:
    print(d)
    if b>a and b>c and b>d:
        print(b)
    if a<c and a<d:
        print(a)
    elif c<b and c<d:
        print(c)
    else:
        print(d)
    if c>a and c>b and c>d:
        print(c)    
    if a<b and a<d:
        print(a)
    if b<a and b<d:
        print(b)
    else:
        print(d)
else: print(d)

    
    
    
   