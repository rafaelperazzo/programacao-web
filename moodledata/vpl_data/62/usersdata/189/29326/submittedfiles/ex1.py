a=float(input('digite a:'))
b= float(input('digite b:'))
c= float(input('digite c:'))
delta=b*b-(4*a*c)
if delta>=0:
    x1=(-b+delta**(1/2))/(2*a)
    x2=(-b-delta**(1/2))/(2*a)
    print('x1 %.2f' %x1)
    print('x2 %.2f' %x2)
else:print('SRR')

