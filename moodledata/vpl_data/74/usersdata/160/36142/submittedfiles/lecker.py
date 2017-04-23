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
    
elif a==b and b==d and c>d:
    print('S')
    
elif a==b==c==d:
    print('N') 
else:
    print('N')
    