a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
d=float(input('Digite d:'))


if cont>=0:
    if a>b:
        cont=cont+1
        
    if b>a and b>c:
        cont=cont+1
    
    if c>d:
        cont=cont+1
    
    if cont==1:
        print('S')
    else:
        print('N')
    