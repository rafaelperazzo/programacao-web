a = input(' digite o valor de a ')
b = input(' digite o valor de b ')
c = input(' digite o valor de c ')
delta = b**2 - 4*a*c
print  delta 

 if delta > 0:
     x1 = (-b + delta**0.5)/ 2.0 * a
     x2 = (-b - delta**0.5)/2.0*a
     print x1,x2
else:
    print ' nao pode ser calculado '
     
     