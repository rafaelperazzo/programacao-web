
def f1 (a,b,c):
    a=int(input('a:'))
    b=int(input('b:'))
    c=int(input('c:'))
    if a>=b and a>=c:
        return a
    if b>=a and b>=c:
        return b
    if c>=a and c>=b:
        return c