a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
delta=(b*b)-(4*a*c)
if delta>=0:
   x1=(-b+delta**0.5)/(2*a)
   x2=(-b-delta**0.5)/(2*a)
   print('X1:%.2f'% x1)
   print('X2:%.2f'% x2)
else:
    print('SSR')
    
