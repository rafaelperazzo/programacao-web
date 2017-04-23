a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
d=float(input('Digite d:'))

    
if a<b and b<c and c<d:
    print('S')
    
elif a<b and b<c and c>d:
    print('S')
    
elif b>a>c>d:
    print('S')
    
elif b<a<c<d:
    print('S')

else:
    print('N')
    