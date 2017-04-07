a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=float(input('digite d:'))
if a>=b and a>=c and a>=d and b>=c and b>=d:
    print('%d' %a)
    print('%d' %b)
if a>=b and a>=c and a>=d and c>=b and c>=d:
    print('%d' %a)
    print('%d' %c)
if a>=b and a>=c and a>=d and d>=b and d>=c:
    print('%d' %a)
    print('%d' %d)
if b>=a and b>=c and b>=d and a>=b and a>=d:
    print('%d' %b)
    print('%d' %a)
if b>=a and b>=c and b>=d and c>=a and c>=d:
    print('%d' %b)
    print('%d' %c)
if b>=a and b>=c and b>=d and d>=a and d>=c:
    print('%d' %b)
    print('%d' %d)
if c>=a and c>=b and c>=d and a>=c and d>=d:
    print('%d' %c)
    print('%d' %a)
if c>=a and c>=b and c>=d and b>=c and b>=d:
    print('%d' %c)
    print('%d' %b)
if c>=a and c>=b and c>=d and d>=a and d>=b:
    print('%d' %c)
    print('%d' %d)
if d>=a and d>=b and d>=c and a>=b and a>=c:
    print('%d' %d)
    print('%d' %a)
if d>=a and d>=b and d>=c and b>=a and b>=c:
    print('%d' %d)
    print('%d' %b)
if d>=a and d>=b and d>=c and c>=a and c>=b:
    print('%d' %d)
    print('%d' %c)