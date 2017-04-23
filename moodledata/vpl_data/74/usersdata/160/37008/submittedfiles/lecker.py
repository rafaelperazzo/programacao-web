a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
d=float(input('Digite d:'))


if a>=0 and b>=0 and c>=0 and d>=0:
    if a>b:
        cont=a+1
        
    if b>a and b>c:
        cont=b+1
    
    if c>d:
        cont=d+1
    
    print('S')
else:
    print('N')
    