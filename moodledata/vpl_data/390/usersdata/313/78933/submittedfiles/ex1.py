
 #x2 -5x +6 =0
 
a = float(input(' digite o valor de a '))

b = float(input(' digite o valor de b ')) 
     
c = float(input( 'digite o valor de c '))

delta = (b*b) - 4*a*c

if delta >= 0:
    print('x1,x2')
else:
    print("SRR")
x1 = (-b+delta**0.5)/2*a
x2 = (-b-delta**0.5)/2*a
print( '%.2f'  % x1 )
print( '%.2f'  % x2 )

   

     
     