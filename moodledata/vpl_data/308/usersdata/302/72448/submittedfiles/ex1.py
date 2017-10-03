a = float(input('digite a: '))
b = float(input('digite b: '))
c = float(input('digite c: '))

delta=b**2-4*a*c

if delta>=0:
    x1=(b**2+(delta**0.5))/2*a
    print(x1)