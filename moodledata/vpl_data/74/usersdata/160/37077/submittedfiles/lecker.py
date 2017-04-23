a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
d=float(input('Digite d:'))


if a>=0 and b>=0 and c>=0 and d>=0:
    if a==b==c==d:
        print('N')
    
    elif a>b:
        cont=a+1
        print('S')
        
    elif b>a and b>c:
        cont=b+1
        print('S')
    
    elif c>d:
        cont=c+1
        print('S')
        
    elif d>a and d>b and d>a:
        cont=d+1
        print('S')

else:
    print('N')
    