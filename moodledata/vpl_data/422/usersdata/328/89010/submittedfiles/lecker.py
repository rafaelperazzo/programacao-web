n1=int(input('n1:'))
n2=int(input('n2:'))
n3=int(input('n3:'))
n4=int(input('n4:'))
if n1 >n2 and n4<n3:
    print('S')
elif n2 >n1> n3 and n4<n3 :
    print('S')
elif n3>n4>n2 and n1<n2:
    print('S')
elif n4>n3 and n1<n2:
    print('S')
else:
    print('N')