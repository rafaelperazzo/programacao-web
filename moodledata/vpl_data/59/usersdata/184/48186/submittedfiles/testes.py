d1=int(input('digite o primeiro dia:'))
m1=int(input('digite o primeiro mês:'))
a1=int(input('digite o primeiro ano:'))
d2=int(input('digite o segundo dia:'))
m2=int(input('digite o segundo mês:'))
a2=int(input('digite o segundo ano:'))
if a1>=a2:
    print('data 1')
elif a2>=a1:
    print('data 2')
else:
    if m1>=m2:
        print('data 1')
    elif m2>=m1:
        print('data 2')
    else:
        if d1>=d2:
            print('data 1')
        else:
            print('data 2')