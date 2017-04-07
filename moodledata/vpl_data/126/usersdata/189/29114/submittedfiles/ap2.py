a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=float(input('digite d:'))
if a>=b and a>=c and a>=d and b>=c and b>=d:
    print('%d' %a)
    print('%d' %b)
elif a>=b and a>=c and a>=d and c>=b and c>=d:
    print('%d' %a)
    print('%d' %c)
else a>=b and a>=c and a>=d and d>=b and d>=c:
    print('%d' %a)
    print('%d' %d)

