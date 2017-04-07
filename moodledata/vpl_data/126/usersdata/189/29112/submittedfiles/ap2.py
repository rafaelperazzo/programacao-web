a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=float(input('digite d:'))
if a>=b and a>=c and a>=d and b>=c and b>=d:
    print('%d' %a)
    print('%d' %b)
if b>=a and b>=c and b>=d and a>=c and a>=d:
    print('%d' %b)
    print('%d' %a)