d1=int(input('Digite o dia 1:'))
m1=int(input('Digite o mes 1:'))
a1=int(input('Digite o ano 1:'))

d2=int(input('Digite o dia 2:'))
m2=int(input('Digite o mes 2:'))
a2=int(input('Digite o ano 2:'))

if a1>a2:
    print('Data 1')

elif a1<a2:
    print('Data 2')

else:
    if m1>m2:
        print('Data 1')
    
    elif m1<m2:
        print ('Data 2')
    
else:
    if d1>d2:
        print('Data 1')
    
    elif d1<d2:
        print('Data 2')

else:
    print ('Iguais)