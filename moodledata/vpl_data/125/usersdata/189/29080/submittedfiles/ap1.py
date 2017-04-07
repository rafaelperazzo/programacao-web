a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
if a>=b and a>=c and b>=c:
    print('%d' %a)
    print('%d' %b)
    print('%d' %c)
if a>=b and a>=c and c>=b:
    print('%d' %a)
    print('%d' %c)
    print('%d' %b)
if b>=a and b>=c and a>=c:
    print('%d' %b)
    print('%d' %a)
    print('%d' %c)
if b>=a and b>=c and c>=a:
    print('%d' %b)
    print('%d' %c)
    print('%d' %a)
if c>=a and c>=b and a>=b:
    print('%d' %c)
    print('%d' %a)
    print('%d' %b)
if c>=a and c>=b and b>=a:
    print('%d' %c)
    print('%d' %b)
    print('%d' %a)