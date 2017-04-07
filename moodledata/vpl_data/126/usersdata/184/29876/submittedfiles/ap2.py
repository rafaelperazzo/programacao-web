a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))
d=int(input('digite o valor de d:'))
if a>=b and a>=c and a>=d:
    print(a)
    if b<=c and b<=d:
        print(b)
    elif c<=b and c<=d:
        print(c)
    else:
        print(d)
elif b>=a and b>=c and b>=d:
    print(b)
    if a<=c and a<=d:
        print(a)
    elif c<=a and c<=d:
        print(c)
    else:
        print(d)
elif c>=a and c>=b and c>=d:
    print(c)
    if a<=b and a<=d:
        print(a)
    elif b<=a and b<=d:
        print(b)
    else:
        print(d)
else:
    print(d)
    if a<=b and a<=c:
        print(a)
    elif b<=a and b<=c:
        print(b)
    else:
        print(c)
