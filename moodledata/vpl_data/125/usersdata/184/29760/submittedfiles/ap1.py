a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
if a<b and a<c:
    print(a)
elif b<c:
    print(b)
    print(c)
else:
    print(c)
    print(b)
if b<a and b<c:
    print(b)
elif a<c:
    print(a)
    print(c)
else:
    print(c)
    print(a)
if c<a and c<b:
    print(c)
elif a<b:
    print(a)
    print(b)
else:
    print(b)
    print(a)
