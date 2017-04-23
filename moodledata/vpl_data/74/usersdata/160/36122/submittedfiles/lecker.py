a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
d=float(input('Digite d:'))

if a==b==c==d:
    print('N')
    
elif a<b and b<c and c>d:
    print('S')

    
elif a<b and b>c and c<d:
    print('S')
    
elif a==b and b<d and c>d:
    print('S')
    
else:
    print('N')
    
    
    