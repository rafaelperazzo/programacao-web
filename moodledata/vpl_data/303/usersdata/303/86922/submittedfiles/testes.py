# -*- coding: utf-8 -*
n1= int(input('DIGITE O PRIMEIRO NUMERO:'))
n2= int(input('DIGITE O SEGUNDO NUMERO:'))
n3= int(input('DIGITE O TERCEIRO NUMERO:'))
n4= int(input('DIGITE O QUARTO NUMERO:'))
while( n1<n2<n3<n4):
    print('S')
    break 
while( n1<n2<n3>n4):
    print('S')
    break
while (n1<n3<n4<n2):
    print('S')
    break
while (n2<n2<n3<n1):
    print('S')
    break
else:
    print('N')

    

    
    